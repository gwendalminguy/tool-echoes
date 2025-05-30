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
			i = 1;
			for (const [key, value] of Object.entries(data.genres)) {
				document.getElementById(`genre-${i}`).textContent = `${value.genre} (${value.length} minutes)`;
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

function nextCard() {
	currentIndex = (currentIndex + 1) % sections.length;
	showCard(currentIndex);
}

function prevCard() {
	currentIndex = (currentIndex - 1 + sections.length) % sections.length;
	showCard(currentIndex);
}

function showCard(index) {
	sections.forEach((section, i) => {
		section.classList.toggle('active', i === index);
	});
}
