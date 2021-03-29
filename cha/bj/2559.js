const readline = require('readline');

const solve = (arr, n, k) => {
  // k일 동안 최대 온도
  let prev = 0;
  for (let i = 0; i < k; i += 1) {
    prev += arr[i];
  }
  let ans = prev;
  for (let i = k; i < n; i += 1) {
    prev -= arr[i - k];
    prev += arr[i];
    if (prev > ans) {
      ans = prev;
    }
  }
  return ans;
};

const input = () => {
  let n;
  let k;
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  rl.on('line', (line) => {
    if (!n) {
      [n, k] = line.split(' ').map((el) => +el);
    } else {
      const arr = line.split(' ').map((el) => +el);
      const ans = solve(arr, n, k);
      console.log(ans);
      rl.close();
    }
  }).on('close', () => process.exit());
};

input();
