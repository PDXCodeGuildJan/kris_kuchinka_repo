# Created by: Kris Kuchinka
# Date Created: 2015.01.11
# PDX Code Guild Lecture Practice
# Practice file for slicing strings, looping through a sequence, etc

def main():

	user_input = input("Please tell me what's on your mind.   ")

	# make a list of random stuff and call loop function with looping function
	animals = ["dog", "cat", "turtle", "frog", "fish", "snake", "duck", "goat", "chicken"]

	fun_with_strings()
	# call functions from below and feed it string parameter
	hard_code_middle_3(user_input)
	dynamic_middle_3(user_input)
	super_dynamic_middle_3(user_input)
	looping_thru_sequence(user_input)
	# loop through "animals" list from above
	looping_thru_sequence(animals)


#--------------------- various string manipulations function ----------------
def fun_with_strings():
		# create string variables
		string_1 = "This is the first string."
		string_2 = "This is the second string."
		string_3 = "This is the third string."

		# Make a string, print out it's 2nd character
		print(" ")
		print(" ")
		print("This is how to print out the second character of a string variable.")
		print(string_1[1])
		print(" ")

		# Make a string, print out it's 3rd to last character
		print("This prints out the 3rd to last character of a string.")
		print(string_2[-3])
		print(" ")

		# Make a string, print out it's middle 3 characters as a substring
		# String is 24 characters long
		print("These are the middle 3 characters of a 24 character string:")
		print(string_3[10:13])
		print(" ")

#-------------------- hardcoded function ----------------------

# Make a function that finds the middle 3 characters of any string using 
# string function len()
# This is a hardcoded way of accomplishing that goal
def hard_code_middle_3(string):
	# assign string to variable
	practice_string = "This is the greatest and best practice string in the world."

	# get length of practice_string
	# ------------------------------
	# practice_string_length = len(practice_string)
	# print(practice_string_length)
	# ------------------------------
	# result = 59

	# divide string by 2 using integer division method
	# ------------------------------
	# calculated_string = (practice_string_length//2)
	# print(calculated_string)
	# ------------------------------
	# result 29

	# show middle 3 string characters, based upon math above
	print("This is a middle 3 of a string, done by hardcoding.")
	print(practice_string[28:31])
	print(" ")

#---------------------- dynamic function 1 --------------------------

# define the different functions
# another way to find the middle 3 characters of a string
def super_dynamic_middle_3(string):
	mid = (len(string)-3)//2
	print("This is another set of middle 3 letters from a different dynamic function that takes a string.")
	print(string[mid:mid+3])
	print(" ")

#--------------------- dynamic function 2 ----------------------------

# need a function that can take the middle 3 of ANY string upon being 
# fed into the function parameters
def dynamic_middle_3(string):
	# need to find the middle of the string
	middle = len(string)//2
	print("This is a set of the middle 3 letters of a string found using a dynamic function that can accept a string as a parameter.")
	print(string[middle-1:middle+2])
	print(" ")

#----------------- looping through sequence functions ---------------

# write a function that:
# -->expects an input of a sequence
# -->prints the sequence
# -->loops through the sequence and prints each element

def looping_thru_sequence(sequence):

	print(sequence)

	for x in sequence:
		print(x)
	
	print(" ")

# call main function to initialize program
main()