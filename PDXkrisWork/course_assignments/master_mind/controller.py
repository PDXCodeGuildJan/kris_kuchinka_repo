# This is a test
"""Control module for the game of Master Mind"""
"""<<<<<(Insert game description)>>>>>"""

__author__ = "Alexis Bird & Kris Kuchinka"

"""
Created initial flow chart, UML diagram on 2015.02.15-2015.02.16 together. 
Program is created with MVC concept in mind.

Creation Date: 2016.02.17
Date Modified: 
Date Finished:
"""
import random
from model import *
from view import *

class MasterMind():
	"""
	Template for methods to make the game function.
	"""

	def __init__(self):
		self.view = GameInterface()
		self.model = GameData()


	def create_secret_code(self):
		"""
		Method for computer Master Mind to randomly generate the Secret 
		Code.
		"""
		colors = self.model.peg_colors
		secret_list = []
		while len(secret_list) < 4:
			random_color = random.choice(colors)
			secret_list.append(random_color)

		return secret_list


	def start_game(self):
		"""
		Method that starts the game.
		"""
		pass
		# Welcome the player
		# Get the player name
		# Tell the player how to navigate the game
			# How to access the rules
			# How to quit at any input 
		# Reveal the blank game board 
		# "Ready to start? (Y)es or (N)o"

	def begin_round(self):
		"""
		Method that starts the next round.
		"""
		
		colors = self.model.peg_colors
		guess = self.view.get_guess(colors)

	def display_rules(self, rules):
		"""
		Gives player option to view the rules of the game.
		"""
		# create variable for rules
		# offer user opportunity to be given the rules

		# if string.upper() == "RULES":
		# 	GameData.rules
		pass

	def color_search(self):
		"""
		Method that searches whether each color in the player guess matches 
		any color in the Secret Code.
		"""
		# We definitely have had a lot of trouble with this function,
		# to the point where we decided to stop and come back to it.
		# We feel like the TDD helps us, but we were only able to utilize
		# it with Patrick's help and guidance. We don't seem to have a strong
		# enough grasp of it on our own. Also, the MVC concept throws us off
		# at times. The general concept is understood overall, but actually
		# implementing it gets a little confusing sometimes.
		chosen_colors = ["Black", "White", "Blue", "Yellow"]
		return chosen_colors

		# chosen_colors = self.view.get_guess()
		
		

		# Take in the players round choice and compare to the master mind secret

		# What can go wrong?>>>
			# It could not match colors correctly
			# It could not loop through every color
			# It could 

	def position_search(self):
		"""
		Method that takes colors that are both in the player guess and Secret
		Code and checks to match if any position of those colors are in the same 
		place.
		"""
		pass

	def master_conf(self):
		"""
		Method where the computer evaluates how to respond to player's 
		guess.
		"""
		pass

	def win():
		"""
		Method that determines if player has won.
		"""

		# while current round <= 10
		while self.model.current_round <= 10:
			if self.model.player_guess == secret_code:
				return True
			else:
				return False
			

		# if player_guess == secret code
			# display secret code
			# print congrats to user
#+++++++POSSIBLE OPTION----> offer option to play again
		pass

	def lose():
		"""
		Method that determines if player has lost.
		"""
		if self.model.current_round > 10 and self.model.player_guess != secret_code:
			return True


#+++++++POSSIBLE OPTION----> offer option to play again		
		pass

	def advance_round():
		"""
		Method that increments the round that the player is on.
		"""
		pass

if __name__ == '__main__':
	MasterMind()