const readline = require('readline');

const solve = (n) => {
  let cnt = 0;

  for (let i = 1; i <= n; i += 1) {
    let m = i;
    let sum = m;
    while (sum < n) {
      m += 1;
      sum += m;
    }
    if (sum === n) cnt += 1;
  }

  console.log(cnt);
};

const input = () => {
  let n;
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  rl.on('line', (line) => {
    n = +line;
    solve(n);
    rl.close();
  }).on('close', () => process.exit());
};

input();
