def main():
	# Practice file for slicing strings

	string_1 = "This is the first string."
	string_2 = "This is the second string."
	string_3 = "This is the third string."

	# Make a string, print out it's 2nd character
	print(string_1[1])

	# Make a string, print out it's 3rd to last character
	print(string_2[-3])

	# Make a string, print out it's middle 3 characters as a substring
	# String is 24 characters long
	print(string_3[10:13])

	# Make a function that finds the middle 3 characters of any string using 
	# string function len()
	def middle_3(string):
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
		print(practice_string[28:31])

	# call function and feed it string parameter
	middle_3("practice_string")


main()