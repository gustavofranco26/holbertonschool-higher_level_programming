#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter(function (el) {
    return (el === searchElement);
  }).length;
};
