#!/usr/bin/env node
/**
 * Chess Theory — Balance Calculator
 * Reads [P] and [F] blocks, computes [B] vector with all 9 LEAN paths reachable.
 *
 * Usage:
 *   node chess-balance.js "[P] ..." "[F] ..."
 *   node chess-balance.js "[P] ..." "[F] ..." --h=-2
 */

const fs = require('fs');
const path = require('path');

function parsePBlock(line) {
  const result = {
    '⚠': { count: 0, severity: 0 },
    '✓': { count: 0, severity: 0 },
    '🔄': { count: 0, severity: 0 },
    '👻': { count: 0, severity: 0 },
    '🔁': { count: 0, severity: 0 },
    '⚡': 0,
  };

  const parts = String(line || '').split('|');
  for (const part of parts) {
    if (part.startsWith('⚠:')) {
      const m = part.match(/⚠:(\d+)s(\d+)/);
      if (m) {
        result['⚠'].count = parseInt(m[1], 10);
        result['⚠'].severity = parseInt(m[2], 10);
      }
    } else if (part.startsWith('✓:')) {
      const m = part.match(/✓:(\d+)s(\d+)/);
      if (m) {
        result['✓'].count = parseInt(m[1], 10);
        result['✓'].severity = parseInt(m[2], 10);
      }
    } else if (part.startsWith('🔄:')) {
      const m = part.match(/🔄:(\d+)s(\d+)/);
      if (m) {
        result['🔄'].count = parseInt(m[1], 10);
        result['🔄'].severity = parseInt(m[2], 10);
      }
    } else if (part.startsWith('👻:')) {
      const m = part.match(/👻:(\d+)s(\d+)/);
      if (m) {
        result['👻'].count = parseInt(m[1], 10);
        result['👻'].severity = parseInt(m[2], 10);
      }
    } else if (part.startsWith('🔁:')) {
      const m = part.match(/🔁:(\d+)s(\d+)/);
      if (m) {
        result['🔁'].count = parseInt(m[1], 10);
        result['🔁'].severity = parseInt(m[2], 10);
      }
    } else if (part.startsWith('⚡:')) {
      const m = part.match(/⚡:(\d+)/);
      if (m) result['⚡'] = parseInt(m[1], 10);
    }
  }

  return result;
}

function parseFBlock(line) {
  const result = {
    '⚠': { count: 0, severity: 0, confidence: 3 },
    '✦': { count: 0, severity: 0, confidence: 3 },
    '🔗': { blast: 0, consumers: 0 },
    '🎯': 0,
  };

  const parts = String(line || '').split('|');
  for (const part of parts) {
    if (part.startsWith('⚠:')) {
      const m = part.match(/⚠:(\d+)s(\d+)r(\d+)/);
      if (m) {
        result['⚠'].count = parseInt(m[1], 10);
        result['⚠'].severity = parseInt(m[2], 10);
        result['⚠'].confidence = parseInt(m[3], 10);
      }
    } else if (part.startsWith('✦:')) {
      const m = part.match(/✦:(\d+)s(\d+)r(\d+)/);
      if (m) {
        result['✦'].count = parseInt(m[1], 10);
        result['✦'].severity = parseInt(m[2], 10);
        result['✦'].confidence = parseInt(m[3], 10);
      }
    } else if (part.startsWith('🔗:')) {
      const m = part.match(/🔗:(\d+)b(\d+)c/);
      if (m) {
        result['🔗'].blast = parseInt(m[1], 10);
        result['🔗'].consumers = parseInt(m[2], 10);
      }
    } else if (part.startsWith('🎯:')) {
      const m = part.match(/🎯:([+-]?\d+)/);
      if (m) result['🎯'] = parseInt(m[1], 10);
    }
  }

  return result;
}

function calculateHelpFromHistory(projectRoot = process.cwd()) {
  const historyPath = path.join(projectRoot, '.chess', 'history.jsonl');
  if (!fs.existsSync(historyPath)) return 0;

  let h = 0;
  try {
    const lines = fs
      .readFileSync(historyPath, 'utf8')
      .split('\n')
      .filter((l) => l.trim())
      .slice(-5);

    for (const line of lines) {
      try {
        const entry = JSON.parse(line);
        const ctx = String(entry.ctx || '').toLowerCase();
        if (entry.sig === '✓') h += 0.5;
        if (entry.sig === '⚠') h -= 0.5;
        if (ctx.includes('thanks') || ctx.includes('perfect')) h += 1;
        if (ctx.includes('confused') || ctx.includes('unclear')) h -= 1;
        if (ctx.includes('frustrated') || ctx.includes('again')) h -= 2;
      } catch (_) {}
    }
  } catch (_) {
    return 0;
  }

  return Math.max(-3, Math.min(3, Math.round(h)));
}

