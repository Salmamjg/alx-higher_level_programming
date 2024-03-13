#!/usr/bin/node
function add(a, b){
    return a + b;
}
const a = parseInt(Number(process.argv[2]));
const b = parseInt(Number(process.argv[3]));
if(isNaN(a) || isNaN(b)){
    console.log('NaN');
} else{
    const result = add(a, b);
    console.log(`${result}`);
}
