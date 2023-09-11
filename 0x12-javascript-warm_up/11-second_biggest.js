#!/usr/bin/node
const myargs = process.argv.slice(2);
if (!myargs[0] || !myargs[2]) {
  console.log(0);
} else {
  const args = myargs.map(Number);
  const firstMax = Math.max.apply(null, args);
  args.splice(args.indexOf(firstMax), 1);
  console.log(Math.max.apply(null, args));
}
