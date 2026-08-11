# Chess Theory — Windows Uninstaller (PowerShell 5.1+)
# Removes installed rule/skill files and ~/.chess-theory
# Does NOT delete project .chess/ folders (preserves history)

Write-Host "♟ CHESS THEORY — Uninstaller" -ForegroundColor Cyan
Write-Host ""

$keepCache = $args -contains "--keep-cache"

$paths = @(
    "$env:USERPROFILE\.cursor\rules\chess.mdc",
    "$env:USERPROFILE\.windsurf\rules\chess.mdc",
    "$env:USERPROFILE\.cline\rules\chess.mdc",
    "$env:USERPROFILE\.github\copilot\rules\chess.mdc",
    "$env:USERPROFILE\.claude\skills\chess.md"
)

$hookNames = @(
    "chess-past-cache.js",
    "chess-future-read.js",
    "chess-balance.js",
    "chess-activate.js",
    "chess-statusline.sh",
    "chess-append.js"
)

$count = 0

foreach ($path in $paths) {
    if (Test-Path $path) {
        Remove-Item -Path $path -Force -ErrorAction SilentlyContinue
        Write-Host "  Removed: $path" -ForegroundColor Green
        $count++
    }
}

$hooksDir = "$env:USERPROFILE\.claude\hooks"
if (Test-Path $hooksDir) {
    foreach ($name in $hookNames) {
        $hp = Join-Path $hooksDir $name
        if (Test-Path $hp) {
            Remove-Item -Path $hp -Force -ErrorAction SilentlyContinue
            Write-Host "  Removed: $hp" -ForegroundColor Green
            $count++
        }
    }
}

$cacheDir = "$env:USERPROFILE\.chess-theory"
if (-not $keepCache -and (Test-Path $cacheDir)) {
    Remove-Item -Path $cacheDir -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "  Removed: $cacheDir" -ForegroundColor Green
    $count++
} elseif ($keepCache) {
    Write-Host "  Kept ~/.chess-theory (--keep-cache)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "✅ Uninstall complete ($count path(s) cleaned)." -ForegroundColor Green
Write-Host "   Project .chess/ folders were left intact (history preserved)."
Write-Host "   Restart your agent if it was open."
Write-Host ""
Write-Host "To reinstall: irm https://raw.githubusercontent.com/Sumedh1599/chess-theory/main/install.ps1 | iex"
