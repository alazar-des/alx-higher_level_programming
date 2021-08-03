#!/usr/bin/node

const args = process.argv.slice(2);
if (isNaN(args[0])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(args[0]); i++) {
    for (let i = 0; i < parseInt(args[0]); i++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
