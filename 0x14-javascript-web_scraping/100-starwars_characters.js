#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);
const path = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0] + '/';
const options = { json: true };

request(path, options, function (error, response, body) {
  if (error) console.error('error:', error);
  if (!error && response.statusCode === 200) {
    for (let c = 0; c < body.characters.length; c++) {
      request(body.characters[c], options, function (err, resp, bdy) {
        if (err) console.error('error:', error);
        if (!err && resp.statusCode === 200) {
          console.log(bdy.name);
        }
      });
    }
  }
});
