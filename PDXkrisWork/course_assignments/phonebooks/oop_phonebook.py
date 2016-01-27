"""A Phonebook program implemented with classes."""
"""Code-Along assignment with Tiffany at Code Guild."""
# __date_created__ = "2015.01.26"
# __date_modified__ = "2015.01.27"
__author__ = "Kris Kuchinka"

import re

def main():
	# Test the Contact and Adress classes with Jim Everyperson
	jim = Contact("Jim", "Everyperson")
	jim.phone_num = "5038945940"
	jim.email = "jim@gmail.com"
	jim.update_address("Home", city="Portland")
	jim.update_address("Work", "1234 Awesome Ln", "Bld. G", "Vancouver", "WA", "98684", "USA")
	print(jim)

class Contact:
	"""Defines the contact object to store information about people"""
	def __init__(self, f_name, l_name):
		# Assign past arguments to their corresponding properties
		self.first_name = f_name
		self.last_name = l_name
		self.phone_num = ""
		# Initiate empty address dictionary
		self.address = {}
		self.email = ""

	"""set custom values to empty strings, making them not required"""
	def update_address(self, add_key, street=None, 
					   unit=None, city=None, state=None, 
					   zip_code=None, country=None):
		"""Update the address at Addy_key with info passed."""
		# Check to see if there is already an address for that key
		if add_key in self.address:
			address = self.address[add_key]		
		else:
			# Make a new Address object
			address = Address()

		# Make a new address object that will be put into dictionary
		address = Address()
		# Set the new address street to whatever it was passed
		# Use if to validate wether it is not NONE value
		if street:
			address.street = street
		if unit:
			address.unit = unit
		if city:
			address.city = city
		if state:
			address.state = state
		if zip_code:
			address.zip_code = zip_code
		if country:
			address.country = country
		# Assign the address to the given address key for the contact
		self.address[add_key] = address

	def format_phone_num(self, phone_num):
		"""Make format of phone number uniform"""
		# Scrub and reformat the phone number to follow (xxx) xxx-xxxx pattern
		# Remove all but the numbers
		regex = "[0-9]+"
		nums = re.findall(regex, phone_num)
		new_num = ""

		# Take everything in the list of numbers and make it into a string of nums
		for every_num in nums:
			new_num += every_num
		
		# Introduce the correct formatting to the string of nums
		formatted_num = "(" + new_num[0:3] + ") " + new_num[3:6] + "-" + new_num[6:]
		
		# Save formatted number to Contact
		self.phone_num = formatted_num
 
	def __str__(self):
		"""Print out the contact's info in formatted manner"""
		# Initialize formatted string
		formatted_str = "{0} {1}".format(self.first_name, self.last_name)
		# IF there is a phone number
		if self.phone_num:
			# Format the phone number uniformly
			self.format_phone_num(self.phone_num)
			# Add the uniform phone number to formatted string
			formatted_str += "\nPhone: {0}".format(self.phone_num)
		# If there is an email address
		if self.email:
			formatted_str += "\nEmail: {0}".format(self.email)
		# If there is at least one address
		if self.address:
			formatted_str += "\nAddress:"
			formatted_str += "\n--------------------------"
			# Loop through all the addresses and print them
			# Get all the key, value pairs of the addresses using the dictionary items function
			for key, address in self.address.items():
				formatted_str += "\n{0}:".format(key)
				formatted_str += "\n{0}".format(address)
				formatted_str += "\n--------------------------"

		return formatted_str


			


class Address:
	"""Defines class Address to be used with contact"""
	def __init__(self):
		self.street = ""
		self.unit = ""
		self.city = ""
		self.state = ""
		self.zip_code = ""
		self.country = ""

	def __str__(self):
		"""Print out address in proper format as one string instead of separate
		print statements"""
		formatted_str = ""
		if self.unit != "":
			formatted_str = "{0}, {1}".format(self.street, self.unit)
		formatted_str += "\n {0}, {1}".format(self.city, self.state)
		formatted_str += "\n {0}".format(self.zip_code)
		formatted_str += "\n {0}".format(self.country)

		return formatted_str

if __name__ == '__main__':
	main()
