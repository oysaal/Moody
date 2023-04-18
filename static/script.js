const form = document.querySelector('form');
const graphDiv = document.getElementById('graph');
const suggestionsDiv = document.getElementById('suggestions');

form.addEventListener('submit', (event) => {
	event.preventDefault();

	// Get mood data
	const mood = document.querySelector('input[name="mood"]:checked').value;
	const stress = document.getElementById('stress').value;
	const exercise = document.getElementById('exercise').value;
	const diet = document.getElementById('diet').value;
	const note = document.getElementById('note').value;

	// Send mood data to server
	fetch('/mood', {
		method: 'POST',
		body: JSON.stringify({ mood, stress, exercise, diet, note }),
		headers: {
			'Content-Type': 'application/json'
		}
	})
	.then(response => response.json())
	.then(data => {
		// Display mood graph
		graphDiv.innerHTML = '<img src="' + data.graphUrl + '">';

		// Display personalized suggestions
		suggestionsDiv.innerHTML = '<h2>Personalized Suggestions</h2><ul>';

		for (const suggestion of data.suggestions) {
			suggestionsDiv.innerHTML += '<li>' + suggestion + '</li>';
		}

		suggestionsDiv.innerHTML += '</ul>';
	})
	.catch(error => console.error(error));
});
