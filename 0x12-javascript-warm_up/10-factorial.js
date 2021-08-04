#!/usr/bin/node

function factorial (num) {
  if (num <= 1) { return (1); } else { return (num * factorial(--num)); }
}

const args = process.argv.slice(2);
if (args[0] === undefined) { console.log(1); } else { console.log(factorial(parseInt(args[0]))); }
