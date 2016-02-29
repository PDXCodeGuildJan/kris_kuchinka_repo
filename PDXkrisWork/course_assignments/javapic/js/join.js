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
	if (checkName() == true && checkUserName() == true && checkEmail() == true) {
	
		
		
		
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
		// stopSubmit();
		return false;
	} else {
		return true;
	}
}

function checkEmail() {
	var email = document.forms["signup"]["email"].value;
	console.log(email);
	if (email == null || email == "") {
		alert("You didn't enter an email address");

		return false;
	// } else if (email != null && email != "") {
		// alert("Hell yeah, you entered an email address!");
		// getEmail = document.getElementById("email");
		// atSymbol = getEmail.indexOf("@");
		// dotNotation = 
	} else {
		return true;
	}
}

document.getElementById("submit").onclick = verifyAll;

function verifyAll() {
	stopSubmit();
	// checkName();
	// checkUserName();
	// checkEmail();
}







externalJs();
disableBrowserValidation();
