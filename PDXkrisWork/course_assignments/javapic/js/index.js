function externalJs() {
	console.log("Your external JS is connected properly.");
} // End of start funtion

// Create function that changes images every 10 seconds.
// There are 59 images to cycle through (#42 is missing)
function changeImage() {
	// Set variable changing_image to id; grab a hold of it
	var changing_image = document.getElementById("jumbotron");
	// The numbers are written with a 0 before single digit // numbers. To avert this the first step is for images  // 1-9 to add an exra zero to the file path.	
	if (image_number <= 9) {
		// Change the styling of the variables background // image
		changing_image.style.backgroundImage = "url('images/pdxcg_0" + image_number + ".jpg')";
		// Increment image number
		image_number += 1; 
		// Let the console know where you are "located" in 
		// if statement
		console.log("You are <= 9");
	// If the image_number is 10 or greater....
	} else if (image_number >= 10 && image_number <= 60) {
		// Let the console know where you are "located" in 
		// if statement		
		console.log("You are now >= 10");
		// Image number 42 is missing from folder--> skip it
		if (image_number == 42) {
			image_number = 43;
		}; // End of if image_number is 42
		// Change background image, in this set no need to // add a zero.
		changing_image.style.backgroundImage = "url('images/pdxcg_" + image_number + ".jpg')";
		image_number += 1;
	// If the number is greater than 60
	} else if (image_number >= 61) {
		image_number = 1;
	}; // End of if, else if, else if statement block
} // End of changeImage function
externalJs();
// Create global variable for "image_number" 
var image_number = 1;
// Set a 10 second interval to change the picture
window.setInterval(changeImage, 10000);

