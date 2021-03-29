/* eslint-disable radix */
const readline = require('readline');

const solve = (n, arr) => {
  arr.sort((a, b) => a - b);
  let prevSum = 0;
  for (let i = 0; i < n; i += 1) {
    if (prevSum + 1 < arr[i]) {
      return prevSum + 1;
    }
    prevSum += arr[i];
  }
  return prevSum + 1;
};

const input = () => {
  let n;
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  rl.on('line', (line) => {
    if (!n) {
      n = +line;
    } else {
      const arr = line.split(' ').map((el) => +el);
      const ans = solve(n, arr);
      console.log(ans);
      rl.close();
    }
  }).on('close', () => process.exit());
};

input();
