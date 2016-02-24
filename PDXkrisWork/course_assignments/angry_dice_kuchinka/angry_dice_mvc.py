"""A computer version of the game Angry Dice."""

__author__ = "Kris Kuchinka"

"""Created flow chart of game and UML diagram that was used to code this program
with Sarah Fellows at Code Academy.

Creation Date: 2016.01.27
Date finished: 2015.02.09
"""

# Import randint function from random module to implement and use on dice roll.
from random import randint
# Import os to use "operating system like" traits, like clearing the terminal
# after a certain event.
import os

class Angry_Controller():

	def __init__(self):
		self.model = Angry_Model()
		self.view = Angry_View()

	def play_game(self):

		# Welcome the user and ask for their name
		self.model.player_name = self.view.begin_game()

		# Show them the rules
		self.view.game_rules()

		while self.model.current_stage < 4:

			self.roll_dice()

			if self.check_angry():

				self.unlock_die()

				continue

			if self.win_round():

				self.unlock_die()

				continue

			self.player_choice()

	def roll_dice(self):
		"""Method to roll the dice for game play"""
		
		# Check to make sure that die_1 is not locked by player
		if not self.model.die_1.locked:
			# Roll the dice we need to roll
			self.model.die_1.roll()
		# if die_1 is locked, print that it is locked to terminal for user
		elif self.model.die_1.locked:
			self.view.print_locked("1")

		# Check to make sure that die_2 is not locked by player
		if not self.model.die_2.locked:
			# Roll the dice we need to roll
			self.model.die_2.roll()
		# if die_1 is locked, print that it is locked to terminal for user		
		elif self.model.die_2.locked:
			self.view.print_locked("2")

		self.view.print_dice(self.model.die_1, self.model.die_2)

	def check_angry(self):
		"""Define method to check if both die are 'angry'"""
		
		if self.model.die_1.value == 3 and self.model.die_2.value == 3:
			self.model.current_stage = 1
			
			self.view.display_angry()

			return True
		else: 
			return False

	def unlock_die(self):
		self.die_1.locked = False
		self.die_2.locked = False

	def player_choice(self):
		"""Method to allow player to hold 1, roll 1 or roll both die again"""
		
		# Ask the player if they want to lock the die
		# Evaluate their response (yes or no)
		# If yes, lock chosen die
		lock_die_1 = input("Would you like to hold Die 1? (Y)es or (N)o? >>> ")
		end_game(lock_die_1)

		if lock_die_1.upper() == "Y":
			self.die_1.locked = True
		else:
			lock_die_1.upper() == "N"
			self.die_1.locked = False

		lock_die_2 = input("Would you like to hold Die 2? (Y)es or (N)o? >>> ")
		end_game(lock_die_2)
		if lock_die_2.upper() == "Y":
			self.die_2.locked = True
		else: 
			lock_die_2.upper() == "N"
			self.die_2.locked = False

	def win_round(self):
		"""Define method that informs player they have won their current round"""

		self.view.display_current_stage(self.model.current_stage)

		current_goal = self.model.stage_goal[self.model.current_stage]
	
		if self.model.die_1.value in current_goal and self.model.die_2.value in current_goal:
			if self.model.die_1.value != self.model.die_2.value:
				if self.model.current_stage < 3:
					self.model.current_stage += 1
					os.system("clear")
					self.view.display_new_stage(self.model.current_stage)
					return True
				elif self.current_stage == 3:
					self.view.display_win()
					exit()
		else:
			return False

		self.view.show_new_stage(self.model.current_stage)



class Angry_View():

	def begin_game(self):
		print("\nWelcome to Angry Dice. I hope you enjoy the game. Please note, "  \
	      "at any prompt, you can type 'q' to quit the game.\n")

		player_name = input("What is your name? >>>  ")

		self.end_game(player_name)

		# Use .format to insert player name into message	
		print("\nOk, {}. Let's play the game...".format(player_name))

		return player_name

	def game_rules(self):
		rules = """
A thorough explanation of the game rules for a new player.
		 
		   ----------The Battle----------

Duelists roll their dice at the same time, trying to get from 1 to 6 
the fastest. The first to do so wins! Rolling two 'Angry Dice' means 
that you have to start over at Round 1. 

You may also choose to lock dice. If you lock a die, it won't be rolled. 
If you lock an incorrect die, you will be able to unlock it after the 
next roll. 

		    ---------- Round Goals ----------
Each duelist gets two 'Angry Dice'. Duelists roll thier dice, looking to 
complete Round 1 through Round 3. When each round is complete, the duelist 
must declare it out loud.
		
	Round 1 objective:
	You must have a value of 1 and 2 on your two die.
		
	Round 2 objective:
	Player must have one 'Angry Dice' and one die with the value of 4.
		
	Round 3 objective:
	Player die must have values of 5 and 6.

		      ---------- Victory ----------
The first duelist to race through all the stages and announces Get Angry!
is declared the victor.\n
"""


		game_understanding = input("Do you know the rules of the game?" \
			" (Y)es or (N)o >>>   ")
		# Allows player to quit, if they choose to type 'q'		
		self.end_game(game_understanding)
		
		if game_understanding.upper() == "N":
			print(rules)
			input("Press Enter to continue.")
		elif game_understanding.upper() == "Y":
			print("Let the game begin!")

	def print_locked(self, die_num):
		print("Die", die_num, "is locked")

	def print_dice(self, die_1, die_2):
		print(die_1)
		print(die_2)

	def display_angry(self):
		input("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		Anger has occurred. Back to Stage 1. Press enter to continue
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")

	def display_current_stage(self, current_stage):
		print("Current stage:", current_stage)

	def show_new_stage(self, current_stage):
		print("Stage after check:", current_stage)

	def display_win(self):
		input("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  SUCCESS!!! You have won the game! Press enter once you are done celebrating.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
						""")

	def display_new_stage(self, current_stage):
		input("""
		++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				 	Goal met! Welcome to stage {}. Press enter to continue
		++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
							""".format(current_stage))

	def end_game(self, string):
		"""Gives user ability to press "Q" or "q" on any input and quit the program at that point."""

		if string.upper() == "Q":
			print("\nSo sorry to see you go. Come back before the dice get more " \
				"angry.\n")
			exit()


class Angry_Model():
	"""Defines the variables and methods needed to play the game Angry Dice."""
	# initalize necessary variables to pass to the Angry_Dice class	
	def __init__(self):
		self.current_stage = 1
		# Create a dictionary of each stage(1-3) with the values needed to win
		#	for each round
		self.stage_goal = {1:[1,2], 2:[3, 4], 3:[5,6]}
		self.player_name = ""
		self.die_1 = Die()
		self.die_2 = Die()

class Die:
	"""Define object that describes dice and implements their actions (refer 
		to imported random library for rolling authenticity)"""

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
	game = Angry_Controller()
	game.play_game()