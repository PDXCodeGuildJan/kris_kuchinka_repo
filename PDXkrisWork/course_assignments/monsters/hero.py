# Code along exercise created in Class at Code Guild
# Created by: Kris Kuchinka
# Creation Date: 2016.02.05

# Import class from creature.py module
from creature import Creature
# Import class from monster.py module
from monster import Monster

class Hero(Creature):
	"""Create a class of Hero and let it inherit properties from Creature class. 
	This is object inheritance."""

	def __init__(self):
		super(Hero, self).__init__()

		self.level = 1

class MonsterHero(Monster, Hero):

	def __init__(self):
		Monster.__init__(self)
		Hero.__init__(self)

		self.second_weapon = self.weapon	

