"""Model module for the game of Master Mind"""
"""<<<<<(Insert game description)>>>>>"""

__author__ = "Alexis Bird & Kris Kuchinka"

"""
Created initial flow chart, UML diagram on 2015.02.15-2015.02.16 together. 
Program is created with MVC concept in mind.

Creation Date: 2016.02.17
Date Modified: 
Date Finished:
"""

class PlayerPeg():
	"""
	Defines the attributes of the object that is Player Peg
	"""
	def __init__(self, color):
		self.color = color

class ConfPeg():
	"""
	Defines the attributes for the confirmation pegs that the computer 
	utilizes to tell the player what is correct.
	"""
	def __init__(self, color):
		self.color = color

class GameData():
	"""
	Holds all the information and content for the current game that is being 
	played.
	"""
	def __init__(self):
		self.rules = """
				Master Mind
"Easy to learn. Easy to play. But not so easy to win."

How to Play:
1. The computer generates a Secret Code of four code pegs.
2. The player chooses four code pegs and the position they go in, in an attempt 
to match position and color of the Secret Code.
3. The computer evalues the player choice and gives the following feedback via 
pegs:
	Black Peg: One for each code peg that is the right color and in the right 
	position.
	White Peg: One for each code peg that is the right color, but in the wrong
	position.
4. The player gets 10 rounds to accurately figure out the Secret Code. If they 
do it within 10 rounds, they win, otherwise they lose.
"""
		self.player_name = ""
		self.peg_colors = ["white", "black", "blue", "green", "yellow", "red"]
		self.eval_colors = ["white", "black"]
		self.secret_code = None
		self.current_guess = None
		self.past_guesses = {}
		self.current_round = 1
		self.track_eval = {}
		self.current_eval = {}		

class Guess():
	"""
	Stores the past and current guesses of the player.
	"""
	def __init__(self):
		self.player_guess = []
		self.mm_eval = []
