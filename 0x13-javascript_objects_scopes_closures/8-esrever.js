#!/usr/bin/node
exports.esrever = function (list) {
  let arr = [];
  for (let i = list.length - 1; i >= 0; i--) {
    arr.push(list[i]);
  }
  return arr;
};
