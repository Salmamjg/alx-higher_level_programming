#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      } else {
        this.width = 0;
        this.height = 0;
      }
    }

    print() {
      if (this.width === 0 || this.height === 0) {
        console.log('');
      } else {
        const row = 'X'.repeat(this.width);
        for (let i = 0; i < this.height; i++) {
          console.log(row);
        }
      }
    }
  }
  
  module.exports = Rectangle;
  