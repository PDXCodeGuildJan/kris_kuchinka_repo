"""A computer version of the game Angry Dice."""

__author__ = "Kris Kuchinka"
__conceptPartner__ = "Sarah Fellows"

from random import randint


def main():
	current_stage = 1
	angry = Angry_Dice("Jim")
	angry.roll_dice()
	angry.check_angry()
	print(current_stage)


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

	
	def roll_dice(self):
		"""Method to roll the dice for game play"""
		
		if not self.die_1.locked:
			# Roll the dice we need to roll
			self.die_1.roll()

		if not self.die_2.locked:
			# Roll the dice we need to roll
			self.die_2.roll()

		print(self.die_1)
		print(self.die_2)

	
	
	def check_angry(self):
		"""Define method to check if both die are 'angry'"""
		
		if self.die_1.value == 3 and self.die_2.value == 3:
			print("angry!!!")
			current_stage = 1
	
	
	def win_round(self):
		"""Define method that informs player they have won their current round"""
		pass
	
	
	def player_choice(self):
		"""Method to allow player to hold 1, roll 1 or roll both die again"""
		pass

	
	def evaluate_hold(self):
		"""Method to evaluate and ensure that game rules are followed, i.e. invalid dice can not be held"""
		pass

		
	def advance_round(self):
		"""Method to advance player to next stage in the game or to the winning stage"""
		pass



class Die:
	"""Define object that describes dice and implements their actions (refer to imported random library for rolling authenticity)"""

	def __init__(self):
		"""Define Die library that is comprised of the various dice sides."""
		self.value = 1
		self.locked = False
		# ASCII art representations of each side of the dice.
		self.sides = {
			1: """    
 -----
|     |
|  0  |
|     |
 -----  
	   """,

			2: """    
 -----  
|0    |
|     |
|    0|
 -----  
	   """,

			3: """
 -----  
| o o |
|  |  |
| ### |
 -----  
 RARRR!
	   """,

			4: """    
 -----  
|0   0|
|     |
|0   0|
 -----  
	   """,

			5: """    
 -----  
|0   0|
|  0  |
|0   0|
 -----  
	   """,

			6: """     
 -----  
|0   0|
|0   0|
|0   0|
 -----  
	   """	

}				    					  

	def roll(self):
		"""Define method to roll dice"""
		self.value = randint(1,6)
		
	def __str__(self):
		"""Returns a string representation of the die."""
		return self.sides[self.value]



if __name__ == '__main__':
	main()