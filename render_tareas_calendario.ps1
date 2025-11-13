Param(
    [string]$File = "tareas_calendario.qmd",
    [switch]$Offline,
    [string[]]$Mark,
    [switch]$IncludeButtonsOffline,
    [switch]$Open,
    [string]$Browser = "chrome"
)

Write-Host "[Render] Iniciando render del archivo $File" -ForegroundColor Cyan

# Verificar existencia del archivo
if (-not (Test-Path $File)) {
    Write-Error "Archivo $File no encontrado en el directorio actual."; exit 1
}

# Verificar instalación de Quarto
$quartoCmd = Get-Command quarto -ErrorAction SilentlyContinue
if (-not $quartoCmd) {
    Write-Warning "Quarto CLI no encontrado. Instala desde https://quarto.org/ antes de continuar."; exit 1
}

# Marcar tareas antes de render si se solicita
if ($Mark) {
    Write-Host "[Mark] Procesando marcas de estado..." -ForegroundColor Cyan
    $content = Get-Content $File -Raw
    foreach ($entry in $Mark) {
        # Formato esperado: Asignatura::Actividad
        if ($entry -notmatch '::') { Write-Warning "Entrada '$entry' sin '::' -> omitida"; continue }
        $parts = $entry.Split('::')
        $asig = [Regex]::Escape($parts[0].Trim())
        $act = [Regex]::Escape($parts[1].Trim())
        # Regex para fila <tr><td>Asignatura</td><td>Actividad...</td><td>...<td>...</td><td>[ ]</td>
        $pattern = "<tr><td>$asig</td><td>$act</td><td([\s\S]*?)</td><td([\s\S]*?)</td><td>\[ \]</td></tr>"
        $replacementEvaluator = {
            param($m)
            return $m.Value -replace "\[ \]", "[x]"
        }
        $newContent = [Regex]::Replace($content, $pattern, $replacementEvaluator, 'IgnoreCase')
        if ($newContent -ne $content) {
            Write-Host "[Mark] Marcada: $entry" -ForegroundColor Green
            $content = $newContent
        } else {
            Write-Warning "[Mark] No se encontró coincidencia exacta para: $entry"
        }
    }
    $content | Set-Content $File -Encoding UTF8
}

# Render principal
quarto render $File --to html

