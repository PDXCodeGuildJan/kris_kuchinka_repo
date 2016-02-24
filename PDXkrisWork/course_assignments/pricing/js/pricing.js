// Establish even listener for when they click an item
// Add the click event handler to the "add-item"
var addItemButton = document.getElementById("add-item");
addItemButton.onclick = addItem;

var addStockButton = document.getElementById("add-stock");
addStockButton.onclick = addStock;

/* Add the item in the text fields to the inventory
 * list, which is in the table body (id="inventory")
 */
function addItem() {
	var materialName = document.getElementById("name").value;
	var price = document.getElementById("price").value;
	var inStock = document.getElementById("in-stock").checked;
	if (inStock == true) {
		inStockConfirm = "Yes";
	} else if (inStock == false) {
		inStockConfirm = "No";
	}	
	
	var inventory = document.getElementById("inventory");
	var newRow = "<tr> <td><input type=\"checkbox\" class=\"selector\" /></td> <td>" + materialName + "</td> <td>" + price + "</td> <td class=" + inStock + ">" + inStockConfirm + "</td> </tr>";

	inventory.innerHTML += newRow;
} // end of function thing


//----> Toggles the inStock status on the selected rows inside of inventory
function addStock() {
	// CANNOT USE querySelectorAll
	console.log("You clicked add stock button.");
	var checked_selection = document.getElementsByClassName("selector");
	console.log(checked_selection);
	var inStock = document.getElementById("in-stock").checked;
	console.log(inStock);
	console.log(inStockConfirm);
	// var inStock = document.getElementById("in-stock").checked;
	// if (checked_selection == true) {
	// 	inStockConfirm = "Yes";
	// } else if (inStock == false) {
	// 	inStockConfirm = "No";
	// }
	for (temp = 0; temp<checked_selection.length; temp++) {
		if (checked_selection[temp].checked == true) {
			console.log("This is checked.");
			inStock == true;
			return inStock;
			// console.log(checked_selection[temp])
			// thsi will select alll of th checked elements
			// find the parents of these elements
			// find the instock children of these parents 


		} else {
			console.log("This is not checked.");
		}
	}


	// Find all the selected things

	// Change the inStock value of selected things



}

function removeStock() {
	// USE querySelectorAll

}
