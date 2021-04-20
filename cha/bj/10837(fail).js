const readline = require('readline');

const solve = (k, c, arr) => {
  const dp = Array.from(Array(k + 1), () => Array(k + 1).fill(true));
  for (let i = 0; i <= k; i += 1) {
    for (let j = 0; j <= k; j += 1) {
      if (i < j) {
        if (k - j < j - i && Math.abs(i - j) !== 1) dp[i][j] = false;
      }
      if (i > j) {
        if (k - i < i - j && Math.abs(i - j) !== 1) dp[i][j] = false;
      }
    }
  }
  for (let i = 0; i < c; i += 1) {
    const [a, b] = arr[i];
    console.log(dp[a][b] ? 1 : 0);
  }
};

const input = () => {
  let k;
  let c;
  const arr = [];
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  rl.on('line', (line) => {
    if (!k) {
      k = +line;
    } else if (!c) {
      c = +line;
    } else {
      arr.push(line.split(' ').map((el) => +el));
      if (arr.length === c) {
        solve(k, c, arr);
        rl.close();
      }
    }
  }).on('close', () => process.exit());
};
input();
