// Establish even listener for when they click an item
// Add the click event handler to the "add-item"
var addItemButton = document.getElementById("add-item");
addItemButton.onclick = addItem;
// Add the click event handler to the "add-stock"
var addStockButton = document.getElementById("add-stock");
addStockButton.onclick = addStock;
// Add the click even handler to the "remove-stock" button
var removeStockButton = document.getElementById("remove-stock");
removeStockButton.onclick = removeStock;

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
	// if the inStock(checked) item is true
	if (inStock == true) {
		// set variable below to yes and it will be used as flag for list
		inStockConfirm = "Yes";
	// else if something is not checked
	} else if (inStock == false) {
		// set variable below to no and it will be used as a flag for list
		inStockConfirm = "No";
	}	
	
	var inventory = document.getElementById("inventory");
	var newRow = "<tr> <td><input type=\"checkbox\" class=\"selector\" /></td> <td>" + materialName + "</td> <td>" + price + "</td> <td class=" + inStock + ">" + inStockConfirm + "</td></tr>";

	inventory.innerHTML += newRow;
} // end of function thing


//----> Toggles the inStock status on the selected rows inside of inventory
function addStock() {
	// CANNOT USE querySelectorAll

	var selection = document.getElementsByClassName("selector");
	// test that selection has a handle on all nodes with class "selector"
	// console.log("This should be all the nodes:", selection);
	// create a variable named check to hold a list of the checked items
	checked = [];
	for (temp = 0; temp<selection.length; temp++) {
		// inside the loop, if it is checked, set value to true
		if (selection[temp].checked == true) {
			// if condition above is satisfied, add current selection to 
			// checked list
			checked.push(selection[temp]);
		} // end of if
	} // end of for loop
	// print to console the list of checked items
	// console.log(checked);

	for (var temp = 0; temp < checked.length; temp++) {
		var status = checked[temp].parentNode.parentNode.lastChild;
		console.log(status);
		status.textContent = "Yes"; 
		status.className = "true";
		checked_choice = checked[temp];
		checked_choice.checked = false;
	}
} // end of function addStock


function removeStock() {
	// Tiffany Mandate ---> use 'querySelectorAll'
	var selected = document.querySelectorAll("td>input.selector[type=checkbox]:checked");
	console.log("This is supposed to print checked boxes-->", selected)

	for (var temp = 0; temp < selected.length; temp++) {
		var status = selected[temp].parentNode.parentNode.children[3];
		status.textContent = "No";
		status.className = "false";
		checked_choice = selected[temp];
		checked_choice.checked = false;
	}
}
