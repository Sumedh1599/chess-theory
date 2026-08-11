#!/usr/bin/env node
/**
 * Chess Theory — SessionStart Hook (Claude Code)
 * Activates chess mode on session start if flag file exists
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

const FLAG_FILE = path.join(os.homedir(), '.chess-active');
const CHESS_DIR = path.join(process.cwd(), '.chess');

function main() {
  const isActive = fs.existsSync(FLAG_FILE);
  
  if (isActive) {
    console.log('[CHESS] ♟ Three Selves engine active');
    
    if (!fs.existsSync(CHESS_DIR)) {
      fs.mkdirSync(CHESS_DIR, { recursive: true });
    }
    
    const historyFile = path.join(CHESS_DIR, 'history.jsonl');
    if (!fs.existsSync(historyFile)) {
      fs.writeFileSync(historyFile, '');
    }
    
    const specFile = path.join(CHESS_DIR, 'spec.yaml');
    if (!fs.existsSync(specFile)) {
      fs.writeFileSync(specFile, 'future:\nconstraints:\nroadmap:\n');
    }
    
    console.log('Run Three Selves deliberation before every response.');
    console.log('Read .chess/history.jsonl (last 20 lines) for Past Self.');
    console.log('Read .chess/spec.yaml for Future Self.');
  }
}

main();
