#!/usr/bin/env node
/**
 * Chess Theory — Uninstaller
 * Removes installed rule/skill/hook files and optionally ~/.chess-theory
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

const HOME = os.homedir();

const TARGETS = [
  // Cursor
  path.join(HOME, '.cursor', 'rules', 'chess.mdc'),
  // Windsurf
  path.join(HOME, '.windsurf', 'rules', 'chess.mdc'),
  // Cline
  path.join(HOME, '.cline', 'rules', 'chess.mdc'),
  // Copilot
  path.join(HOME, '.github', 'copilot', 'rules', 'chess.mdc'),
  // Claude Code skill
  path.join(HOME, '.claude', 'skills', 'chess.md'),
];

const HOOK_NAMES = [
  'chess-past-cache.js',
  'chess-future-read.js',
  'chess-balance.js',
  'chess-activate.js',
  'chess-statusline.sh',
  'chess-append.js',
];

function rm(file) {
  try {
    if (fs.existsSync(file)) {
      fs.unlinkSync(file);
      console.log(`  Removed: ${file}`);
      return true;
    }
  } catch (e) {
    console.warn(`  Failed: ${file} (${e.message})`);
  }
  return false;
}

function rmDirIfEmpty(dir) {
  try {
    if (fs.existsSync(dir) && fs.readdirSync(dir).length === 0) {
      fs.rmdirSync(dir);
      console.log(`  Removed empty dir: ${dir}`);
    }
  } catch (e) {}
}

function main() {
  console.log('♟ CHESS THEORY — Uninstaller\n');

  const keepCache = process.argv.includes('--keep-cache');
  const alsoProject = process.argv.includes('--project');
  let count = 0;

  for (const t of TARGETS) {
    if (rm(t)) count++;
  }

  const hooksDir = path.join(HOME, '.claude', 'hooks');
  if (fs.existsSync(hooksDir)) {
    for (const name of HOOK_NAMES) {
      if (rm(path.join(hooksDir, name))) count++;
    }
  }

  const installDir = path.join(HOME, '.chess-theory');
  if (!keepCache && fs.existsSync(installDir)) {
    try {
      fs.rmSync(installDir, { recursive: true, force: true });
      console.log(`  Removed: ${installDir}`);
      count++;
    } catch (e) {
      console.warn(`  Failed to remove ${installDir}: ${e.message}`);
    }
  } else if (keepCache) {
    console.log('  Kept ~/.chess-theory (--keep-cache)');
  }

  if (alsoProject) {
    const chessDir = path.join(process.cwd(), '.chess');
    if (fs.existsSync(chessDir)) {
      console.log(`\n⚠️  --project set: leaving ${chessDir} intact (contains history).`);
      console.log('   Delete manually if desired: rm -rf .chess');
    }
  }

  console.log(`\n✅ Uninstall complete (${count} path(s) cleaned).`);
  console.log('   Restart your agent if it was open.');
}

main();
