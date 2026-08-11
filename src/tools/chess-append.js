#!/usr/bin/env node
/**
 * chess-append.js
 * Appends a history entry after a Chess response.
 * Usage:
 *   node src/tools/chess-append.js --cat code --sig ✓ --s 2 --ctx "auth fix ok" --fix jwt
 *   node src/tools/chess-append.js --json '{"cat":"code","sig":"⚠","s":4,"ctx":"auth fail","fix":"none","c":0.9}'
 */

const fs = require('fs');
const path = require('path');

const VALID_SIGNALS = ['⚠', '✓', '🔄', '👻', '🔁', '⚡'];
const VALID_CATEGORIES = [
  'code', 'marketing', 'learn', 'creative', 'strategy',
  'research', 'design', 'legal', 'health', 'coaching',
  'translate', 'math', 'support', 'content', 'academic',
  'brainstorm', 'debug', 'interview', 'finance', 'project',
];

const HISTORY_LIMIT = 20;

function logDebug(projectRoot, message) {
  try {
    const chessDir = path.join(projectRoot, '.chess');
    if (!fs.existsSync(chessDir)) fs.mkdirSync(chessDir, { recursive: true });
    fs.appendFileSync(
      path.join(chessDir, 'debug.log'),
      `${new Date().toISOString()} ${message}\n`
    );
  } catch (_) {
    /* never crash on debug log */
  }
}

function appendHistoryEntry({
  category,
  confidence = 0.5,
  signal,
  severity = 2,
  context = 'none',
  fix = 'none',
  projectRoot = process.cwd(),
}) {
  const historyPath = path.join(projectRoot, '.chess', 'history.jsonl');
  const historyDir = path.dirname(historyPath);

  try {
    if (!fs.existsSync(historyDir)) {
      fs.mkdirSync(historyDir, { recursive: true });
    }

    try {
      fs.accessSync(historyDir, fs.constants.W_OK);
    } catch (e) {
      throw new Error(`.chess/ not writable: ${e.message}`);
    }

    let lastTurn = 0;
    let existingLines = [];
    if (fs.existsSync(historyPath)) {
      const raw = fs.readFileSync(historyPath, 'utf8');
      for (const line of raw.split('\n')) {
        if (!line.trim()) continue;
        try {
          const parsed = JSON.parse(line);
          existingLines.push(parsed);
          if (typeof parsed.t === 'number' && parsed.t > lastTurn) lastTurn = parsed.t;
        } catch (_) {
          /* skip corrupt lines */
        }
      }
    }

    const entry = {
      t: lastTurn + 1,
      cat: category,
      c: Math.max(0, Math.min(1, Number(confidence) || 0)),
      sig: signal,
      s: Math.max(1, Math.min(5, Math.round(Number(severity) || 2))),
      ctx: String(context || 'none').substring(0, 50),
      fix: fix || 'none',
      ts: new Date().toISOString(),
    };

    if (!VALID_SIGNALS.includes(entry.sig)) {
      throw new Error(`Invalid signal: ${entry.sig}`);
    }
    if (!VALID_CATEGORIES.includes(entry.cat)) {
      throw new Error(`Invalid category: ${entry.cat}`);
    }

    const trimmed = [...existingLines, entry].slice(-HISTORY_LIMIT);
    const content = trimmed.map((e) => JSON.stringify(e)).join('\n') + '\n';
    const tempPath = historyPath + '.tmp';
    fs.writeFileSync(tempPath, content, 'utf8');
    fs.renameSync(tempPath, historyPath);

    return entry;
  } catch (error) {
    logDebug(projectRoot, `append failed: ${error.message}`);
    console.error('❌ History append failed:', error.message);
    return null;
  }
}

function parseArgs(argv) {
  const out = {
    category: 'code',
    confidence: 0.5,
    signal: '✓',
    severity: 2,
    context: 'none',
    fix: 'none',
    projectRoot: process.cwd(),
  };

  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--json' && argv[i + 1]) {
      Object.assign(out, JSON.parse(argv[++i]));
    } else if (a === '--cat' && argv[i + 1]) out.category = argv[++i];
    else if (a === '--c' && argv[i + 1]) out.confidence = Number(argv[++i]);
    else if (a === '--sig' && argv[i + 1]) out.signal = argv[++i];
    else if (a === '--s' && argv[i + 1]) out.severity = Number(argv[++i]);
    else if (a === '--ctx' && argv[i + 1]) out.context = argv[++i];
    else if (a === '--fix' && argv[i + 1]) out.fix = argv[++i];
    else if (a === '--root' && argv[i + 1]) out.projectRoot = argv[++i];
    else if (a === '--help' || a === '-h') out.help = true;
  }
  return out;
}

function main() {
  const opts = parseArgs(process.argv.slice(2));
  if (opts.help) {
    console.log(`Usage: node chess-append.js --cat code --sig ✓ --s 2 --ctx "three words" --fix none`);
    process.exit(0);
  }

  const entry = appendHistoryEntry({
    category: opts.category || opts.cat,
    confidence: opts.confidence != null ? opts.confidence : opts.c,
    signal: opts.signal || opts.sig,
    severity: opts.severity != null ? opts.severity : opts.s,
    context: opts.context || opts.ctx,
    fix: opts.fix,
    projectRoot: opts.projectRoot,
  });

  if (!entry) process.exit(1);
  console.log(`✓ History appended: turn ${entry.t}`);
  console.log(JSON.stringify(entry));
}

if (require.main === module) {
  main();
}

module.exports = { appendHistoryEntry, VALID_SIGNALS, VALID_CATEGORIES, HISTORY_LIMIT };
