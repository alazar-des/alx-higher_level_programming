#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const options = { json: true };

request(args[0], options, function (error, response, body) {
  if (error) console.error('error:', error);
  if (!error && response.statusCode === 200) {
    const dict = {};
    let i = 0;
    while (i < body.length) {
      let count = 0;
      const userId = body[i].userId;
      while (body[i] !== undefined && userId === body[i].userId) {
        if (body[i].completed === true) count++;
        i++;
      }
      dict[userId] = count;
    }
    console.log(dict);
  }
});
