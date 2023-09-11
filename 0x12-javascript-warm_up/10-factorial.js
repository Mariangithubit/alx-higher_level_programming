#!/usr/bin/node
const myargs = process.argv.slice(2);
function factorial (num) {
	if (isNaN(myargs[0])) {
		return 1;
	}
	if (num <= 1) {
		return 1;
	}
	return num * factorial(num - 1);
}
console.log(factorial(parseInt(myargs[0])));
