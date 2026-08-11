/**
 * Chess Theory — Init Wrapper
 */

const { execSync } = require('child_process');
const path = require('path');

function runInit() {
  const initScript = path.join(__dirname, '..', '..', 'src', 'tools', 'chess-init.js');
  execSync(`node "${initScript}"`, { stdio: 'inherit' });
}

module.exports = { runInit };
