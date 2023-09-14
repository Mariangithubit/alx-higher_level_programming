#!/usr/bin/node
const myargs = process.argv.slice(2);
let i = 0;
if (isNaN(myargs[0])) {
  console.log('Missing number of occurrences');
} else {
  while (i < parseInt(myargs[0])) {
    console.log('C is fun');
    i++;
  }
}
