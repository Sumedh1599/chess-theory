#!/usr/bin/env node
/**
 * Chess Theory — Unified Installer
 * Detects agent, drops skill files, initializes repo
 *
 * Flags:
 *   --dry-run   Preview actions without writing files
 *   --help      Show usage
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

const ARGS = process.argv.slice(2);
const isDryRun = ARGS.includes('--dry-run');
const wantHelp = ARGS.includes('--help') || ARGS.includes('-h');

const PROVIDERS = [
  {
    id: 'claude-code',
    name: 'Claude Code',
    skillDir: () => path.join(os.homedir(), '.claude', 'skills'),
    hooksDir: () => path.join(os.homedir(), '.claude', 'hooks'),
    rulesDir: null,
    pluginDir: () => path.join(os.homedir(), '.claude', 'plugins'),
  },
  {
    id: 'cursor',
    name: 'Cursor',
    skillDir: null,
    hooksDir: null,
    rulesDir: () => path.join(os.homedir(), '.cursor', 'rules'),
    pluginDir: null,
  },
  {
    id: 'windsurf',
    name: 'Windsurf',
    skillDir: null,
    hooksDir: null,
    rulesDir: () => path.join(os.homedir(), '.windsurf', 'rules'),
    pluginDir: null,
  },
  {
    id: 'cline',
    name: 'Cline',
    skillDir: null,
    hooksDir: null,
    rulesDir: () => path.join(os.homedir(), '.cline', 'rules'),
    pluginDir: null,
  },
  {
    id: 'copilot-chat',
    name: 'GitHub Copilot Chat',
    skillDir: null,
    hooksDir: null,
    rulesDir: () => path.join(os.homedir(), '.github', 'copilot', 'rules'),
    pluginDir: null,
  },
];

const REPO_ROOT = process.cwd();
const CHESS_DIR = path.join(REPO_ROOT, '.chess');

function detectProviders() {
  const found = [];
  for (const p of PROVIDERS) {
    let exists = false;
    if (p.skillDir && fs.existsSync(p.skillDir())) exists = true;
    if (p.hooksDir && fs.existsSync(p.hooksDir())) exists = true;
    if (p.rulesDir && fs.existsSync(p.rulesDir())) exists = true;
    if (p.pluginDir && fs.existsSync(p.pluginDir())) exists = true;
    if (exists) found.push(p);
  }
  return found;
}

function ensureDir(dir) {
  if (fs.existsSync(dir)) return;
  if (isDryRun) {
    console.log(`  [DRY-RUN] Would create: ${dir}`);
    return;
  }
  fs.mkdirSync(dir, { recursive: true });
  console.log(`  Created: ${dir}`);
}

function copyFile(src, dest) {
  if (isDryRun) {
    console.log(`  [DRY-RUN] Would install: ${dest}`);
    return;
  }
  fs.copyFileSync(src, dest);
  console.log(`  Installed: ${dest}`);
}

function writeFile(dest, content) {
  if (isDryRun) {
    console.log(`  [DRY-RUN] Would write: ${dest}`);
    return;
  }
  fs.writeFileSync(dest, content);
  console.log(`  Created: ${path.relative(REPO_ROOT, dest) || dest}`);
}

function installForProvider(provider, sourceDir) {
  console.log(`\n📦 Installing for ${provider.name}...`);

  if (provider.skillDir) {
    const dir = provider.skillDir();
    ensureDir(dir);
    const skillSrc = path.join(sourceDir, 'skills', 'chess', 'SKILL.md');
    if (fs.existsSync(skillSrc)) {
      copyFile(skillSrc, path.join(dir, 'chess.md'));
    }
  }

  if (provider.hooksDir) {
    const dir = provider.hooksDir();
    ensureDir(dir);
    const hooksSrc = path.join(sourceDir, 'src', 'hooks');
    if (fs.existsSync(hooksSrc)) {
      for (const file of fs.readdirSync(hooksSrc)) {
        copyFile(path.join(hooksSrc, file), path.join(dir, file));
      }
    }
  }

  if (provider.rulesDir) {
    const dir = provider.rulesDir();
    ensureDir(dir);
    const ruleSrc = path.join(sourceDir, '.cursor', 'rules', 'chess.mdc');
    if (fs.existsSync(ruleSrc)) {
      copyFile(ruleSrc, path.join(dir, 'chess.mdc'));
    }
  }

  if (provider.pluginDir) {
    const dir = provider.pluginDir();
    ensureDir(dir);
    const pluginSrc = path.join(sourceDir, 'plugins', 'chess');
    if (fs.existsSync(pluginSrc)) {
      for (const file of fs.readdirSync(pluginSrc)) {
        copyFile(path.join(pluginSrc, file), path.join(dir, file));
      }
    }
  }
}

function initRepo() {
  console.log('\n🔧 Initializing Chess in current repo...');
  ensureDir(CHESS_DIR);

  const historyFile = path.join(CHESS_DIR, 'history.jsonl');
  if (!fs.existsSync(historyFile)) {
    writeFile(historyFile, '');
  }

  const specFile = path.join(CHESS_DIR, 'spec.yaml');
  if (!fs.existsSync(specFile)) {
    writeFile(specFile, 'future:\n  # Auto-populated by chess-init\n  # Add your project constraints here\n');
  }

  const patternsFile = path.join(CHESS_DIR, 'patterns.json');
  if (!fs.existsSync(patternsFile)) {
    writeFile(patternsFile, '{}');
  }

  console.log(isDryRun ? '  [DRY-RUN] Repo init previewed' : '  ✅ Repo initialized');
}

function main() {
  if (wantHelp) {
    console.log(`♟ Chess Theory installer

Usage:
  node cli/install.js [--dry-run] [--help]

Options:
  --dry-run   Show what would be installed without writing files
  --help      Show this help
`);
    return;
  }

  console.log('♟ CHESS THEORY — Unified Installer\n');
  if (isDryRun) console.log('🔎 DRY-RUN mode — no files will be written\n');

  const sourceDir = path.resolve(__dirname, '..');
  const providers = detectProviders();

  if (providers.length === 0) {
    console.log('⚠️  No AI agents detected. Install Cursor, Claude Code, Windsurf, or Cline first.');
    console.log('   Chess files will still be copied to current repo.');
  } else {
    console.log(`Found ${providers.length} agent(s): ${providers.map((p) => p.name).join(', ')}`);
    for (const p of providers) {
      installForProvider(p, sourceDir);
    }
  }

  initRepo();

  if (isDryRun) {
    console.log('\n✓ DRY-RUN COMPLETE — no files written');
    console.log('Re-run without --dry-run to actually install');
    return;
  }

  console.log('\n✅ Chess Theory installed!');
  console.log('\nNext steps:');
  console.log('  1. Open your agent (Cursor / Claude Code / etc)');
  console.log('  2. Type: /chess');
  console.log('  3. Or type: /chess init  (to scan repo dependencies)');
  console.log('\nDocs: https://github.com/Sumedh1599/chess-theory');
}

main();
