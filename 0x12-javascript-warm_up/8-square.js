#!/usr/bin/node
if (parseInt(process.argv[2])) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    let str = '';
    for (let j = 0; j < parseInt(process.argv[2]); j++) { str += 'X'; }
    console.log(str);
  }
} else { console.log('Missing size'); }
