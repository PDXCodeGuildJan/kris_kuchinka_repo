function externalJs() {
	console.log("Your external JS is connected properly.");
} // End of start funtion

function displayImages() {
	// Grab gallery section
	var gallery = document.getElementById("gallery");
	// Create unordered list element
	var unorderedElement = document.createElement("UL");
	// loop through pic numbers to add to image elements
	for (var pic = 1; pic <= 60; pic++) {
		// Create list item element
		var listElement = document.createElement("LI");
		// Create img item element
		var imageElement = document.createElement("IMG");
		if (pic < 10) {
			// Give the image taga a source and insert current pic number to loop through
			imageElement.src = "images/pdxcg_0" + pic + ".jpg";
		} else if (pic == 42) {
			continue;
		} else if (pic >= 10) {
			// Give the image taga a source and insert current pic number to loop through		
			imageElement.src = "images/pdxcg_" + pic + ".jpg";
		};
		// make the imageElement a child of the listItem
		listElement.appendChild(imageElement);
		// Make the listElement a child of the unorderedElement
		unorderedElement.appendChild(listElement);
	};
	// Put the whole unordered list that has been created // into the gallery
	gallery.appendChild(unorderedElement);
} // end of displayImages function


externalJs();

displayImages();