"""A computer version of the game Angry Dice."""

__author__ = "Kris Kuchinka"
__conceptPartner__ = "Sarah Fellows"

from random import randint


def main():

class Angry_Dice:
	"""Defines the variables and methods needed to play the game."""
#!#!#!#!-- I DON'T KNOW WHAT TO PUT IN THE PARENS BELOW
	def __init__(self, player_name):
		# initalize necessary variables for Angry_Dice
		self.current_stage: 1
		self.current_goal: []
		self.player_name: ""
		# initialize a dictionary for the Die
#!#!#!#!# This may be wrong #!#!#!#!#
		self.die_1: {Die}
		self.die_2: {Die}

	"""Define method to roll dice"""
	def roll_die(self, die_1, die_2):
		pass
	
	"""Define method to check if both die are 'angry'"""
	def check_angry(self, die_1, die_2):
		pass
	
	"""Define method that informs player they have won their current round"""
	def win_round(self, current_stage):
		pass
	
	"""Method to allow player to hold 1, roll 1 or roll both die again"""
	def palyer_choice(self, die_1, die_2):
		pass

	"""Method to evaluate and ensure that game rules are followed, i.e. invalid dice can not be held"""
	def evaluate_hold(self, die_1, die_2):
		pass

	"""Method to advance player to next stage in the game or to the winning stage"""
	def advance_round(current_stage):
		pass


"""Define object that describes dice and implements their actions (refer to imported random library for rolling authenticity)"""
class Die:






















if __name__ == '__main__':
		main()