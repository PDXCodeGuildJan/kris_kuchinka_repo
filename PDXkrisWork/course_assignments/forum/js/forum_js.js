/*
* Created By: Kris Kuchinka
* Conception Date: 2016.03.05
* Last Modified: 2016.03.07
*
* Purpose: This is the final JavaScript/AJAX assignment at  * PDX Code Guild. The instructions for it are in the readme.* md file in the forum folder. 
*
* This external JS file is linked to forum_index.html.
* A jQuery CDN is being used via Google.
*/

// ==================================================
// Create an XMLHttpRequest object to make a call to the Google Sheets database
// var xhr = new XMLHttpRequest();
// xhr.open('GET', 'https://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script', true);
// xhr.send();
// ==================================================

$(document).ready(function() {
	receiveData();

	$("#submit-form").click(function(event) {
		event.preventDefault();
		title = $("#subject").val();
		bodyText = $("#comment").val();
		console.log(title, bodyText);
		postData(title, bodyText);

		

	}); // end of click function 
}); // end of ready


function postData(title, bodyText) {
	url = 'https://docs.google.com/forms/d/1W1jO8DwInFuzlabeYqEp6hUUUqDbR8gESs1Pk6qozOc/formResponse';

	$.ajax({
		type: 'POST',
		url: url,
		dataType: 'xml',
		data: {"entry_1639809944": title, "entry_1402022725": bodyText},
		success: function(result) {
			$("#successful-post").html(result);
			console.log("You successfully posted your post.");
		},
		error: function(result) {
			$("#successful-post").html(result);
			console.log("You got an error!");
			location.reload();
		}
	}) // end of ajax call
}

function receiveData() {
	getUrl = 'https://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script'

	$.ajax({
		type: 'GET',
		url: getUrl,
		dataType: 'jsonp',
		success: function(result) {
			for (var i = 0; i < result.feed.entry.length; i++) {
				console.log(result.feed.entry[i].gsx$title.$t);
				console.log(result.feed.entry[i].gsx$post.$t);
				console.log(result.feed.entry[i].gsx$timestamp.$t);
				container = document.createElement("DIV");
				container.className = "message";
				title = document.createElement("H1");
				title.textContent = result.feed.entry[i].gsx$title.$t;
				post = document.createElement("P");
				post.textContent = result.feed.entry[i].gsx$post.$t;
				timestamp = document.createElement("P");
				timestamp.textContent = result.feed.entry[i].gsx$timestamp.$t;
				container.appendChild(title);
				container.appendChild(post);
				container.appendChild(timestamp);
				$("#returned-posts").append(container);
			}
		}, // end of success
		error: function(result) {
			console.log("Fail!");
		}
	}) // end of ajax get
} // end receiveData


