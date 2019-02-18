#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  // Method
  print () {
    for (let i = 0; i < this.height; i++) { console.log('X'.repeat(this.width)); }
  }
  // Method
  rotate () {
    let tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
  // Method
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
