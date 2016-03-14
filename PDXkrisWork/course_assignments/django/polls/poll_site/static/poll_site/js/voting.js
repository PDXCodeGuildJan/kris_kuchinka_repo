window.onload = function () {
	document.getElementById('question_vote').addEventListener('submit', votingSubmission);

}

function votingSubmission(event) {
	// Keep page from refreshing when button is clicked
	event.preventDefault();

	var form = document.getElementById("question_vote");
	// FormData is a built in function that crawls through a form and gets all its info
	var data = form.querySelector("[name='question_choice']:checked");

	var question_id = form.getElementById('question_id').value;

}