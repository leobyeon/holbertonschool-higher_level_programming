#!/usr/bin/node
const request = require('request');
let url = process.argv[2];
let count = 0;
request(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    let results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i]['characters'].length; j++) {
        if (results[i]['characters'][j].includes('/18')) { count++; }
      }
    }
    console.log(count);
  }
});
