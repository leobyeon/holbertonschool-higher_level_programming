#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, resp) { (err) ? console.log(err) : console.log('code:', resp.statusCode); });
