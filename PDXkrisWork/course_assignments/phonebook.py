"""Implements a very simple Phonebook using a Dictionary."""

__author__ = "Kris Kuchinka"
# Creation Date: 2015.01.21
# Last Date Modified:

# import regular expressions module that has built in functions to validate and do other things for sanitization
import re

# initialize variable phonebook and make it a dictionary that can store phone numbers
# at this point, it is an empty dictionary called phonebook
phonebook = {}

def main():
	"""The main driver function of our Phonebook."""
	print("\n!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
	print("Welcome to the fanciest Phonebook EVER!\n")
	# initialize option variable
	option = ""

	while option != "E":
		# Ask the user what they want to do
		option = input("You have the power to: \n\t(A)dd contacts \n\t(D)elete contacts \n\t(P)rint your Phonebook \n\t(S)earch \n\t(E)xit. \nWhich would you like to do? ")

		if option.upper() == "A":
			name = input("\nWhat is the name of your contact? ")
			number = input("\nWhat is " + name + "'s number? ")
			add_contact(name, number)
		elif option.upper() == "D":
			name = input("\nWhat contact are you removing? ")
			delete_contact(name)
		elif option.upper() == "P":
			print_phonebook()
		elif option.upper() == "S":
			search_term = input("\nDo you want to search by (N)ame or by (Ph)one Number? ")
			search_phonebook(search_term)
		elif option.upper() == "E":
			exit_phonebook()
		else:
			print ("\nI'm sorry that is not an acceptable option. ")


# create a function for adding information to the phonebook dictionary
def add_contact(name, phone_number):
	"""Does an addition to the Phonebook with added contact info."""
#--------------------- Begin RegEx-----------------#
#---------- Need to Research on own time-----------#

	regex = "\s+\Z"
	replacement_string = ""
	scrubbed_name = re.sub(regex, replacement_string, name)
	
	regex = "[0-9]+"
	nums = re.findall(regex, phone_number)
	new_num = ""
	for every_num in nums: 
		new_num += every_num

	# Introduce the correct formatting
	formatted_num = "(" + new_num[0:3] + ") " + new_num[3:6] + "-" + new_num[6:]


	phonebook[scrubbed_name] = formatted_num
	print("Thank you. Your new contact " + scrubbed_name + " was added with the following phone number: " + formatted_num + ". \n")


#--------------------- End RegEx -------------------#

def delete_contact(name):
	"""Remove the given contact from the Phonebook."""
	if name in phonebook:
		del phonebook[name]
		print("You have successfully deleted " + name + "from your Phonebook.\n")
	else:
		print("That contact already does not exist.")


def print_phonebook():
	"""Prints the contents of the whole dictionary."""
	print("\nThese are the contacts in your phonebook:")
	for name in phonebook:
		print("\n")
		print("\t", name, ": ", phonebook[name])
	print("\n")

def search_phonebook(search_term):
	"""Finds contact information based on input and information desired."""
	
	if search_term.upper() == "N":
		"""Find the number associated with a specific name."""
		name = input("Who are you trying to search for? ")
		if name in phonebook:
			number = phonebook[name]
			print("The number for " + name + " is " + number + ".\n")
		else:
			print("Sorry, no contact exists with that name. ")
	elif search_term.upper() == "PH":
		"""Find the name associated with a specific phone number."""
		search_number = input("\n\tWhat is the phone number you are using to search with.")
		# more generic way to do the following search: for key, value in dictionary.items()
		result = ""
		for name, number in phonebook.items():
			if search_number == number:
				print(number + "is linked to " + name + "\n")
				result = name
			
			if result == "":
				print("Sorry, no contact is linked to that number.")


def exit_phonebook():
	print("\nHave a nice day!")
	print("\n\n\n")
	exit()

if __name__ == '__main__':
	main()