/* 
Created By: Kris Kuchinka
* Start Date: 2016.02.26
* Submission Date:
* Document Purpose: This is an external JavaScript file  
*   written for the "JavaPic" assignment at PDX Code Guild.
*/


function externalJs() {
	console.log("Your external JS is connected properly.");
} // End of start funtion

function disableBrowserValidation() {
	console.log("Browser validation disabled.");
	// Target the form by id and disable browser validation
	// Form validation is set automatically in HTML5, so 
	// the noValidate needs to be set to TRUE
	document.getElementById("signup").noValidate = true;
}

// create a function to keep form from submitting
function stopSubmit() {
	// Select the form by ID and add "listener" for the submit event
	// In the addEventListener function, feed it the variable submit to be listened for and an anonymous function
	document.getElementById("signup").addEventListener("submit", function(event) {
		// Pass the event from anonymous function and attach it to preventDefault function
		event.preventDefault()
		// Verify in the console that the submission didn't work
		console.log("Submission suppressed.");
	});
}

function checkName() {
	var name = document.forms["signup"]["name"].value;
	if (name == null || name == "") {
		stopSubmit();
		alert("You forgot your name!");
		return false;
	};
}

function checkUserName() {
	var user_name = document.forms["signup"]["username"].value;
	if (user_name == null || user_name == "") {
		alert("You didn't enter a username...");
		stopSubmit();
		return false;
	}
}

function checkEmail() {
	var email = document.forms["signup"]["email"].value;
	if (email == null || email == "") {
		alert("You didn't enter an email address");
		stopSubmit();
		return false;
	} else if (email != null && email =="") {
		alert("Hell yeah, you entered an email address!");
	}
}







externalJs();
disableBrowserValidation();
checkName();
checkUserName();
checkEmail()