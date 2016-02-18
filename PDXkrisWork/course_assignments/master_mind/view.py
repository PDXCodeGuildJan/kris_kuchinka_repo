"""View module for the game of Master Mind"""
"""<<<<<(Insert game description)>>>>>"""

__author__ = "Alexis Bird & Kris Kuchinka"

"""
Created initial flow chart, UML diagram on 2015.02.15-2015.02.16 together. 
Program is created with MVC concept in mind.

Creation Date: 2016.02.17
Date Modified: 
Date Finished:
"""

class GameInterface():
	"""Defines the differing methods for displaying the game and game progress 
	and how it looks. This will also ask for user input."""

	def display_board(self, player_name, current_guess, past_guess, 
		current_eval, current_round, past_eval):
		"""Creates visual of necessary information to display game progress and 
		past guesses."""
		game_board = """

  	     |       Player Guess by Position       | Master Mind 
   Round |     A        B        C        D     |   Response
  -------------------------------------------------------------
         |                                      |  *  *  *  *
         |  +++++++  +++++++  +++++++  +++++++  |  W  B  W  W 
     1   |	+ BLK +	 + WHT +  + YLW +  + RED +  |  H  L  H  H
         |	+++++++	 +++++++  +++++++  +++++++	|  T  K  T  T
         |                                      |  *  *  *	*
  -------|--------------------------------------|--------------
         |                                      |  *  *  *  *
         |  +++++++  +++++++  +++++++  +++++++  |  W  B  W  W 
     2   |	+ BLK +	 + WHT +  + YLW +  + RED +  |  H  L  H  H
         |	+++++++	 +++++++  +++++++  +++++++	|  T  K  T  T
         |                                      |  *  *  *	*
  -------|--------------------------------------|-------------- 	               
                                                   
                                                                                                                                                                                                                       
"""



	def quit(self):
		"""Gives player option to quit at any point of input during the game."""

		if string.upper() == "Q":
			print("\nSo sad that you want to leave. Come back another time.\n")
			exit()

	def get_name(self):
		"""Asks player for name input before game begins."""
		player_name = input("What is your name, Friend? >>>   ")

	def get_guess(self):
		"""Asks player about what they choose to play in a given round."""
		pass

	def final_screen(self):
		"""Displays message of whether the player wins or loses, the varying 
		round guesses and other game data. This is the last screen that the 
		player will see, before they either quit or replay."""
		pass

















