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
	$("#submit-form").click(function() {
		$.ajax({url: "https://docs.google.com/forms/d/1W1jO8DwInFuzlabeYqEp6hUUUqDbR8gESs1Pk6qozOc/formResponse",
		async: true,
		success: function(result) {
			$("#successful-post").html(result);
			console.log("You successfully posted your post.");
		}});
	});
});