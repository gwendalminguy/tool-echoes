let year = new Date().getFullYear();

function load() {
	document.getElementById('year').innerHTML = year;
	fetch(`../data/exports/${year}.json`)
		.then(response => response.json())
		.then(data => {
			let i = 1;
			for (const [key, value] of Object.entries(data.titles)) {
				document.getElementById(`title-${i}`).textContent = `${value.artist} : ${value.title}`;
				i++;
			}
			i = 1;
			for (const [key, value] of Object.entries(data.artists)) {
				document.getElementById(`artist-${i}`).textContent = `${value.artist} (${value.length} minutes)`;
				i++;
			}
  		});
}

function prevYear() {
	year--;
	load();
	document.getElementById('year').innerHTML = year;
}

function nextYear() {
	year++;
	load()
	document.getElementById('year').innerHTML = year;
}

function prevCard() {
	let json = require(`../data/exports/${year}.json`);
	card = json["count"];
	document.getElementById('card').innerHTML = card;
}

function nextCard() {
	let json = require(`../data/exports/${year}.json`);
	card = json.count.top_titles;
	document.getElementById('card').innerHTML = card;
}

/*
var count = json["count"]
var titles = json["titles"]
var artists = json["artists"]
var genres = json["genres"]

console.log(count, titles, artists, genres);
*/