#!/usr/bin/node
const myargs = process.argv.slice(2);
let result = 0;
function add (a, b) {
  result = a + b;
  return result;
}
add(parseInt(myargs[0]), parseInt(myargs[1]));
console.log(result);
