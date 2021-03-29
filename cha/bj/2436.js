/* eslint-disable radix */
const readline = require('readline');

const GCD = (a, b) => {
  if (b === 0) return a;
  return GCD(b, a % b);
};

const getCD = (num) => {
  const sqrt = Math.sqrt(num);
  const arr = [];
  for (let i = 1; i <= sqrt; i += 1) {
    if (num % i === 0) {
      if (GCD(num / i, i) === 1) {
        arr.push([i, num / i]);
      }
    }
  }
  return arr;
};

const getMinSum = (commonDevisor) => {
  let minSum = 1e9;
  let ansA;
  let ansB;
  commonDevisor.map(([x, y]) => {
    if (x + y < minSum) {
      minSum = x + y;
      ansA = x;
      ansB = y;
    }
  });
  return [ansA, ansB];
};

const solve = (gcd, lcm) => {
  const ab = parseInt(lcm / gcd);
  const commonDevisor = getCD(ab);
  const [a, b] = getMinSum(commonDevisor);
  return [gcd * a, gcd * b];
};

const input = () => {
  let a;
  let b;
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  rl.on('line', (line) => {
    if (!a) {
      [a, b] = line.split(' ').map((el) => +el);
      const ans = solve(a, b);
      console.log(ans.join(' '));
      rl.close();
    }
  }).on('close', () => process.exit());
};

input();
