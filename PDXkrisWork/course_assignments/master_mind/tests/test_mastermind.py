__author__ = "Alexis Bird and Kris Kuchinka"

"""
Practicing Test Driven Development for the game of MasterMind
"""
import unittest
from controller import MasterMind

class ControllerTest(unittest.TestCase):

	def setUp(self):
		"""
		Create an instance of the MasterMind class so we can leverage its function in our tests.\
		"""
		self.mastermind = MasterMind()

	def tearDown(self):
		"""
		Delete the MasterMind instance we made in the setUp.
		"""
		del self.mastermind


	def test_create_secret_code_is_list(self):
		"""
		Perform tests to makes sure function produces a secret code.
		"""

		# Saving variable, running function
		code = self.mastermind.create_secret_code()
		
		# Test to make sure that the provided data is a list
		self.assertIsInstance(code, list, "Your value is not a list.")

	def test_create_secret_code_len_is_four(self):
		"""
		Perform test to ensure that the secret code is exactly 4 long.
		"""
		# Saving variable, running function
		code = self.mastermind.create_secret_code()

		# Test to make sure list length is exactly four
		self.assertEqual(len(code), 4)

	def test_create_secret_code_list_is_strings(self):
		"""
		Perform test to check that given list is full of strings.
		"""
		# Saving variable, running function
		code = self.mastermind.create_secret_code()

		# Test to make sure list items are strings
		for item in code:
			self.assertIsInstance(item, str, "Your value is not a string.") 

	def test_create_secret_code_items_are_given_colors(self):
		"""
		Perform a test to make sure the items are the colors that are given in object.
		"""
		colors = self.mastermind.model.peg_colors

		code = self.mastermind.create_secret_code()

		for item in code:
			self.assertIn(item, colors)

	def test_create_secret_code_is_random(self):
		"""
		This test is not flawless, but it opens the gateway for testing whether
		create_secret_code is random.
		"""

		code = self.mastermind.create_secret_code()

		code2 = self.mastermind.create_secret_code()

		self.assertNotEqual(code, code2, "The two resulting codes are equivalent")











