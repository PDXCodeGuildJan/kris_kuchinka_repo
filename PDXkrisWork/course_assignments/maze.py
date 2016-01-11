# Date Started: 2015.01.08
# Created By: Kris Kuchinka
# Assignment at PDX Code Guild
#----------------------------------->

# The object of the Maze Game:
# Create a text-based maze with at least five rooms
# The five rooms can include the start and finish rooms
# The game must handle incorrect decisions politely
# Extra: handle inputs w/out case sensitivity
# Extra Extra: Add a trap
# Extra Extra Extra: Output path taken to the finish (allow
	# user to start over or exit)
#---------------------------------->

# Those are the rules, now let's play a game...

# Basic premise, to be edited later. User wakes up in mysterious lodge
# and doesn't know how they got there or where they are. They can tell
# that there are other structures, but it's foggy, so you can't make
# anything out of it. User must find their way to the parking lot, where 
# a sleek Audi awaits them, waiting to take them to safety.

# Each building at the Dark Moor Pond needs to be it's own function
# Each function has if elifs for movement options
# Each function has a string explanation of the room they are in
# Each function choice should refer and instantiate a different function

#---------------------------------->
def main():
	print (" ")
	print("You never, ever thought it would happen to you, but it did-- you have been abducted and are now waking up in an unknown place. Welcome to Dark Moor Pond.")
	print (" ") 
	print ("There is a way out, but you have to find it on your own. I wanted to play a game. Now you are the player. Your goal is to make it to the parking lot. IF you decide to simply give up and suicide, hit 'q' and the game will be over.")
	print (" ")
	print ("But that's not like you, is it? You want to find your way to the parking lot and you know you can.")
	print (" ")
	print ("It's as simple as that. Then there is an Audi waiting for you, the key is in a magnetic case under the passenger side tire well. You can make it out alive. Until then, enjoy...")
	print (" ")

	lodge()


def lodge():
	print (" ")
	print ("Welcome to the lodge.") 
	print (" ")
	print ("Maybe you have stayed with us before. I'm sure you wouldn't remember, so don't bother...")
	print (" ")
	print ("The point now is to find the parking lot.")
	print (" ")
	print ("In the lodge, you have 3 options to choose from.")
	print ("Option 1 is to head to the door in the forward, left diagnol corner of the Lodge.")
	print ("Option 2 is to head to the door in the forward, right diagnol corner of the Lodge.")
	print ("Option 3 is to head straight forward to the door on the opposite end of the Lodge.")
	print ("Or you can simply type 'q' and give up, but that wouldn't be any fun, now would it?")
	print (" ")
	# set flag to false for correct_answer variable
	correct_answer = False

	while correct_answer == False:
		#list the choices that the user has
		choice = input("Which choice do you choose? Option '1', '2' or '3'?   ")
		# Choice 1 leads to the Kitchen
		if choice == "1":
			correct_answer = True
			print (" ")
			kitchen()
		# Choice 2 leads to the Library
		elif choice == "2":
			correct_answer = True
			print (" ")
			library()
		# Choice 3 leads to the Viewing Deck
		elif choice == "3":
			correct_answer = True
			print (" ")
			viewing_deck()
		# The ultimate out--> they quit:-(
		elif choice == "q":
			correct_answer = True
			print (" ")
			exit()
		# repeat the options
		else:
			correct_answer = False
			print ("You didn't choose one of the 3 options. You didn't even choose to quit. Now you have to start over at the Lodge.")
			lodge()



