#!/usr/bin/node
const numberArg = process.argv[2];
console.log(isNaN(numberArg) ? "Not a number" : `My number: ${Math.floor(numberArg)}`);
