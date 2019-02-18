#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let freqMap = {};
  list.forEach(function (x) { (freqMap[x]) ? freqMap[x] += 1 : freqMap[x] = 1; });
  return freqMap[searchElement];
};
