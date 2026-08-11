#!/usr/bin/env node
/**
 * Chess Theory — UserPromptSubmit Hook (Claude Code)
 * Reads compressed history and emits [P] block
 */

const fs = require('fs');
const path = require('path');

const SETTINGS = { historyLimit: 20 };

function logDebug(projectRoot, message) {
  try {
    const chessDir = path.join(projectRoot, '.chess');
    if (!fs.existsSync(chessDir)) fs.mkdirSync(chessDir, { recursive: true });
    fs.appendFileSync(path.join(chessDir, 'debug.log'), `${new Date().toISOString()} ${message}\n`);
  } catch (_) {}
}

function readHistory(projectRoot = process.cwd()) {
  const historyFile = path.join(projectRoot, '.chess', 'history.jsonl');
  try {
    if (!fs.existsSync(historyFile)) return [];
    const lines = fs.readFileSync(historyFile, 'utf8').trim().split('\n').filter(Boolean);
    return lines.slice(-SETTINGS.historyLimit);
  } catch (e) {
    logDebug(projectRoot, `readHistory failed: ${e.message}`);
    return [];
  }
}

function parseHistory(lines) {
  const signals = { '⚠': [], '✓': [], '🔄': [], '👻': [], '🔁': [], '⚡': [] };
  let category = 'code';
  let conf = 0.5;
  let lesson = '';
  let action = '';

  for (const line of lines) {
    try {
      const entry = JSON.parse(line);
      if (entry.sig && signals[entry.sig]) {
        signals[entry.sig].push({ s: entry.s || 2, ctx: entry.ctx || '', fix: entry.fix || 'none' });
      }
      if (entry.cat) {
        category = entry.cat;
        conf = typeof entry.c === 'number' ? entry.c : 0.5;
      }
    } catch (_) {}
  }

  const failures = signals['⚠'];
  if (failures.length > 0) {
    const ctxs = {};
    for (const f of failures) ctxs[f.ctx] = (ctxs[f.ctx] || 0) + 1;
    const topCtx = Object.entries(ctxs).sort((a, b) => b[1] - a[1])[0];
    if (topCtx) lesson = topCtx[0];
  }

  const successes = signals['✓'];
  if (successes.length > 0) {
    const last = successes[successes.length - 1];
    action = last.fix !== 'none' ? last.fix : last.ctx;
  }

  return { category, conf, signals, lesson, action };
}

function formatPBlock(parsed) {
  const sigs = parsed.signals;
  const format = (sym) => {
    const arr = sigs[sym];
    if (!arr || arr.length === 0) return `${sym}:0`;
    const s = Math.round(arr.reduce((a, b) => a + (b.s || 2), 0) / arr.length);
    const r = arr.length;
    return `${sym}:${r}s${s}`;
  };

  const cat = parsed.category || parsed.cat || 'code';
  const conf = typeof parsed.conf === 'number' ? parsed.conf : 0;
  return `[P] C:${cat}:${conf.toFixed(2)}|${format('⚠')}|${format('✓')}|${format('🔄')}|${format('👻')}|${format('🔁')}|⚡:${sigs['⚡'].length}|L:${parsed.lesson || 'none'}|A:${parsed.action || 'none'}`;
}

function emitPastSelf(projectRoot = process.cwd()) {
  const lines = readHistory(projectRoot);
  if (lines.length === 0) {
    return '[P] C:code:0.00|⚠:0|✓:0|🔄:0|👻:0|🔁:0|⚡:0|L:none|A:none';
  }
  return formatPBlock(parseHistory(lines));
}

function main() {
  try {
    console.log(emitPastSelf(process.cwd()));
  } catch (e) {
    logDebug(process.cwd(), `past main failed: ${e.message}`);
    console.log('[P] C:code:0.00|⚠:0|✓:0|🔄:0|👻:0|🔁:0|⚡:0|L:none|A:none');
  }
}

if (require.main === module) main();

module.exports = {
  readHistory,
  parseHistory,
  formatPBlock,
  emitPastSelf,
  SETTINGS,
};
