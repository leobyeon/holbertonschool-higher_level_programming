#!/usr/bin/node
const request = require('request');
let url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (err, resp, body) {
  (err) ? console.log(err) : console.log(JSON.parse(body).title);
});
