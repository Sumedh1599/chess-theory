# Chess Theory — Windows Installer
$REPO_URL = "https://github.com/Sumedh1599/chess-theory"
$INSTALL_DIR = "$env:USERPROFILE\.chess-theory"

Write-Host "♟ CHESS THEORY — Installer" -ForegroundColor Cyan
Write-Host ""

if (Test-Path "cli\install.js") {
    $SOURCE_DIR = Get-Location
    Write-Host "📁 Installing from local directory: $SOURCE_DIR"
} else {
    Write-Host "📥 Downloading Chess Theory..."
    if (Test-Path $INSTALL_DIR) {
        Remove-Item -Recurse -Force $INSTALL_DIR
    }
    try {
        git clone --depth 1 $REPO_URL $INSTALL_DIR 2>$null
    } catch {
        Write-Host "⚠️ Git clone failed. Downloading ZIP..."
        Invoke-WebRequest -Uri "$REPO_URL/archive/refs/heads/main.zip" -OutFile "$env:TEMP\chess-theory.zip"
        Expand-Archive -Path "$env:TEMP\chess-theory.zip" -DestinationPath "$env:TEMP"
        Move-Item "$env:TEMP\chess-theory-main" $INSTALL_DIR
    }
    $SOURCE_DIR = $INSTALL_DIR
}

Set-Location $SOURCE_DIR

if (!(Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Node.js not found. Install from https://nodejs.org" -ForegroundColor Red
    exit 1
}

node cli/install.js

Write-Host ""
Write-Host "🎉 Done! Type '/chess' in your agent to activate." -ForegroundColor Green
