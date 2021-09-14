#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const fs = require('fs');

request(args[0], function (error, response, body) {
  if (error) console.error('error:', error);
  if (!error && response.statusCode === 200) {
    fs.writeFile(args[1], body, 'utf8', function (err, data) {
      if (err) console.error('error:', err);
    });
  }
});
