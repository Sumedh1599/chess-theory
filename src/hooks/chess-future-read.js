#!/usr/bin/env node
/**
 * Chess Theory — Future Self Reader (Claude Code)
 * Reads spec.yaml and emits [F] block
 */

const fs = require('fs');
const path = require('path');

function parseYamlSimple(content) {
  const lines = content.split('\n');
  const result = { future: {}, constraints: [], roadmap: [] };
  let currentSection = null;
  let currentKey = null;

  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;

    const indent = line.match(/^\s*/)[0].length;

    if (indent === 0 && trimmed.endsWith(':') && !trimmed.includes(' ')) {
      const section = trimmed.slice(0, -1);
      if (section === 'future' || section === 'constraints' || section === 'roadmap') {
        currentSection = section;
        currentKey = null;
        continue;
      }
      if (currentSection === 'future') {
        currentSection = null;
        currentKey = null;
      }
    }

    if (currentSection === 'future') {
      if (indent > 0 && indent <= 2 && trimmed.endsWith(':') && !trimmed.startsWith('-')) {
        currentKey = trimmed.slice(0, -1).trim();
        result.future[currentKey] = {};
        continue;
      }
      if (currentKey && trimmed.startsWith('- ')) {
        if (!result.future[currentKey].consumers) result.future[currentKey].consumers = [];
        result.future[currentKey].consumers.push(trimmed.replace(/^- /, '').trim());
        continue;
      }
      if (currentKey && trimmed.includes(':')) {
        const colon = trimmed.indexOf(':');
        const k = trimmed.slice(0, colon).trim();
        let v = trimmed.slice(colon + 1).trim();
        if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) {
          v = v.slice(1, -1);
        }
        if (k === 'consumers') {
          result.future[currentKey].consumers = result.future[currentKey].consumers || [];
        } else if (v) {
          result.future[currentKey][k] = v;
        }
      }
    }

    if (currentSection === 'constraints' && trimmed.startsWith('- ')) {
      result.constraints.push(trimmed.replace(/^- /, '').replace(/^["']|["']$/g, ''));
    }
  }

  return result;
}

function readSpec(projectRoot = process.cwd()) {
  const specFile = path.join(projectRoot, '.chess', 'spec.yaml');
  if (!fs.existsSync(specFile)) return null;
  try {
    return parseYamlSimple(fs.readFileSync(specFile, 'utf8'));
  } catch (_) {
    return null;
  }
}

function formatFBlock(spec) {
  if (!spec || !spec.future) {
    return '[F] C:code:0.00|⚠:0|✦:0|🔗:0b0c|🎯:0g0|L:none|A:none';
  }

  const future = spec.future;
  const keys = Object.keys(future);
  if (keys.length === 0) {
    return '[F] C:code:0.00|⚠:0|✦:0|🔗:0b0c|🎯:0g0|L:none|A:none';
  }

  let riskCount = 0;
  let oppCount = 0;
  let blastRadius = 0;
  let consumers = 0;
  let lesson = '';
  let alt = '';

  for (const [, val] of Object.entries(future)) {
    if (val.risk) riskCount++;
    if (val.upcoming) oppCount++;
    if (val.consumers) {
      consumers += val.consumers.length;
      blastRadius = Math.max(blastRadius, val.consumers.length);
    }
    if (val.constraint) lesson = val.constraint;
    if (val.upcoming) alt = typeof val.upcoming === 'string' ? val.upcoming : JSON.stringify(val.upcoming);
  }

  return `[F] C:code:0.50|⚠:${riskCount}s3r3|✦:${oppCount}s3r3|🔗:${blastRadius}b${consumers}c|🎯:+1g0|L:${lesson || 'none'}|A:${alt || 'none'}`;
}

function emitFutureSelf(projectRoot = process.cwd()) {
  return formatFBlock(readSpec(projectRoot));
}

function main() {
  try {
    console.log(emitFutureSelf(process.cwd()));
  } catch (_) {
    console.log('[F] C:code:0.00|⚠:0|✦:0|🔗:0b0c|🎯:0g0|L:none|A:none');
  }
}

if (require.main === module) main();

module.exports = {
  parseYamlSimple,
  readSpec,
  formatFBlock,
  emitFutureSelf,
};
