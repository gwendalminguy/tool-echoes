		let year = new Date().getFullYear();
		let json = require(`../data/exports/${year}.json`);

		document.getElementById('year').innerHTML = year;

		function prevYear() {
			year--;
			document.getElementById('year').innerHTML = year;
		}

		function nextYear() {
			year++;
			document.getElementById('year').innerHTML = year;
		}


/*
var count = json["count"]
var titles = json["titles"]
var artists = json["artists"]
var genres = json["genres"]

function prevCard() {
	year--;
}

function nextCard() {
	year++;
}

console.log(count, titles, artists, genres);
*/