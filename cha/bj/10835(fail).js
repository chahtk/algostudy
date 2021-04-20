const readline = require('readline');

let dp = [];

const solve = (N, LD, RD, left, right) => {
  if (left === N || right === N) return;
  if (LD[left] > RD[right]) {
    if (
      dp[left][right + 1] === -1 ||
      dp[left][right + 1] < dp[left][right] + RD[right]
    ) {
      dp[left][right + 1] = dp[left][right] + RD[right];
      solve(N, LD, RD, left, right + 1);
    }
  } else {
    if (
      dp[left + 1][right + 1] === -1 ||
      dp[left + 1][right + 1] < dp[left][right]
    ) {
      dp[left + 1][right + 1] = dp[left][right];
      solve(N, LD, RD, left + 1, right + 1);
    }
    if (dp[left + 1][right] === -1 || dp[left + 1][right] < dp[left][right]) {
      dp[left + 1][right] = dp[left][right];
      solve(N, LD, RD, left + 1, right);
    }
  }
};

const input = () => {
  let N;
  let leftDeck = [];
  let rightDeck = [];

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  rl.on('line', (line) => {
    if (!N) {
      N = +line;
      dp = Array.from(Array(N + 1), () => Array(N + 1).fill(-1));
    } else if (leftDeck.length !== N) {
      leftDeck = line.split(' ').map((el) => +el);
    } else {
      rightDeck = line.split(' ').map((el) => +el);
      solve(N, leftDeck, rightDeck, 0, 0);
      let ans = 0;
      dp.map((rows) => {
        rows.map((col) => {
          if (ans < col) ans = col;
        });
      });
      console.log(ans);
      rl.close();
    }
  }).on('close', () => process.exit());
};

input();
