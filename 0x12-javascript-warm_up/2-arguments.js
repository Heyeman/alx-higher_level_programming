#!/usr/bin/node
const {argv} = require('process');
let argLen = argv.length;
if (argLen == 2){
    console.log("No arguments");
}
else if (argLen == 3){
    console.log("Argument found");
}
else{
    console.log("Arguments found");
}