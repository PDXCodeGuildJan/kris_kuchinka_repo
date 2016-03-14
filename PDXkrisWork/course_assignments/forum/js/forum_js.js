/*
* Created By: Kris Kuchinka
* Submission Date: 2016.03.14
* Project Name: Forum
*
* Explanation: This was a project assigned to me at PDX Code Guild by the instructor. It is * supposed to be a single page forum that uses AJAX to automatically sync up with the Google * spreadsheet it is attached to. (Refer to README.md for assignment particulars.) The style * theme was supposed to be modeled after a Star Wars promotional picture.
*
* This external JS file is linked to forum_index.html.
* A jQuery CDN is being used via Google.
*/

$(document).ready(function() {
	// Once the document has loaded, call the receive Data function to display the posts that are already loaded into the forum
	receiveData();

	// When the submit button is clicked (this assumes that the user has filled out the post)
	$("#submit-form").click(function(event) {
		// Keep the page from doing its default function which would lead away from forum page
		event.preventDefault();
		// Get the value of the post title and assign it a variable. Uses a jQuery selector.
		title = $("#subject").val();
		// Get the value of the actual comment in the forum and apply it to a variable.
		bodyText = $("#comment").val();
		// Use console.log to show developer that the click function is working and getting the proper values attributed to the created variables
		console.log(title, bodyText);
		// Pass the information from both fields to the postData function which adds to the ongoing forum discussion
		postData(title, bodyText);
	}); // end of click function 
}); // end of ready


//-------------------------> Begin function creation

// This function takes two parameters (variables assigned based on click function) and posts the information to the ongoing list that is the forum
function postData(title, bodyText) {
	// create a variable for the url
	url = 'https://docs.google.com/forms/d/1W1jO8DwInFuzlabeYqEp6hUUUqDbR8gESs1Pk6qozOc/formResponse';
	// begin jQuery AJAX call
	$.ajax({
		// User will be filling in form title and content and posting to the spreadsheet
		type: 'POST',
		// Refer to url above
		url: url,
		// Specs in README.md detailed the need for which types of data and what data to use with the call
		dataType: 'xml',
		data: {"entry_1639809944": title, "entry_1402022725": bodyText},
		// If the AJAX call works, feed the result into the div for post success notices. This is an empty div until the content is fed to it.
		success: function(result) {
			$("#successful-post").html(result);
			// Make sure post is showing as successful in the console for development purposes.
			console.log("You successfully posted your post.");
		},
		// If the AJAX call results in an error....
		error: function(result) {
			// If the AJAX call does not work, feed the result into the div for notice of failure. This is an empty div until the content is fed to it.
			$("#successful-post").html(result);
			// Let the developer know there is an error
			console.log("You got an error!");
			// Reload the page so that it doesn't divert away. This is supposed to be a single page forum that feeds into itself.
			location.reload();
		}
	}) // end of ajax call
}

// This function receives the data from the existing spreadsheet and builds it into the HTML without leaving the forum page.
function receiveData() {
	// Assign variable to url address where we are receiving our data from.
	getUrl = 'https://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script'
	// Begin AJAX jQuery call to get the forum content from Google spreadsheet.
	$.ajax({
		// Type, url and dataType where described in the README.md doc
		type: 'GET',
		url: getUrl,
		dataType: 'jsonp',
		// Upon a successful AJAX scenario...
		success: function(result) {
			// Loop through the results received from the Google spreadsheets
			for (var i = 0; i < result.feed.entry.length; i++) {
				// Have the console log display data that is being received for the developer
				console.log(result.feed.entry[i].gsx$title.$t);
				console.log(result.feed.entry[i].gsx$post.$t);
				console.log(result.feed.entry[i].gsx$timestamp.$t);
				// Create a DIV element to insert into the pages HTML
				container = document.createElement("DIV");
				// GIve the div that was just created a class to aid in CSS design
				container.className = "message";
				// Create a H1 element to hold the title of the current post that is being displayed into the container div (remember, this is a loop. There are multiple posts to loop through...)
				title = document.createElement("H1");
				// Insert the results into the newly created title variable
				title.textContent = result.feed.entry[i].gsx$title.$t;
				// Create a paragraph element to give the current post a place in the DOM
				post = document.createElement("P");
				// Insert the results into the post area of the forum
				post.textContent = result.feed.entry[i].gsx$post.$t;
				// Create a paragraph element to show a timestamp
				timestamp = document.createElement("P");
				// Grab the timestamp results and insert it into newly created "p-tag"
				timestamp.textContent = result.feed.entry[i].gsx$timestamp.$t;
				// Take the title, post and timestamp values and insert them into the container div that was created at the beginning of the loop
				container.appendChild(title);
				container.appendChild(post);
				container.appendChild(timestamp);
				// Insert the elements and values of the newly created (or re-created) container div into the empty div "returned-posts" so that the newly retrieved data is displayed in the forum below and the loop can move to the next post
				$("#returned-posts").append(container);
			}
		}, // end of success
		// Let the developer know if there is an error....
		error: function(result) {
			console.log("Fail!");
		}
	}) // end of ajax get
} // end receiveData


