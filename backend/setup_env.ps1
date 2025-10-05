param(
    [string]$PythonExecutable = "python"
)

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPath = Join-Path $projectRoot "venv"
$requirementsFile = Join-Path $projectRoot "requirements.txt"
$appFile = Join-Path $projectRoot "app.py"

Write-Host "Project root:" $projectRoot
Write-Host "Using python executable:" $PythonExecutable

if (-not (Test-Path $requirementsFile)) {
    throw "requirements.txt not found at $requirementsFile"
}

if (-not (Test-Path $venvPath)) {
    Write-Host "Creating virtual environment..."
    & $PythonExecutable -m venv $venvPath
} else {
    Write-Host "Virtual environment already exists." -ForegroundColor Yellow
}

$venvPython = Join-Path $venvPath "Scripts/python.exe"
if (-not (Test-Path $venvPython)) {
    throw "Unable to locate python inside venv at $venvPython"
}

Write-Host "Upgrading pip inside the virtual environment..."
& $venvPython -m pip install --upgrade pip

Write-Host "Installing Python dependencies..."
& $venvPython -m pip install -r $requirementsFile

Write-Host "Verifying Flask installation..."
& $venvPython -m pip show Flask

if (-not (Test-Path $appFile)) {
    Write-Host "app.py not found at $appFile. Skipping run." -ForegroundColor Yellow
    return
}

Write-Host "Starting Flask app..."
& $venvPython $appFile
