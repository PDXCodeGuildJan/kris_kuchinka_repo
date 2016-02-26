function start() {
	console.log("Your external JS is connected properly.");
} // end of start funtion

function changeImage() {
	var changing_image = document.getElementById("jumbotron");
	console.log(changing_image);

	changing_image.style.backgroundImage = "url('images/pdxcg_" + image_number + ".jpg')";
	
	if (image_number <= 9) {
		changing_image = "url('images/pdxcg_0" + image_number + ".jpg')";
	} else {
		changing_image = "url('images/pdxcg_" + image_number + ".jpg'";
	};
	
	image_number += 1;

} // end of changeImage function
start();
// create global variable for image_number 
var image_number = 1;
window.onclick = changeImage;

