"""Control module for the game of Master Mind"""
"""<<<<<(Insert game description, yay descriptions!!!)>>>>>"""

__author__ = "Alexis Bird & Kris Kuchinka"

"""
Created initial flow chart, UML diagram on 2015.02.15-2015.02.16 together. 
Program is created with MVC concept in mind.

Creation Date: 2016.02.17
Date Modified: 
Date Finished:
"""

from model import *
from view import *

class MasterMind():
	"""Template for methods to make the game function."""

	def __init__(self):
		self.view = GameInterface()
		self.model = GameData()


	def create_secret_code(self):
		"""Method for computer Master Mind to randomly generate the Secret 
		Code."""
		pass 

	def start_game(self):
		"""Method that starts the game."""
		pass
		# Welcome the player
		# Get the player name
		# Tell the player how to navigate the game
			# How to access the rules
			# How to quit at any input 
		# Reveal the blank game board 
		# "Ready to start? (Y)es or (N)o"

	def begin_round(self):
		"""Method that starts the next round."""
		pass

	def display_rules(self, rules):
		"""Gives player option to view the rules of the game."""
		pass
		# if string.upper() == "RULES":
		# 	GameData.rules

	def color_search(self):
		"""Method that searches whether each color in the player guess matches 
		any color in the Secret Code."""
		pass

	def position_search(self):
		"""Method that takes colors that are both in the player guess and Secret
		Code and checks to match if any position of those colors are in the same 
		place."""
		pass

	def master_conf(self):
		"""Method where the computer evaluates how to respond to player's 
		guess."""
		pass

	def win():
		"""Method that determines if player has won."""
		pass

	def lose():
		"""Method that determines if player has lost."""
		pass

	def advance_round():
		"""Method that increments the round that the player is on."""
		pass