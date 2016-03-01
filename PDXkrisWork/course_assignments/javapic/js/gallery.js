function externalJs() {
	console.log("Your external JS is connected properly.");
} // End of start funtion

function displayImages() {
	var list_item = document.createElement("LI");
	var picture = document.createElement("IMG");
	picture.src = "images/pdxcg_01.jpg";
	list_item.appendChild(picture);
	document.getElementById("gallery").appendChild(list_item);
	console.log("Something.");
}

externalJs();

displayImages();