$htmlOut = [System.IO.Path]::ChangeExtension($File, 'html')
if (Test-Path $htmlOut) {
    Write-Host "[Render] Generado: $htmlOut" -ForegroundColor Green
    if ($Open) {
        # Determinar ejecutable de navegador si se especifica
        $browserExe = $null
        if ($Browser) {
            switch ($Browser.ToLower()) {
                'edge' { $browserExe = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" }
                'chrome' { $browserExe = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" }
                'firefox' { $browserExe = "C:\\Program Files\\Mozilla Firefox\\firefox.exe" }
                default { if (Test-Path $Browser) { $browserExe = $Browser } else { $browserExe = $Browser } }
            }
        }
        # Resolver ruta absoluta y garantizar uso como archivo local (evita http://tareas_calendario.html/)
        try { $fullHtmlPath = (Resolve-Path $htmlOut).Path } catch { $fullHtmlPath = $htmlOut }
        if ($browserExe -and (Test-Path $browserExe)) {
            Write-Host "[Open] Abriendo en navegador especificado ($browserExe) -> $fullHtmlPath" -ForegroundColor Cyan
            try { Start-Process -FilePath $browserExe -ArgumentList $fullHtmlPath } catch { Write-Warning "No se pudo abrir el navegador especificado: $_" }
        } else {
            if ($Browser -and (-not (Test-Path $browserExe))) { Write-Warning "No se encontró ejecutable para '$Browser'. Usando asociación predeterminada." }
            Write-Host "[Open] Abriendo vía asociación de archivos -> $fullHtmlPath" -ForegroundColor Cyan
            try { Start-Process -FilePath $fullHtmlPath } catch { Write-Warning "No se pudo abrir el archivo en el navegador predeterminado: $_" }
        }
    } else {
        Write-Host "[Hint] Usa -Open para abrir el HTML automáticamente (opcional: -Browser edge|chrome|firefox|<ruta>)." -ForegroundColor DarkGray
    }
} else {
    Write-Error "Render fallido: no se encontró $htmlOut"; exit 1
}

if ($Offline) {
    Write-Host "[Offline] Preparando versión sin dependencias CDN..." -ForegroundColor Yellow
    $vendorDir = "vendor"
    if (-not (Test-Path $vendorDir)) { New-Item -ItemType Directory -Path $vendorDir | Out-Null }

    $files = @(
        @{Url='https://code.jquery.com/jquery-3.6.0.min.js'; Name='jquery-3.6.0.min.js'},
        @{Url='https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js'; Name='jquery.dataTables.min.js'},
        @{Url='https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css'; Name='jquery.dataTables.min.css'},
        @{Url='https://cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json'; Name='es-ES.json'}
    )
    if ($IncludeButtonsOffline) {
        $files += @(
            @{Url='https://cdn.datatables.net/buttons/2.4.1/js/dataTables.buttons.min.js'; Name='dataTables.buttons.min.js'},
            @{Url='https://cdn.datatables.net/buttons/2.4.1/js/buttons.html5.min.js'; Name='buttons.html5.min.js'},
            @{Url='https://cdn.datatables.net/buttons/2.4.1/css/buttons.dataTables.min.css'; Name='buttons.dataTables.min.css'},
            @{Url='https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js'; Name='jszip.min.js'}
        )
    }

    foreach ($f in $files) {
        try {
            Invoke-WebRequest -Uri $f.Url -OutFile (Join-Path $vendorDir $f.Name) -UseBasicParsing
            Write-Host "Descargado: $($f.Name)" -ForegroundColor DarkGreen
        } catch {
            Write-Warning "No se pudo descargar $($f.Url): $_"
        }
    }

    # Reemplazar referencias en HTML
    $htmlContent = Get-Content $htmlOut -Raw
    $htmlContent = $htmlContent -replace 'https://code.jquery.com/jquery-3.6.0.min.js', 'vendor/jquery-3.6.0.min.js'
    $htmlContent = $htmlContent -replace 'https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js', 'vendor/jquery.dataTables.min.js'
    $htmlContent = $htmlContent -replace 'https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css', 'vendor/jquery.dataTables.min.css'
    $htmlContent = $htmlContent -replace 'https://cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json', 'vendor/es-ES.json'
    if ($IncludeButtonsOffline) {
        $htmlContent = $htmlContent -replace 'https://cdn.datatables.net/buttons/2.4.1/js/dataTables.buttons.min.js', 'vendor/dataTables.buttons.min.js'
        $htmlContent = $htmlContent -replace 'https://cdn.datatables.net/buttons/2.4.1/js/buttons.html5.min.js', 'vendor/buttons.html5.min.js'
        $htmlContent = $htmlContent -replace 'https://cdn.datatables.net/buttons/2.4.1/css/buttons.dataTables.min.css', 'vendor/buttons.dataTables.min.css'
        $htmlContent = $htmlContent -replace 'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js', 'vendor/jszip.min.js'
    }
    $offlineOut = [System.IO.Path]::GetFileNameWithoutExtension($htmlOut) + '.offline.html'
    $htmlContent | Set-Content $offlineOut -Encoding UTF8
    Write-Host "[Offline] Generado: $offlineOut (usar junto a carpeta 'vendor/')" -ForegroundColor Green
    if ($Open) {
        Write-Host "[Open] Abriendo versión offline en navegador..." -ForegroundColor Cyan
        $targetToOpen = $offlineOut
        $browserExe = $null
        if ($Browser) {
            switch ($Browser.ToLower()) {
                'edge' { $browserExe = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" }
                'chrome' { $browserExe = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" }
                'firefox' { $browserExe = "C:\\Program Files\\Mozilla Firefox\\firefox.exe" }
                default { if (Test-Path $Browser) { $browserExe = $Browser } else { $browserExe = $Browser } }
            }
        }
        try { $fullOfflinePath = (Resolve-Path $targetToOpen).Path } catch { $fullOfflinePath = $targetToOpen }
        if ($browserExe -and (Test-Path $browserExe)) {
            try { Start-Process -FilePath $browserExe -ArgumentList $fullOfflinePath } catch { Write-Warning "No se pudo abrir el navegador especificado (offline): $_" }
        } else {
            if ($Browser -and (-not (Test-Path $browserExe))) { Write-Warning "No se encontró ejecutable para '$Browser'. Usando asociación predeterminada (offline)." }
            try { Start-Process -FilePath $fullOfflinePath } catch { Write-Warning "No se pudo abrir el archivo offline en navegador: $_" }
        }
    }
}

Write-Host "Proceso completado." -ForegroundColor Cyan
