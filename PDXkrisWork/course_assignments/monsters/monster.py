# Code along exercise created in Class at Code Guild
# Created by: Kris Kuchinka
# Creation Date: 2016.02.05

# Import class from creature.py module
from creature import Creature


class Monster(Creature):
	""" Create a class of Monster and let it inherit properties from Creature class.
	This is object inheritance."""

	AGGRO = "aggressive"
	DEFENSE = "defensive"

	def __init__(self):

		super(Monster, self).__init__()
		"""'super' is built in variable in Python that represents the object 
		that it is inherited from. First thing to do is call the parent 
		initialization function."""

		self.personality = Monster.AGGRO

