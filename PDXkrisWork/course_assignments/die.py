# Create a die function that returns a random number, 
# as if the user rolled a die.

# important random function from Python3 file
from random import randint

def die():
	roll = randint(1, 6)
	print(roll)

# call function when desired

#--------------------------------------------->

# Make a function called custom_die that takes a range for 
# and returns a random number in that range

# import randint
from random import randint

# make the function accept two inputs
def custom_die(number_1, number_2):
	# make sure to have the two inputs in the randint() function
	roll = randint(number_1, number_2)
	print(roll)

# define the range of numbers to find a number when function is called

#---------------------------------------------->

# Create a "role-playing" die program with the following specs

# 2 pieces of info needed to know:
#		1. How big is the die
#		2. How many dice are there

# best practice is to define the main function that kicks off the program
def main():
	# modify our main function so that it will continue asking us to
	# roll dice, until we exit the program
	# Wrap the core logic of the function that takes a range and print
	# from a random number in that range
	
	# let user know that they can put in 'q' to stop program
	print("Welcome to the dice roller. Enter 'q' to exit.")

	# initialize "entry" variable by giving it an empty string
	entry = ""

	# make a while loop that checks to see wether or not the user has entered 'q'
	while entry != "q":

		# Ask the user how many dice to roll
		# Assign "entry" variable to the input value
		entry = input("How many dice rolls? ")
		# if input is not "q".....
		if entry != "q":
			# assign "total_rolls" variable to variable "entry" input 
			# make the variable an integer upon assignment
			total_rolls = int(entry) 
		# Make sure that the program quits when "q" is entered
		if entry == "q":
			print("Thanks for playing. Have a nice day.")
			exit()

		# Find out how many sides the die has
		# Assign "entry" variable to the input value
		entry = input("How many sides does the die have? ")
		# if input is not "q".....
		if entry != "q":
			# assign "die_size" variable to variable "entry" input
			# make the variable an integer upon assignment
			die_size = int(entry)
		# Make sure that the program quits when "q" is entered
		if entry == "q":
			print("Thanks for playing. Have a nice day.")
			exit() 

		# need a for loop to know how many times to roll the die
		# start range at 0, due to zero-index counting system
		for x in range(0,total_rolls):
			# Roll that many dice, using the custom_die function from above
			custom_die(1, die_size)

# call function
main()


