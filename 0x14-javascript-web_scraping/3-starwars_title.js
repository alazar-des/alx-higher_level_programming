#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);
const path = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
const options = { json: true };

request(path, options, function (error, response, body) {
  if (error) console.error('error:', error);
  console.log(body.title);
});
