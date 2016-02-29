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
function acceptInfo(event) {
	event.preventDefault();
	if (checkName() == true && checkUserName() == true && checkEmail() == true) {
		window.location="gallery.html";		
	} else {
		// Verify in the console that the submission didn't work
		console.log("Submission suppressed.");
	} // End of if all are true		
} // End of stopSubmit

function checkName() {
	var name = document.forms["signup"]["name"].value;
	if (name == null || name == "") {
		alert("You forgot your name!");
		return false;
	}
	
	return true;
	
}

function checkUserName() {
	var user_name = document.forms["signup"]["username"].value;
	if (user_name == null || user_name == "") {
		alert("You didn't enter a username...");
		return false;
	} 
	return true;	
}

function checkEmail() {
	// Create variable for email by pulling value
	var email = document.forms["signup"]["email"].value;
	// Use RegExp that looks for no spaces, 1 @, proper period placement
	if ( /^[^\s@]+@[^\s\.@]+\.[^\s\.@]+$/.test(email)) {
		return true;
	} else {
		alert("You have entered an invalid email address.")
		return false;
	} // end of regex if 
} // End of checkEmail function

document.getElementById("submit").addEventListener("click", verifyAll);

function verifyAll(event) {
	acceptInfo(event);
}

function stupidTestFunction() {
	string = "kriskuchinka@gmail.com"
	given_email = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(string);
	return given_email;
}






externalJs();
disableBrowserValidation();
