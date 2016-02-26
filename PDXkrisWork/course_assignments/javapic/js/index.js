function start() {
	console.log("Your external JS is connected properly.");
} // end of start funtion

function changeImage() {
	var changing_image = document.getElementById("jumbotron");
	console.log(changing_image);
	
	if (image_number <= 9) {
		changing_image.style.backgroundImage = "url('images/pdxcg_0" + image_number + ".jpg')";
		image_number += 1; 
		console.log("You are <= 9");
	} else if (image_number >= 10 && image_number <= 60) {
		console.log("You are now >= 10");
		changing_image.style.backgroundImage = "url('images/pdxcg_" + image_number + ".jpg')";
		image_number += 1;
	} else if (image_number >= 61) {
		// console.log("You are greater than pic 60.");
		image_number = 1;
		// changing_image.style.backgroundImage = "url('images/pdxcg_0" + image_number + ".jpg')";
	};
	
	

} // end of changeImage function
start();
// create global variable for image_number 
var image_number = 1;
window.onclick = changeImage;

