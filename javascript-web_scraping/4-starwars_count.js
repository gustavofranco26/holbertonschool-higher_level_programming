#!/usr/bin/node

const request = require('request');
request(`${process.argv[2]}`, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    console.log(films.reduce((c, e) => {
      e.characters.forEach(tu => tu.includes('18') ? c++ : c);
      return c;
    }, 0));
  }
});
