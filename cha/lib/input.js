const readline = require('readline');

const input = () => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  rl.on('line', (line) => {
    rl.close();
  }).on('close', () => process.exit());
};
