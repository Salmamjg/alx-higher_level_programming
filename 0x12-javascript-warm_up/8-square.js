#!/usr/bin/node
const y = Math.floor(Number(process.argv[2]));
if (isNaN(y)) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < y; i++) {
        let row = '';
        for (let j = 0; j < y; j++) {
            row += 'X';
        }
        console.log(row);
    }
  }