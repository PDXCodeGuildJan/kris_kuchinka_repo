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

def main():
	GameInterface.get_guess()

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

	def get_guess(self, colors):
		"""Asks player about what they choose to play in a given round."""

		print("""\nPlease choose which colors to put in positions A, B, C, and D. Remember, 
order matters! Your color choices are: Red, Green, Blue, Yellow, Black, and 
White. No other colors exist in the world of Mastermind.\n """)
		
		position_a = input("Please select a color choice for position A: >>>  ")
		while position_a not in colors:
			print("Please enter a valid color. ")
			position_a = input("Please select a color choice for position A: >>>  ")

		position_b = input("Please select a color choice for position B: >>>  ")
		while position_b not in colors:
			print("Please enter a valid color. ")
			position_b = input("Please select a color choice for position B: >>>  ")

		position_c = input("Please select a color choice for position C: >>>  ")
		while position_c not in colors:
			print("Please enter a valid color. ")
			position_c = input("Please select a color choice for position C: >>>  ")

		position_d = input("Please select a color choice for position D: >>>  ")
		while position_d not in colors:
			print("Please enter a valid color. ")
			position_d = input("Please select a color choice for position D: >>>  ")
		
		guess = [position_a, position_b, position_c, position_d]
		
		# answer = 0
		# while answer <= len(guess):
		# 	print("The colors you picked out where {}".format(guess))
		# 	answer += 1

		for answer in guess:
			print(answer)

		confirm_guess = input("In the voice of Regis Philbin, 'Is that your final answer?' ")


		return guess



	def final_screen(self):
		"""Displays message of whether the player wins or loses, the varying 
		round guesses and other game data. This is the last screen that the 
		player will see, before they either quit or replay."""
		pass

if __name__ == '__main__':
	main()

















