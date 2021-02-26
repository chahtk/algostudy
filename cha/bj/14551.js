const readline = require('readline');

const solve = (decks, m) => {
  const res = decks.reduce((acc, cur) => {
    if (cur === 0) return acc % m;
    return (acc * cur) % m;
  });
  return res % m;
};

const input = () => {
  let n;
  let m;
  const decks = [];

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  rl.on('line', (line) => {
    if (!n) {
      [n, m] = line.split(' ').map((el) => +el);
      if (n === 0) {
        console.log(1 % m);
        rl.close();
      }
    } else if (decks.length !== n) {
      decks.push(+line);
      if (decks.length === n) {
        const answer = solve(decks, m);
        console.log(answer);
        rl.close();
      }
    }
  }).on('close', () => process.exit());
};

input();
