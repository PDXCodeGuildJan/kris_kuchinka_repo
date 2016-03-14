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

function votingSuccess(data) {
	console.log("Congratulations! You rocked the vote.");
}