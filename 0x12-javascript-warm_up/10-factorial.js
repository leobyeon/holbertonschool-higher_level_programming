#!/usr/bin/node
console.log(factorial(parseInt(process.argv[2])));
function factorial(n) {
  if (!n || n === 1) { return 1; } else { return n * factorial(n - 1); }
}
