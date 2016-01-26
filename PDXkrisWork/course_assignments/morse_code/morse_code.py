"""
A morse code translator that takes user input and translates it to either 
English or morse code.
"""

__author__ = "Katie Dover", "Kris Kuchinka"

# import Regex functionality
import re
# Import morse code dictionary from morse.py
from morse import morse

def main():
	"""Determine whether we're translating Morse Code into English or
	English into Morse Code"""
	print("-------------------------------------------------")
	print("Welcome to the Morse Code intpreter!")
	print("-------------------------------------------------")
	# Prompt user for input, either Morse or English, but user can quit
	prompt = input("Would you like to translate (E)nglish or (M)orse Code? (Q)uit at any time. > ")

	# Take the E prompt regardless of case sensitivity
	if prompt.upper() == "E":
		print("-------------------------------------------------")
		message = input("What would you like translated? > ")
		file_name = input("Please type in the filename and extension you would like to create. >")
		# Call write_code function with user input and file name
		write_code(message.upper(), file_name)
		# Tell the user their file has been created.
		print("-------------------------------------------------")
		print("Your file has been created.")
		print("-------------------------------------------------")


	# take the M prompt regardless of case sensitivity
	elif prompt.upper() == "M":
		print("-------------------------------------------------")
		file_name = input("Please enter the file name that you would like to translate from Morse Code to English: > ")

		# call function that changes Morse Code into English (below)
		# carries user input to function and applies case sensitivity exception to variable
		complete_sentence = read_code(file_name)
		# Print the decoded message
		print("-------------------------------------------------")
		print("Your decoded message: " + complete_sentence)
		print("-------------------------------------------------")

		# handles quit function with goodbye and case sensitivity 
	elif prompt.upper() == "Q":
		print("-------------------------------------------------")
		print("\t\t Goodbye!")
		print("-------------------------------------------------")
		exit()
		# if input is not recognized, send user message below and return to main
	else:
		print("-------------------------------------------------")
		print("I'm sorry, please choose a valid option.")
		print("-------------------------------------------------")


def read_code(file_name):
	"""Take Morse Code message and turn it into English
	"""
	# Get the morse code from a preexisting file
	load_file = open(file_name, "r")
	# Get the morse sentence out of the file
	morse_message = load_file.read()
	load_file.close()

	# Initialize the english sentence
	complete_sentence = ""
	
	# Split the morse into words depending
	# 	on how many spaces each value has between the next value (7 is the key)
	regex = "\s{7}"
	# Split the sentence into a list of words
	list_of_words = re.split(regex, morse_message)

	# Loop through each word
	for each_word in list_of_words:

		#print("This is a word:", each_word)

		# Split the morse words into lists of morse letters.
		regex = "\s{3}"
		list_of_letters = re.split(regex, each_word)

		# Loop through the morse letters
		for each_letter in list_of_letters:
			#print("This is the letters in the word:", each_letter)

			# Once all values have been grouped appropriately
			# 	Translate the values into their english counterparts
			for character, code in morse.items():
				if code == each_letter:
					complete_sentence += character
					#print("This is the letter in english:", character)

		# Add a space between the words
		complete_sentence += " "

	# Return the translated message
	return complete_sentence
	

def write_code(message, file_name):
	"""Takes an English message and turn it into Morse Code. Put it into a file with the given name."""

	
	# Initialize variable current_sentence to be an empty string
	current_sentence = ""
	# Initialize variable current_character to be an empty string
	current_character = ""
	# Loop through each character given in english message
	for character in message:
		# If any character is a space
		if character == " ":
			# Add seven spaces between each word
			# (Morse Code formatting requires seven spaces between each word)
			current_sentence += (" " * 7)

		# If the characters are in the dictionary morse
		elif character in morse: 
			# Give vaule to letter variable with case sensitivity
			letter = morse[character.upper()]
			# Concatenate current_sentence with new letters with three spaces in between each letter
			# (Morse Code formatting requires three spaces between each letter)
			current_sentence += letter + (" " * 3) 
	# Print completed sentence
	# Establish a variable to load file
	load_file = open(file_name, "w")
	load_file.write(current_sentence)
	load_file.close()


# Initiates program
if __name__ == '__main__':
	main()