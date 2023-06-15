#!/usr/bin/node
function add (i, x) {
  const j = i + x;
  console.log(j);
}

add(Number(process.argv[2]), Number(process.argv[3]));
