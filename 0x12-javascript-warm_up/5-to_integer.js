#!/usr/bin/node
const numberArg = process.argv[2];
const convertedNumber = parseInt(numberArg, 10);
console.log(isNaN(convertedNumber) ? "Not a number" : `My number: ${convertedNumber}`);