/**
 * LEAN rules reordered so all 9 directions are reachable.
 * First match wins.
 */
function determineLeanDirection({ r, m, c, d, s, h, fr, fo, fc }) {
  // 1. break-loop
  if (s >= 4 || (fr >= 4 && r >= 3)) return 'break-loop';
  // 2. reassure (before clarify)
  if (h <= -1 && fo >= 2) return 'reassure';
  // 3. pivot (before clarify; needs stuck + misalignment)
  if (s >= 3 && fc <= -2) return 'pivot';
  // 4. clarify — drift, or misalignment without stuck
  if (d >= 2 || (fc <= -2 && s < 3)) return 'clarify';
  // 5. slow-down
  if (r >= 3 || fr >= 4) return 'slow-down';
  // 6. hedge (before simplify so high risk+opp isn't swallowed)
  if (fr >= 3 && fo >= 3) return 'hedge';
  // 7. simplify
  if (c <= 0.3 && fr >= 3) return 'simplify';
  // 8. accelerate
  if (m >= 3 && fo >= 3) return 'accelerate';
  // 9. deepen
  return 'deepen';
}

function computeBalance(p, f, helpOverride = null, projectRoot = process.cwd()) {
  const avgSev = (sym) => p[sym].severity || 2;

  let r =
    p['⚠'].count * avgSev('⚠') * 0.4 +
    p['🔄'].count * 0.8 +
    p['👻'].count * avgSev('👻') * 0.6 -
    p['✓'].count * 0.3;
  r = Math.max(-5, Math.min(5, Math.round(r)));

  let m = p['✓'].count * 1.5 - p['⚠'].count * 0.5;
  m = Math.max(-5, Math.min(5, Math.round(m)));

  let c = p['✓'].count / (p['✓'].count + p['⚠'].count + 0.1);
  c = Math.round(c * 100) / 100;

  let d = p['⚡'] * 2;
  d = Math.max(0, Math.min(5, d));

  let s = p['🔄'].count * avgSev('🔄') + (p['🔁'].count > 2 ? 2 : 0);
  s = Math.max(0, Math.min(5, s));

  let h =
    helpOverride != null && !Number.isNaN(Number(helpOverride))
      ? Math.max(-3, Math.min(3, Number(helpOverride)))
      : calculateHelpFromHistory(projectRoot);

  let fr = (f['⚠'].count * f['⚠'].severity * f['⚠'].confidence) / 5;
  fr = Math.max(0, Math.min(5, Math.round(fr)));

  let fo = (f['✦'].count * f['✦'].severity * f['✦'].confidence) / 5;
  fo = Math.max(0, Math.min(5, Math.round(fo)));

  let fd = f['🔗'].blast;
  fd = Math.max(0, Math.min(10, fd));

  let fc = f['🎯'];
  fc = Math.max(-5, Math.min(5, fc));

  const lean = determineLeanDirection({ r, m, c, d, s, h, fr, fo, fc });
  return { r, m, c, d, s, h, fr, fo, fd, fc, lean };
}

function formatB(b) {
  const signed = (n) => (n > 0 ? `+${n}` : `${n}`);
  return `[B] r:${signed(b.r)}|m:${signed(b.m)}|c:${b.c}|d:${signed(b.d)}|s:${signed(b.s)}|h:${signed(b.h)}|fr:${signed(b.fr)}|fo:${signed(b.fo)}|fd:${b.fd}|fc:${signed(b.fc)}|LEAN→${b.lean}`;
}

function parseHelpArg(argv) {
  for (const a of argv) {
    if (a.startsWith('--h=')) return Number(a.slice(4));
    if (a.startsWith('--help-metric=')) return Number(a.slice(14));
  }
  const idx = argv.indexOf('--h');
  if (idx >= 0 && argv[idx + 1] != null) return Number(argv[idx + 1]);
  return null;
}

function main() {
  const argv = process.argv.slice(2);
  const bare = argv.filter((a) => !a.startsWith('--'));
  const pLine = bare[0] || '[P] C:code:0.00|⚠:0|✓:0|🔄:0|👻:0|🔁:0|⚡:0|L:none|A:none';
  const fLine = bare[1] || '[F] C:code:0.00|⚠:0|✦:0|🔗:0b0c|🎯:0g0|L:none|A:none';
  const help = parseHelpArg(argv);
  const b = computeBalance(parsePBlock(pLine), parseFBlock(fLine), help);
  console.log(formatB(b));
}

if (require.main === module) {
  main();
}

module.exports = {
  parsePBlock,
  parseFBlock,
  computeBalance,
  determineLeanDirection,
  calculateHelpFromHistory,
  formatB,
};
