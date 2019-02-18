#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(function (x) { if (x === searchElement) { count++; } });
  return count;
};
