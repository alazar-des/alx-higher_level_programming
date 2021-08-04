#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    let ch;
    if (c === undefined) { ch = 'X'; } else { ch = c; }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) { process.stdout.write(ch); }
      console.log('');
    }
  }
}

module.exports = Square;
