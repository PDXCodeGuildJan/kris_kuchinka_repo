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
	# Ask the user how many dice to roll
	total_rolls = int(input("How many dice rolls? "))
	# cast data object into another data object
	#total_rolls=int(total_rolls)

	# Ask the user how big the dice is
	die_size = int(input("How many sides does the die have? "))

	# need a for loop to know how many times to roll the die
	# start range at 0, due to zero-index counting system
	for x in range(0,total_rolls):
		# Roll that many dice, using the custom_die function from above
		custom_die(1, die_size)

# call function
main()


