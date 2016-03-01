function externalJs() {
	console.log("Your external JS is connected properly.");
} // End of start funtion

function displayImages() {
	var list_item = document.createElement("LI");
	var picture = document.createElement("IMG");
	picture.src = "images/pdxcg_01.jpg";
	for (var pic = 0; pic < picture.length; i++) {
		if (picture.length < 10) {
			picture.src = "images/pdxcg_0" + pic + ".jpg";
			pic++;	
		} else if (picture.length >= 10) {
			picture.src = "images/pdxcg_" + pic + ".jpg";
			pic++;
		};

	};
	list_item.appendChild(picture);
	document.getElementById("gallery").appendChild(list_item);
	console.log("Something.");
}

externalJs();

displayImages();