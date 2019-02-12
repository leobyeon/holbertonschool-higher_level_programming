#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(process.argv[i]);
  }
  console.log(arr.sort((a, b) => a - b)[arr.length - 2]);
}
