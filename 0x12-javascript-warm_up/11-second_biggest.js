#!/usr/bin/node

const args = process.argv.slice(2);
let maxIdx; let temp; let i = 0;
while (i < 2) {
  maxIdx = i;
  for (let j = i + 1; j < args.length; j++) {
    if (parseInt(args[j]) > parseInt(args[maxIdx])) {
      maxIdx = j;
    }
  }
  temp = args[maxIdx];
  args[maxIdx] = args[i];
  args[i] = temp;
  i++;
}
if (args[1] === undefined) {
  args[1] = 0;
}
console.log(parseInt(args[1]));
