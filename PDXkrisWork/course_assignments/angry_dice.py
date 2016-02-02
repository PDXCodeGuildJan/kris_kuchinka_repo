"""A computer version of the game Angry Dice."""

__author__ = "Kris Kuchinka"

"""Created flow chart of game and UML diagram that was used to code this program with Sarah Fellows at Code Academy.

   Creation Date: 2016.01.27
   Date finished: 

"""

# import randint function from random module to implement dice roll 
from random import randint


def main():
	# Create a player using the class Angry_Dice and call player Jim
	player = Angry_Dice("Jim")
	# Goal is reach stage 4. Set the beginning stage to 1 for start of game.
	player.current_stage = 1

	while player.current_stage != 4:
		# Roll the dice, using function created below and player initiated above
		player.roll_dice()
		player.player_choice()
		player.win_round()
	

	# Check if both the die are "angry"
	# Tell player what stage they are on
	print("Starting Stage:", player.current_stage)

	

	print("Stage after winround", player.current_stage + 1)


class Angry_Dice():
	"""Defines the variables and methods needed to play the game."""
	def __init__(self, player_name):
		# initalize necessary variables for Angry_Dice
		self.current_stage = 1
		self.stage_goal = {1:[1,2], 2:[3, 4], 3:[5,6]}
		self.player_name = player_name
		self.die_1 = Die()
		self.die_2 = Die()

	
	def roll_dice(self):
		"""Method to roll the dice for game play"""
		
		# Check to make sure that die_1 is not locked by player
		if not self.die_1.locked:
			# Roll the dice we need to roll
			self.die_1.roll()

		# Check to make sure that die_2 is not locked by player
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
		print("Current stage:", self.current_stage)
		current_goal = self.stage_goal[self.current_stage]
	
		if self.die_1.value in current_goal and self.die_2.value in current_goal:
			if self.die_1.value != self.die_2.value:
				print("Goal met")
				self.current_stage += 1

		print("Stage after check:", self.current_stage)


	def player_choice(self):
		"""Method to allow player to hold 1, roll 1 or roll both die again"""
		pass
		# ask the player if they want to lock the die
		# evaluate their response (yes or no)
			# if yes, lock chosen die
		lock_die_1 = input("Would you like to hold Die 1? (Y)es or (N)o)? ")
		if lock_die_1.upper() == "Y":
			self.die_1.locked = True
		else:
			lock_die_1.upper() == "N"
			self.die_1.locked = False

		lock_die_2 = input("Would you like to hold Die 2? (Y)es or (N)o? ")
		if lock_die_2.upper() == "Y":
			self.die_2.locked = True
		else: 
			lock_die_2.upper() == "N"
			self.die_2.locked = False

#!>!>!?####---> Possibly not necessary, part of holding decision
	def evaluate_hold(self):
		"""Method to evaluate and ensure that game rules are followed, i.e. invalid dice can not be held"""
		pass


# =====>>> Possibly unnecessary		
	# def advance_round(self):
	# 	"""Method to advance player to next stage in the game or to the winning stage"""
	# 	pass
		# if player is on Stage 1 and die 1 and 2 values are 1 and 2, advance player to Stage 2




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