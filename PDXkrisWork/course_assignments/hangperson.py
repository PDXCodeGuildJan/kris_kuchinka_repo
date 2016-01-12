#hangman.py
# A program about hanging people if you don't spell things correctly.




from random import randint

words = ["pterodactyl", "antidisestablishmentarianism", "existentialism", "universalism", "Machiavellianism", "Kierkegaard", "banana" ]
numWrong = 0
listedWord = [None]

# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over.
def hangperson():
   hang_person_picture()
   global listedWord

   # Greet the user
   print("Let's play a game of hangperson!")

   # Randomly select a word from the list of words
   #-- Need to find the length of list of words dynamically
   #-- Want to be able to add more words to the words list in the future
   words_num = len(words)
   #-- Create a variable (words_index) and assign it a random number
   #-- We want this to give us the random index number to pull from the list of words
   #-- len() function needs to have -1 on variable, because it is not a zero index starting count
   words_index = randint(0, words_num-1)
   #-- assign the randomly chosen index number list of words and give it a variable
   listedWord = words[words_index]
   
   # Make the randomly selected word into a list object
   listedWord = list(listedWord)

   # Make another list the same length as the word, but with
   # '_' instead of letters. This will track the user's progress.
   # Use the variable name currentState
   #-- First we need to find the length of the listedWord
   currentState = list("_" * len(listedWord))


   # Print the initial state of the game
   printHangperson(currentState)

   # Start the game! Loop until the user either wins or loses

   while currentState != listedWord and numWrong < 6:
      guess = userGuess()

      # see if the guess is in the word, update accordingly
      currentState = updateState(guess, currentState)

      printHangperson(currentState)

   # Determine if the user won or lost, and then tell them accordingly   
   if listedWord == currentState:
      print("You've won!!! Congratulations!")
   elif numWrong >= 6:
      print("You've lost the game. He hung. It's your fault.")



# Update the state of the game based on the user's guess.
#
# guess: a character guessed by the user
# currentState: the current state of the word/game
#
# return currentState
def updateState(guess, currentState):
   global numWrong

   # First, determine if the letter guessed is in the word.
   numInWord = listedWord.count(guess)

   # If it isn't, tell the user and update the numWrong var
   if numInWord == 0:
      print("I'm sorry. You guessed incorrectly.")
      numWrong += 1
   # If it is, congratulate them and update the state of the game.
   #    To update the state, make sure to replace ALL the '_' with
   #    the guessed letter.
   elif numInWord > 0:
      #-- cast the numInWord variable to a string
      correctNumber = str(numInWord)
      #-- create another if statement to manage the is/are grammar issue
      if numInWord == 1:
         print("Congratulations! You guessed correctly. There is " + correctNumber + " of the letter '" + guess + "' in the word.")
      elif numInWord > 1:
         print("Congratulations! You guessed correctly. There are " + correctNumber + " of the letter '" + guess + "' in the word.")
      #-- use while loop to loop through numInWords until there are no more letters to find in the word
      #-- create a new variable and set to 0 (flag)
      numFound = 0
      index = 0
      while numFound < numInWord and index < len(listedWord):
         # see if letter is in word at index
         if listedWord[index] == guess:
            currentState[index] = guess
            numFound += 1
         index += 1


   return currentState


# This helpful function prompts the user for a guess,
# accepting only single letters.
#
# returns a letter
def userGuess():
   guess = input("Guess a letter in the word! (Say 'exit' to stop playing) ")
   while len(guess) != 1:
      if guess == "exit":
         print("You have chosen to exit. Goodbye! Come back to the gallows again.  ")
         exit()
      elif len(guess) > 1:
         guess = input("Please guess again. Just one letter this time.  ")
      else:
         guess = input("Please guess again.  ")

   return guess


################# DO NOT EDIT BELOW THIS LINE ##################

# A helpful function to print the hangman.
# DO NOT CHANGE
#
# state: current state of the word
def printHangperson(state):
   person = [" O "," | \n | ", "\| \n | ", "\|/\n | ", "\|/\n | \n/  ", "\|/\n | \n/ \\"]
   print()

   if numWrong > 0:
      print(person[0])

   if numWrong > 1:
      print(person[numWrong-1])

   print("\n\n")

   for i in state:
      print(i, end=" ")

   print("\n")



# ------------------------------ ASCii Images -------------
# HangPerson
def hang_person_picture():
   hang_person = """                                                                                                              
           ,--,                                   ,-.----.                                                       
         ,--.'|                                   \    /  \                                                      
      ,--,  | :                                   |   :    \                                                     
   ,---.'|  : '                  ,---,            |   |  .\ :          __  ,-.               ,---.        ,---,  
   |   | : _' |              ,-+-. /  |  ,----._,..   :  |: |        ,' ,'/ /|  .--.--.     '   ,'\   ,-+-. /  | 
   :   : |.'  |  ,--.--.    ,--.'|'   | /   /  ' /|   |   \ : ,---.  '  | |' | /  /    '   /   /   | ,--.'|'   | 
   |   ' '  ; : /       \  |   |  ,"' ||   :     ||   : .   //     \ |  |   ,'|  :  /`./  .   ; ,. :|   |  ,"' | 
   '   |  .'. |.--.  .-. | |   | /  | ||   | .\  .;   | |`-'/    /  |'  :  /  |  :  ;_    '   | |: :|   | /  | | 
   |   | :  | ' \__\/: . . |   | |  | |.   ; ';  ||   | ;  .    ' / ||  | '    \  \    `. '   | .; :|   | |  | | 
   '   : |  : ; ," .--.; | |   | |  |/ '   .   . |:   ' |  '   ;   /|;  : |     `----.   \|   :    ||   | |  |/  
   |   | '  ,/ /  /  ,.  | |   | |--'   `---`-'| |:   : :  '   |  / ||  , ;    /  /`--'  / \   \  / |   | |--'   
   ;   : ;--' ;  :   .'   \|   |/       .'__/\_: ||   | :  |   :    | ---'    '--'.     /   `----'  |   |/       
   |   ,/     |  ,     .-./'---'        |   :    :`---'.|   \   \  /            `--'---'            '---'        
   '---'       `--`---'                  \   \  /   `---`    `----'                                              
                                          `--`-'                                                                 """

   print(hang_person)

def winner_picture():
   winner_pic = """ """
   print(winner_pic)


#------------------------- End of Images --------------------------------

# This line runs the program on import of the module
hangperson()


