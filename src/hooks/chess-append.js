#!/usr/bin/env node
/**
 * Hook entrypoint — delegates to src/tools/chess-append.js CLI.
 */
const path = require('path');
const { spawnSync } = require('child_process');

const tool = path.join(__dirname, '..', 'tools', 'chess-append.js');
const r = spawnSync(process.execPath, [tool, ...process.argv.slice(2)], {
  stdio: 'inherit',
  env: process.env,
});
process.exit(r.status == null ? 1 : r.status);
