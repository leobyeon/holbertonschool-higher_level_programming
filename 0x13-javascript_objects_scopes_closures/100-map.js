#!/usr/bin/node
let arr = require('./100-data.js').list;
console.log(arr);
console.log(arr.map((x, index) => x * index));
