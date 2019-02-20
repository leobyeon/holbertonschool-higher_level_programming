#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, resp, body) => {
  let freqMap = {};
  let results = JSON.parse(body);
  if (err) console.log(err);
  for (let key in results) {
    if (results[key].completed) {
      (freqMap[results[key].userId]) ? freqMap[results[key].userId]++ : freqMap[results[key].userId] = 1;
    }
  }
  console.log(freqMap);
});
