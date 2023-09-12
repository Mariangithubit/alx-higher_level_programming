#!/usr/bin/node
const dict = require('./101-data.js').dict;
const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniqe = [...new Set(vals)];
const newDict = {};
for (const i in valsUniqe) {
  const list = [];
  for (const n in totalist) {
    if (totalist[n][1] === valsUniqe[i]) {
      list.unshift(totalist[n][0]);
    }
  }
  newDict[valsUniqe[i]] = list;
}
console.log(newDict);
