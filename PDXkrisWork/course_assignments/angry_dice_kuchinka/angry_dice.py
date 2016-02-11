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



def main():
	"""Starts and runs the game. It sets the order and flow of the game for the
	player."""

	# Note: the \ denotes that line should continue as one statement, despite
	# being broken up in the code.
	print("\nWelcome to Angry Dice. I hope you enjoy the game. Please note, "  \
	      "at any prompt, you can type 'q' to quit the game.\n")


	player_name = input("What is your name? >>>  ")

	# Wrap function end_game around all input options so that the player can
	# press "Q" or "q" and leave the game if they desire to
	end_game(player_name)

	# Create a new game according to the Angry_Dice object template below
	game = Angry_Dice(player_name)

	# Use .format to insert player name into message	
	print("\nOk, {}. Let's play the game...".format(game.player_name))

	# Give the player option to review/read through game rules
	game.game_rules()


	# Create a condition that will continue to advance the stage, until stage
	# becomes a value of 4, meaning the game is over and that the player has
	# won
	while game.current_stage < 4:
		# Clear the terminal window for better play, less screen clutter
		os.system("clear")
		# Roll the dice, using function created below, that player initiated
		# above when they started the game.
		game.roll_dice()
		# The function "check_angry" ensures that both die are not 3 or "angry".
		# If they are both angry, the function sends the player back to Stage 1.
		if game.check_angry():
			# Dice need to be unlocked if the player is being sent back to 
			# Stage 1.
			game.unlock_die()
			# "continue" is a way to go back to the top of the current loop
			# without stopping the loop.
			continue
		# If the player wins, the "win_round" function is implemented and the
		# player moves on to the next stage or wins the game.
		if game.win_round():
			# Wether the player has won or they are moving to the next stage,
			# the dice must be unlocked.
			game.unlock_die()

			continue
		# Gives the player in the current game the chance to select which die 
		# the player would like to lock or not lock
		game.player_choice()


class Angry_Dice():
	"""Defines the variables and methods needed to play the game Angry Dice."""
	# initalize necessary variables to pass to the Angry_Dice class	
	def __init__(self, player_name):
		self.current_stage = 1
		# Create a dictionary of each stage(1-3) with the values needed to win
		#	for each round
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
		# if die_1 is locked, print that it is locked to terminal for user
		elif self.die_1.locked:
			print("Die 1 is locked.")

		# Check to make sure that die_2 is not locked by player
		if not self.die_2.locked:
			# Roll the dice we need to roll
			self.die_2.roll()
		# if die_1 is locked, print that it is locked to terminal for user		
		elif self.die_2.locked:
			print("Die 2 is locked.")


		print(self.die_1)
		print(self.die_2)

	
	
	def check_angry(self):
		"""Define method to check if both die are 'angry'"""
		
		if self.die_1.value == 3 and self.die_2.value == 3:
			self.current_stage = 1
			
			input("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		Anger has occurred. Back to Stage 1. Press enter to continue
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")
			return True
		else: 
			return False
	
	
	def win_round(self):
		"""Define method that informs player they have won their current round"""
		print("Current stage:", self.current_stage)
		current_goal = self.stage_goal[self.current_stage]
	
		if self.die_1.value in current_goal and self.die_2.value in current_goal:
			if self.die_1.value != self.die_2.value:
				if self.current_stage < 3:
					self.current_stage += 1
					os.system("clear")
					input("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		 	Goal met! Welcome to stage {}. Press enter to continue
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
					""".format(self.current_stage))
					return True
				elif self.current_stage == 3:
					input("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  SUCCESS!!! You have won the game! Press enter once you are done celebrating.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
						""")
					exit()
		else:
			return False

		print("Stage after check:", self.current_stage)


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

	def unlock_die(self):
		self.die_1.locked = False
		self.die_2.locked = False

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
		end_game(game_understanding)
		
		if game_understanding.upper() == "N":
			print(rules)
			input("Press Enter to continue.")
		elif game_understanding.upper() == "Y":
			print("Let the game begin!")

				

def end_game(string):
	"""Gives user ability to press "Q" or "q" on any input and quit the program 
	at that point."""

	if string.upper() == "Q":
		print("\nSo sorry to see you go. Come back before the dice get more " \
			"angry.\n")
		exit()

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
	main()