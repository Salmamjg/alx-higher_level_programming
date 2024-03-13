#!/usr/bin/node
const NumberArgs = Math.floor(Number(process.argv[2]));
console.log(isNaN(NumberArgs) ? 'Not a number' : `My number: ${NumberArgs}`);
