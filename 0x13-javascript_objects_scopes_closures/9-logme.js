#!/usr/bin/node

let funCall = 0;
exports.logMe = function (item) {
  console.log(funCall + ': ' + item);
  funCall++;
};
