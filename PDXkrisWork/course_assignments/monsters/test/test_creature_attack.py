__author__ = "Kris Kuchinka"

import unittest
# Import the class where the function lives that you're testing
from creature import Creature, Weapon


# Make a new TestCase, CreatureAttackTest, which inherit's from unittest.TestCase
class CreatureAttackTest(unittest.TestCase):
	# Write functions that are tests for the creature.py module

	# Make the things and do the setup that every test in the TestCase needs.
	def setUp(self):
		"""
		Create an instance of the Creature class that we can leverage it's function in our tests.
		"""
		self.creature = Creature()


	# Undo everything that your setUp function did
	def tearDown(self):
		"""
		Delete the Creature instance we made in the setUp.
		"""
		del self.creature


	# Test to make sure we get an int back
	def test_attack_return_int(self):
		"""
		Ensure that when an attack is called an int is returned.
		"""

		# Call the attack function of our creature and catch what it returns in value.
		value = self.creature.attack()

		self.assertIsInstance(value, int, "Returned attack value is not an int.")

	def test_no_weapon_return_base_damage(self):
		"""
		Ensure that with no weapon equipped, the creature does its base damage.
		"""

		# Manually set the base damage to 3
		self.creature.attack_points = 2

		# Get the creatures attack value
		value = self.creature.attack()

		self.assertEqual(value, 2, "Expected base attack value not given.")

	def test_with_weapon_return_damage(self):
		"""
		Ensure that with a weapon, the creature does base damage + weapon damage.
		"""

		# Make a weapon to give to creature
		weapon = Weapon(3)

		# Give the weapon to the creature
		self.creature.weapon = weapon

		# Set creature's base attack value
		self.creature.attack_points = 2

		# Get the creature's attack value
		value = self.creature.attack()

		# Assert the attack value is the base + weapon damage
		self.assertEqual(value, 5,
		 	"Expected base attack with weapon not correct.")















