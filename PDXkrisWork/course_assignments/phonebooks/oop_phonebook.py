"""A Phonebook program implemented with classes."""

__author__ = "Kris Kuchinka"

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
	def update_address(self, add_key, street="", 
					   unit="", city="", state="", 
					   zip="", country=""):
		"""Update the address at Addy_key with info passed."""
		pass

	def format_phone_num(self, phone_num):
		"""Make format of phone number uniform"""
		pass

	def print_contact(self):
		"""Print out the contact's info in formatted manner"""
		pass

class Address:
	"""Defines class Address to be used with contact"""
	def __init__(self):
		self.street = ""
		self.unit = ""
		self.city = ""
		self.state = ""
		self.zip_code = ""
		self.country = ""

	def print_address(self):
		"""Print out address in proper format"""
