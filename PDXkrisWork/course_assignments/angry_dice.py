"""A computer version of the game Angry Dice."""

__author__ = "Kris Kuchinka"
__conceptPartner__ = "Sarah Fellows"

from random import randint


def main():

	print(sides[1])

class Angry_Dice:
	"""Defines the variables and methods needed to play the game."""
	def __init__(self, player_name):
		# initalize necessary variables for Angry_Dice
		self.current_stage = 1
		self.current_goal = []
		self.player_name = ""
		# initialize a dictionary for the Die
#!#!#!#!# This may be wrong #!#!#!#!#
		self.die_1 = Die()
		self.die_2 = Die()

	
	def roll_die(self, die_1, die_2):
		"""Define method to roll dice"""
		pass
	
	
	def check_angry(self, die_1, die_2):
		"""Define method to check if both die are 'angry'"""
		pass
	
	
	def win_round(self, current_stage):
		"""Define method that informs player they have won their current round"""
		pass
	
	
	def palyer_choice(self, die_1, die_2):
		"""Method to allow player to hold 1, roll 1 or roll both die again"""
		pass

	
	def evaluate_hold(self, die_1, die_2):
		"""Method to evaluate and ensure that game rules are followed, i.e. invalid dice can not be held"""
		pass

		
	def advance_round(current_stage):
		"""Method to advance player to next stage in the game or to the winning stage"""
		pass



class Die:
	"""Define object that describes dice and implements their actions (refer to imported random library for rolling authenticity)"""
	def __init__(self):
		"""Define Die library that is comprised of the various dice sides."""
		self.value = 1


	def roll_dice(self):
		"""Method to roll the dice for game play"""
		pass



sides = {
	1: """    
	-----  
       |     |
       |  0  |
       |     |
        -----  
	   """,

	2: """    -----  
			 |0    |
			 |     |
			 |    0|
			  -----  
	   """,

	3: """    -----  
			 | o o |
			 |  |  |
			 | ### |
			  -----  
			  RARRR!
	   """,

	4: """    -----  
			 |0   0|
		     |     |
			 |0   0|
			  -----  
	   """,

	5: """    -----  
			 |0   0|
			 |  0  |
			 |0   0|
			  -----  
	   """,

	6: """     -----  
			  |0   0|
			  |0   0|
			  |0   0|
			   -----  
	   """	

}				    					  



if __name__ == '__main__':
		main()