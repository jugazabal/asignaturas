# PowerShell script to render all Practicum actividades (QMD) to PDF and HTML
param(
    [switch]$Html,
    [switch]$Pdf
)

if(-not ($Html -or $Pdf)) { $Html = $true; $Pdf = $true }

$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$qmdFiles = @(
    Join-Path $root 'Actividad 1/actividad1.qmd';
    Join-Path $root 'Actividad 2/actividad2.qmd';
    Join-Path $root 'Actividad 3/actividad3.qmd'
)

Write-Host "[Render] Iniciando render de actividades Practicum..." -ForegroundColor Cyan

foreach($file in $qmdFiles){
    if(-not (Test-Path $file)){ Write-Warning "No encontrado: $file"; continue }
    Write-Host "[Render] Procesando $file" -ForegroundColor Yellow
    if($Pdf){
        quarto render $file --to pdf
        Write-Host "[OK] PDF generado para $file" -ForegroundColor Green
    }
    if($Html){
        quarto render $file --to html
        Write-Host "[OK] HTML generado para $file" -ForegroundColor Green
    }
}

Write-Host "[Render] Finalizado." -ForegroundColor Cyan
