/**
 * Chess Theory — Settings Reader
 * JSONC-tolerant settings parser
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

const SETTINGS_PATH = path.join(os.homedir(), '.chess-theory', 'settings.json');

const DEFAULTS = {
  historyLimit: 20,
  compactThreshold: 100,
  verbose: false,
  categories: [
    'code', 'marketing', 'learn', 'creative', 'strategy',
    'research', 'design', 'legal', 'health', 'coaching',
    'translate', 'math', 'support', 'content', 'academic',
    'brainstorm', 'debug', 'interview', 'finance', 'project'
  ],
  signals: ['⚠', '✓', '🔄', '👻', '🔁', '⚡'],
  leanDirections: [
    'break-loop', 'slow-down', 'accelerate', 'clarify',
    'simplify', 'reassure', 'pivot', 'hedge', 'deepen'
  ]
};

function readSettings() {
  try {
    if (fs.existsSync(SETTINGS_PATH)) {
      const raw = fs.readFileSync(SETTINGS_PATH, 'utf8');
      const cleaned = raw.replace(/\/\/.*$/gm, '').replace(/\/\*[\s\S]*?\*\//g, '');
      const parsed = JSON.parse(cleaned);
      return { ...DEFAULTS, ...parsed };
    }
  } catch (e) {
    console.warn('⚠️  Failed to read settings, using defaults:', e.message);
  }
  return DEFAULTS;
}

function writeSettings(settings) {
  const dir = path.dirname(SETTINGS_PATH);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(SETTINGS_PATH, JSON.stringify(settings, null, 2));
}

module.exports = { readSettings, writeSettings, DEFAULTS };
