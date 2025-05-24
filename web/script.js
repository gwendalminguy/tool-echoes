var year = new Date().getFullYear()
var json = require(`../data/exports/${year}.json`);
var count = json["count"]
var titles = json["titles"]
var artists = json["artists"]
var genres = json["genres"]
console.log(count, titles, artists, genres);