"""Model module for the game of Master Mind"""
"""<<<<<(Insert game description)>>>>>"""

__author__ = "Alexis Bird"
__author__ = "Kris Kuchinka"

"""
Created initial flow chart, UML diagram on 2015.02.15-2015.02.16 together. Program is created with MVC concept in mind.

Creation Date: 2016.02.17
Date Modified: 
Date Finished:
"""

class Player_Peg():
	"""Defines the attributes of the object that is Player Peg"""
	def __init__(self, color):
		self.color = color

class Conf_Peg():
	"""Defines the attributes for the confirmation pegs that the computer utilizes to tell the player what is correct."""
	def __init__(self, color):
		self.color = color

class Game_Data():
	"""Holds all the information and content for the current game that is being played."""
	def __init__(self):
		self.rules = ""
		self.player_name: ""
		self.peg_colors: ["white", "black", "blue", "green", "yellow", "red"]
		self.eval_colors: ["white", "black"]
		self.secret_code: None
		self.current_guess: None
		self.past_guess: None
		self.current_round = 1
		self.track_eval = {}
		self.current_eval = {}		
