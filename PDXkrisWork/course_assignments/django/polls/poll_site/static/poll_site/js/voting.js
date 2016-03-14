window.onload = function () {
	document.getElementById('question_vote').addEventListener('submit', votingSubmission);

}

function votingSubmission(event) {
	// Keep page from refreshing when button is clicked
	event.preventDefault();

	var form = document.getElementById("question_vote");
	// FormData is a built in function that crawls through a form and gets all its info
	var data = form.querySelector("[name='question_choice']:checked");

	var question_id = document.getElementById('question_id').value;

	console.log("Question ID: ", question_id, "Choice ID: ", data.value);

	// Build JS object, pass it to stringify function. Create dictionary object notation below.
	var jsonData = JSON.stringify({
		'question_id': question_id,
		'choice_id': data.value
	});
	// Verify that the proper data is displayed, according to selection
	console.log(jsonData);

	var csrfToken = form.querySelector("[name='csrfmiddlewaretoken']").value;

	var xhr = new XMLHttpRequest();
	// Set where the info is going and how it's being sent. True, because it asynchronous.
	xhr.open('POST', 'submit_vote', true)
	// When the call comes back, we want it to pass the data to votingSuccess function
	xhr.onload = votingSuccess;
	// Update the header
	xhr.setRequestHeader('X-CSRFToken', csrfToken);

	xhr.send(jsonData);

}

function votingSuccess(response) {
	if(response.target.status === 200) {
		// Get the data from the response
		var data_json = response.target.response;
		// Translate the data from json
		var data = JSON.parse(data_json);
		console.log(data); 
		//Post the voting results!!
		postResults(data.data)
	}
}

function postResults(data) {
	// Get the div and clear out the form
	var divThing = document.getElementById("questions");
	divThing.innerHTML = "";

	// Rebuild the form with voting results
	var h3 = document.createElement('H3');
	h3.textContent = "Current Results!";

	var list = document.createElement('UL');
	list.id = 'results';

	// Loop through the returned results and display them
	for (var i = 0; i < data.length; i++) {
		var choice = "'" + data[i].text + "' has " + data[i].votes + " votes"; 
		var item = document.createElement('LI');
		item.textContent = choice;
		list.appendChild(item);
	};

	divThing.appendChild(h3);
	divThing.appendChild(list);
}