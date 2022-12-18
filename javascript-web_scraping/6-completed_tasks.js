#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const lista = JSON.parse(body);
    console.log(lista.reduce((ret, el) => {
      if (el.completed) {
        if (ret[el.userId]) {
          ret[el.userId]++;
        } else {
          ret[el.userId] = 1;
        }
      }
      return ret;
    }, {}));
  }
});
