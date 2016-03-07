function externalJs() {
	console.log("Your external JS is connected properly.");
} // End of start funtion

function getNameFromUrl() {
	var name = window.location.search.substr(1).replace(/%20/g, " ");
	console.log(name);
	if (name) {
		document.getElementsByClassName("tagline")[0].innerHTML = "Let's develop something beautiful, " + name +"!";
	}
	
}



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
		imageElement.className = "image";
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

function makeLightBox(event) {
 	// Create element variable to select div id image_show
	var element = document.getElementById("image_show");
	// If target of the click event is an image
	if (event.target.nodeName == "IMG") {
		// Change the image class name to display_img
		// This will enlarge the image
		element.className = "display_img";
		// Make the source of the item that is targeted (clicked)
		// the source destination for the first child (which is 
		// an image) of the div named image_show
		// This will allow the actual picture that is clicked on to be shown
		element.firstChild.src = event.target.src
	} // End of if target == IMG

	// If something that is not an image is clicked
	if (event.target.nodeName != "IMG") {
		// Change the class name of the enlarged, selected 
		// picture to display none, which will put it back
		// to the small size inside the gallery
		element.className = "display_none";
	} // End of if target is NOT IMG
} // End of makeLightBox function

// Create a click event that triggers the makeLightBox function
document.addEventListener("click", makeLightBox);



externalJs();
getNameFromUrl();
displayImages();