def kitchen():
	print (" ")
	print ("Welcome to the Kitchen.")
	print (" ")
	print ("I'd like to say that many have shared meals in here, but others have been part of the share, if you know what I'm saying.")
	print (" ")
	print ("In the kitchen you have two options to choose from.")
	print ("Option 1 is to walk through the door to the rear diagnol corner.")
	print ("Option 2 is to walk to the door in the forward right of the room.")

	# set flag to false for correct_answer variable
	correct_answer = False

	while correct_answer == False:
		#list the choices that the user has
		choice = input("Which choice do you choose? Option '1' or '2'?   ")
		# Choice 1 leads to the Lodge
		if choice == "1":
			correct_answer = True
			print (" ")
			print ("It looks like you are headed to a familiar room.")
			lodge()
		# Choice 2 leads to the Library
		elif choice == "2":
			correct_answer = True
			print (" ")
			print ("You are now in a long corridor. The only way is forward. As you move through the door at the end, you find yourself in the library.")
			print (" ")
			library()
		elif choice == "q":
			correct_answer = True
			exit()
		else: 
			correct_answer = False
			print (" ")
			print ("I'm sorry you had only 2 options to choose from. Or you could have chosen to quit the game, but your answer doesn't fit with any of the options you were given. Try again.")
			print (" ")
			kitchen()

def library():
	print (" ")
	print ("Welcome to the Library.")
	print (" ")
	print ("This room is full of so many books, all with so much knowledge to give, but, try as you might, you will not find a map of Dark Moor Pond in here.")
	print (" ")
	print ("You have 3 options to choose from.")
	print ("Option 1 lets you move diagnolly to the left rear.")
	print ("Option 2 makes you move to the left side of the room and through that door.")
	print ("Option 3 means you move diagnolly to the left corner and walk through that doorway.")
	print (" ")


	# set flag to false for correct_answer variable
	correct_answer = False

	while correct_answer == False:
		#list the choices that the user has
		choice = input("Which of the 3 options do you choose from?    ")
		# Choice 1 leads to the Lodge
		if choice == "1":
			correct_answer = True
			print (" ")
			print ("Uh oh! It looks like you are headed back toward where you started...")
			print (" ")
			lodge()
		# Choice 2 leads to the Kitchen
		elif choice == "2":
			correct_answer = True
			print (" ")
			print ("You are now heading back down the corridor that brought you to the kitchen. It's cold in here and you are headed backwards.")
			print (" ")
			kitchen()
		# Choice 3 leads to the Naughty Room
		elif choice == "3":
			correct_answer = True
			print (" ")
			print ("You walk into a dark hallway. Wherever you're headed, it can't be good. The door at the end of the hallway creaks open when push on it. You have wandered into the Naughty Room.")
			print (" ")
			naughty_room()
		# Or user can choose to quit
		elif choice == "q":
			correct_answer = True
			exit()
		else:
			print (" ")
			print ("It looks like you didn't choose one of the options that you were given. There were 3 or you could give up. Go ahead and make one of the proper choices.")
			library()



def naughty_room():
	print (" ")
	print ("Welcome to the Naughty Room.")
	print (" ")
	print ("Kids do bad things and sometimes there's no way to stop them. That's why the Naughty Room was created in the early 1800's. The room is soundproof, so don't bother screaming. At least you aren't locked in. You don't have to stay here, if you choose not to do so.")
	print (" ")
	print ("You have 4 options to choose from.")
	print ("Option 1 is the door in the rear right diagnol corner of the room.")
	print ("Option 2 is the door directly in the rear of the room.")
	print ("Option 3 leads to door in the forward left diagnol corner.")
	print ("Option 4 is the door in the forward right diagnol corner.")
	print (" ")

	# set flag to false for correct_answer variable
	correct_answer = False

	while correct_answer == False:
		#list the choices that the user has
		choice = input("Which of the 4 options do you choose from?    ")
		# Option 1 is the Library
		# Option 2 is the Kitchen
		# Option 3 is the Green House
		# Option 4 is the Parking Lot
		# Or the user can quit the game
		# If one of the 5 options is not chosen...




def viewing_deck():
	print ("Welcome to the Viewing Deck.")
def green_house():
	print ("Welcome to the Green House.")
def parking_lot():
	print ("You made it to the parking lot!")




main()