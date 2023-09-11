#!/usr/bin/node
const myargs = process.argv.slice(2);
let i, k;
if (isNaN(myargs[0])) {
	console.log('Missing size');
} else {
	for (i = 0; i < parseInt(myargs[0]); i++) {
		let row = '';
		for (k = 0; k < parseInt(myargs[0]); k++) {
			row += 'X';
		}
		console.log(row);
	}
}
