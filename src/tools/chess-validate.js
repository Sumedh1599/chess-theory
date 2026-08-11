#!/usr/bin/env node
/**
 * chess-validate.js — Validates / repairs .chess/ directory integrity
 */

const fs = require('fs');
const path = require('path');

function validateChessDirectory(projectRoot = process.cwd()) {
  const chessDir = path.join(projectRoot, '.chess');
  const historyPath = path.join(chessDir, 'history.jsonl');
  const specPath = path.join(chessDir, 'spec.yaml');
  const issues = [];

  if (!fs.existsSync(chessDir)) {
    try {
      fs.mkdirSync(chessDir, { recursive: true });
    } catch (e) {
      issues.push(`Cannot create ${chessDir}: ${e.message}`);
    }
  }

  if (fs.existsSync(chessDir)) {
    try {
      fs.accessSync(chessDir, fs.constants.W_OK);
    } catch (e) {
      issues.push(`.chess/ directory not writable: ${e.message}`);
    }
  }

  if (fs.existsSync(historyPath)) {
    try {
      const lines = fs.readFileSync(historyPath, 'utf8').split('\n');
      let validCount = 0;
      let invalidCount = 0;
      for (const line of lines) {
        if (!line.trim()) continue;
        try {
          const entry = JSON.parse(line);
          if (entry.t == null || !entry.cat || !entry.sig) invalidCount++;
          else validCount++;
        } catch (_) {
          invalidCount++;
        }
      }
      if (invalidCount > 0) {
        issues.push(`history.jsonl has ${invalidCount} invalid lines (${validCount} valid)`);
      }
    } catch (e) {
      issues.push(`Cannot read history.jsonl: ${e.message}`);
    }

    try {
      const size = fs.statSync(historyPath).size;
      if (size > 5 * 1024 * 1024) {
        issues.push(`history.jsonl too large (${size} bytes > 5MB)`);
      }
    } catch (_) {}
  }

  if (fs.existsSync(specPath)) {
    try {
      const content = fs.readFileSync(specPath, 'utf8');
      // Lightweight YAML sanity: tabs and obvious broken keys
      if (/\t/.test(content)) {
        issues.push('spec.yaml contains tabs (prefer spaces)');
      }
      const openQuotes = (content.match(/"/g) || []).length;
      if (openQuotes % 2 !== 0) {
        issues.push('spec.yaml may have unbalanced quotes');
      }
    } catch (e) {
      issues.push(`Cannot read spec.yaml: ${e.message}`);
    }
  }

  return {
    valid: issues.length === 0,
    issues,
    timestamp: new Date().toISOString(),
  };
}

function repairChessDirectory(projectRoot = process.cwd()) {
  const chessDir = path.join(projectRoot, '.chess');
  if (!fs.existsSync(chessDir)) {
    fs.mkdirSync(chessDir, { recursive: true });
  }

  const historyPath = path.join(chessDir, 'history.jsonl');
  if (fs.existsSync(historyPath)) {
    const lines = fs.readFileSync(historyPath, 'utf8').split('\n');
    const validLines = [];
    for (const line of lines) {
      if (!line.trim()) continue;
      try {
        const entry = JSON.parse(line);
        if (entry.t != null && entry.cat && entry.sig) validLines.push(JSON.stringify(entry));
      } catch (_) {}
    }
    const temp = historyPath + '.tmp';
    fs.writeFileSync(temp, validLines.length ? validLines.join('\n') + '\n' : '', 'utf8');
    fs.renameSync(temp, historyPath);
  } else {
    fs.writeFileSync(historyPath, '', 'utf8');
  }

  const patterns = path.join(chessDir, 'patterns.json');
  if (!fs.existsSync(patterns)) fs.writeFileSync(patterns, '{}', 'utf8');

  const spec = path.join(chessDir, 'spec.yaml');
  if (!fs.existsSync(spec)) {
    fs.writeFileSync(spec, 'future:\nconstraints:\nroadmap:\n', 'utf8');
  }

  return { repaired: true, timestamp: new Date().toISOString() };
}

function main() {
  const repair = process.argv.includes('--repair');
  const rootIdx = process.argv.indexOf('--root');
  const root = rootIdx >= 0 ? process.argv[rootIdx + 1] : process.cwd();

  if (repair) {
    const r = repairChessDirectory(root);
    console.log('✓ Repaired .chess/', r.timestamp);
  }

  const result = validateChessDirectory(root);
  if (result.valid) {
    console.log('✓ Chess directory valid');
    process.exit(0);
  }
  console.log('❌ Issues:');
  for (const i of result.issues) console.log('  -', i);
  process.exit(1);
}

if (require.main === module) main();

module.exports = { validateChessDirectory, repairChessDirectory };
