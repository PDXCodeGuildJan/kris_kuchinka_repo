// Establish even listener for when they click an item
// Add the click event handler to the "add-item"
var addItemButton = document.getElementById("add-item");
addItemButton.onclick = addItem;
// Add the click event handler to the "delete-item"
var deleteItemButton = document.getElementById("del-item");
deleteItemButton.onclick = deleteItem;
// Add the click event handler to the "add-stock"
var addStockButton = document.getElementById("add-stock");
addStockButton.onclick = addStock;
// Add the click even handler to the "remove-stock" button
var removeStockButton = document.getElementById("remove-stock");
removeStockButton.onclick = removeStock;


window.onload = loadDataWithAJAX;
// Initialize array with the variable products

var products = [];

/* Add the item in the text fields to the inventory
 * list, which is in the table body (id="inventory")
 */
function addItem() {
	// Set variable "materialName" to value of anything with id 'name'
	var materialName = document.getElementById("name").value;
	// Set variable "price" to value of anything with id 'price'
	var price = document.getElementById("price").value;
	// Set variable inStock to anything with id 'in-stock' that is checked
	var inStock = document.getElementById("in-stock").checked;
	// Create a new instance of the Product     // object with the new item's info
	var newProd = new Product(materialName, price, inStock);

	products.push(newProd);

	displayInventory();

	saveData();
} // end of function addItem


//}  end of function thing

/*
* Delete the selected rows from the inventory
*/
function deleteItem() {
	// First, determine all the selected rows
	var selected = getSelectedRowBoxes();
	// Delete the Product objects that correspond to those 
	// rows from the Products array
	for (var i = selected.length-1; i >= 0;  i--) {
		// Get the id on the row that the checkbox is in
		var prodId = selected[i].parentNode.parentNode.id;
		// Delete product object that is stored at index
		delete products[prodId];
		products.splice(prodId, 1);
	};

	// Rerender HTML list, using displayInventory
	displayInventory();
	saveData();
}
/*
* Helper function to get all the checked boxes in the HTML
* inventory.
*/
function getSelectedRowBoxes() {
	var selected = document.querySelectorAll("td>input.selector[type=checkbox]:checked");
	return selected;
}

/*Adds all the items in the products array to the HTML.*/
function displayInventory() {
	var inventory = document.getElementById("inventory");

	// Get rid of all existing children of the table
	inventory.innerHTML = "";

	// Loop through the products array, adding each Product
	// to the inventory table in the HTML.
	for (var i = 0; i < products.length; i++) {
		// Make a new row for the Product i
		var newRow = document.createElement("TR");
		newRow.id = i;

		// Make a TD for the checkbox
		var checkbox = document.createElement("TD");
		// Make the actual checkbox
		var innerCheckbox = document.createElement("INPUT");
		// Set the input type to checkbox
		innerCheckbox.type = "checkbox";
		innerCheckbox.className = "selector";
		// Add the inerCheckbox value to the checkbox TD
		checkbox.appendChild(innerCheckbox);


		// Make a TD for the material name
		var materialName = document.createElement("TD");
		materialName.textContent = products[i].prodName;

		// Make a TD for the price
		var price = document.createElement("TD");
		price.textContent = products[i].price;

		// Make a TD for the stock toggle
		var inStock = document.createElement("TD");
		// Set the TD's text content to either yes or no
		// based on the product at index i's inStock property
		inStock.textContent = (function(inStock) {
			if (inStock) {
				return "Yes";
			}
			return "No";
		}(products[i].inStock));
		// Set the class name on the TD
		inStock.className = products[i].inStock;

		//Add all the TD's to the TR
		newRow.appendChild(checkbox);
		newRow.appendChild(materialName);
		newRow.appendChild(price);
		newRow.appendChild(inStock);

		// Add the new row to the actual TBODY in the hmtl
		inventory.appendChild(newRow);

	};

}

/*
* Toggles the inStock status on the selected rows inside of * inventory
*/
function addStock() {
	// Use helper function to get all checked boxes
	var checked = getSelectedRowBoxes();

	// Loop through checked variable to 
	for (var temp = 0; temp < checked.length; temp++) {
		var status = checked[temp].parentNode.parentNode.lastChild;
		console.log(status);
		status.textContent = "Yes"; 
		status.className = "true";
		checked_choice = checked[temp];
		checked_choice.checked = false;

	// Update the Product in the products array that
	// corresponds to the checked checkbox we're updating
	var prodId = checked[temp].parentNode.parentNode.id;
	products[prodId].instock = true;
	}

	saveData();
} // end of function addStock


function removeStock() {

	var selected =  getSelectedRowBoxes();

	for (var temp = 0; temp < selected.length; temp++) {
		var status = selected[temp].parentNode.parentNode.children[3];
		status.textContent = "No";
		status.className = "false";
		checked_choice = selected[temp];
		checked_choice.checked = false;
	var prodId = selected[temp].parentNode.parentNode.id;
	products[prodId].instock = false;
	};

	saveData();
}

/* Constructor for the Product object */
function Product(name, price, inStock) {
	this.prodName = name;
	this.price = price;
	this.inStock = inStock;

	this.setStock = function(stock) {
		this.inStock = stock;
	}
} 

/**
* Saves current state of the products list array.
**/
function saveData() {
	// Transform the products array into a JSON string
	var productJSON = JSON.stringify(products);

	// Save the JSON string to local storage
	localStorage.setItem("price_list", productJSON);
}

/**
* Loads the current state of the products array
**/
function loadData() {
	var productJSON = localStorage.getItem("price_list");
	console.log("Loaded data", productJSON);

	// Parse it into a Javascript data type and
	// save the global array
	products = JSON.parse(productJSON);
	console.log(products);

	// Double check that products is set a list if null
	if (!products) {
		products = [];
	}

	//Update the rendered display
	displayInventory();
}

/*
* Load the data from the json file on the server with AJAX
*/
function loadDataWithAJAX() {
	// Create a new XMLHTTPRequest object
	var request = new XMLHttpRequest();
	// Add the call info
	request.open('GET', 'data.json', true);
	// Setup the onload function
	request.onload = function () {
		// Make sure that everything is good
		if (request.status === 200) {
			// responseText holds the data we get back from the server
			var prodJSON = request.responseText;
			products = JSON.parse(prodJSON);
			displayInventory();
		}
	}

	// Actually send out the request! This is the last thing you do
	// before you send the call
	request.send();
}






