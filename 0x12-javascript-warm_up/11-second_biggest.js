#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let arr = process.argv.slice(2)
  console.log(arr.sort((a, b) => a - b)[arr.length - 2]);
}
