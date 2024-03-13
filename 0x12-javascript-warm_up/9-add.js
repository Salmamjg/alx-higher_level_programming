#!/usr/bin/node
function add (a, b) {
    const c = a + b;
    console.log(c);
}
console.log(add(Number(process.argv[2]), Number(process.argv[3])));
