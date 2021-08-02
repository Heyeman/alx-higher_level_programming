#!/usr/bin/node
const {argv} = require('process');
num = parseInt(argv[2]);
if (num == NaN){
    console.log('Not a number');
}
else{
    console.log("My number: " + num);
}