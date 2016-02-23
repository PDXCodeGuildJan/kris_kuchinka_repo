
// Number of times we're going to loop
var number = 5;

var counter = document.getElementById("counter")

var inputField = document.getElementById("num-loops");

var die1 = "<img src='dice/1.png'>"

function die() {
	// Round down (floor) the random number that is multipled by six (number of die sides)
	// Add 1 to random number, ensuring you will not get 0
	dieNumber = Math.floor((Math.random() * 6) + 1);
	// Give us the number to use
	return dieNumber;
}

function loopClick() {
	number = inputField.value;
	counter.innerHTML = "";

	for (var i = 0; i < number; i++) {	
		counter.innerHTML += "<img src='dice/" + die() + ".png'>" + "<br/>";
	};
};


// Add click listener
document.getElementById("loop-btn").onclick = loopClick;




