#!/usr/bin/node
if (process.argv.length < 3)
  console.log(0);
else {
  let arr = []
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(process.argv[i]);
  }
  console.log(arr.sort()[arr.length-2]);
}