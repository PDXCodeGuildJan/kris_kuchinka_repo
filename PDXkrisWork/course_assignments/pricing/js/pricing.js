/* 
Created By: Kris Kuchinka
* Start Date: 2016.02.28(ish)
* Submission Date:
* Document Purpose: This is a JavaScript assignment that was assigned 
* at PDX Code Guild. We were given HTML and CSS to interact with, under
* the mandate that we can't alter the given HTML and CSS.
*/

//----------- Event Listeners ----------------------------------->
//################################################################
// Establish event listener for when user clicks an item
// Add the click event handler to the "add-item"
var addItemButton = document.getElementById("add-item");
// After clicking addItem, trigger addItem function
addItemButton.onclick = addItem;
// Add the click event handler to the "delete-item"
var deleteItemButton = document.getElementById("del-item");
// After clicking deleteItem, trigger deleteItem function
deleteItemButton.onclick = deleteItem;
// Add the click event handler to the "add-stock"
var addStockButton = document.getElementById("add-stock");
// After clicking addStock, trigger addStock function
addStockButton.onclick = addStock;
// Add the click even handler to the "remove-stock" button
var removeStockButton = document.getElementById("remove-stock");
// After clicking removeStock, trigger removeStock function
removeStockButton.onclick = removeStock;
//##############################################################

// Initialize array with the variable products
var products = [];

/* 
* Add the item in the text fields to the inventory list, which
* is in the table body (id="inventory")
*/
function addItem() {
	// Variable "materialName" is what user inputs in name field
	var materialName = document.getElementById("name").value;
	// Variable "price" is what user inputs in price field
	var price = document.getElementById("price").value;
	// Variable "inStock" is true or false based on checked status
	var inStock = document.getElementById("in-stock").checked
	// Create a new instance of the Product object with the 
	// new item's info
	var newProd = new Product(materialName, price, inStock);
	// Put the value of newProd into the products array
	products.push(newProd);
	// Call function displayInventory
	displayInventory();
} // end of function addItem


/*
* Delete the selected rows from the inventory
*/
function deleteItem() {
	// First, determine all the selected rows with helper function
	// getSelectedRowBoxes
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
