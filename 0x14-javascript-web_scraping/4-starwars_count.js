#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);
const path = myArgs[0];
const options = { json: true };
const charId = 'https://swapi-api.hbtn.io/api/people/18/';
let count = 0;

request(path, options, function (error, response, body) {
  if (error) console.error('error:', error);
  for (let i = 0; i < body.results.length; i++) {
    for (let j = 0; j < body.results[i].characters.length; j++) {
      if (charId === body.results[i].characters[j]) {
        count++;
      }
    }
  }
  console.log(count);
});
