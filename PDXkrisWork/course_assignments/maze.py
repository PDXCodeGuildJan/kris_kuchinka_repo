# Date Started: 2015.01.08
# Date Finished: 
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
	print ("There is a way out, but you have to find it on your own. This is a cruel game. Now you are the player. Your goal is to make it to the parking lot. IF you decide to simply give up, hit 'q' and the game will be over. But that will mean you lose.")
	print (" ")
	print ("That's not like you, is it? You want to find your way to the parking lot. You CAN do it. You just have to get througha small maze first.")
	print (" ")
	print ("It's as simple as that. Then there is an Audi waiting for you, the key is in a magnetic case under the passenger side tire well. You can make it out alive. You even get to keep the car as a reward. Enjoy the game.")
	print (" ")
	# User starts out in the Lodge
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
	print ("Option 1 is to head to the door in the North-East corner of the Lodge.")
	print ("Option 2 is to head to the door in the South-East corner of the Lodge.")
	print ("Option 3 is to head East to the door on the opposite end of the Lodge.")
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
			print ("You are walking down a long hallway. I wonder where this heads.")
			print (" ")
			kitchen()
		# Choice 2 leads to the Library
		elif choice == "2":
			correct_answer = True
			print (" ")
			print ("This hallway is well lit. You can see the door to the next room at the end. Go ahead and walk through.")
			print (" ")
			library()
		# Choice 3 leads to the Viewing Deck
		elif choice == "3":
			correct_answer = True
			print (" ")
			print ("Do you feel that draft? It's starting to get cold.")
			print (" ")
			viewing_deck()
		# The ultimate out--> they quit:-(
		elif choice == "q":
			correct_answer = True
			print (" ")
			print ("You gave up? I can't believe it. It looks like you lost the game.")
			print (" ")
			exit()
		# Repeat the options
		else:
			correct_answer = False
			print (" ")
			print ("You didn't choose one of the 3 options. You didn't even choose to quit. Now you have to start over at the Lodge.")
			print (" ")
			lodge()



def kitchen():
	print (" ")
	print ("Welcome to the Kitchen.")
	print (" ")
	print ("Many have shared meals in here, but others have been part of the share, if you know what I'm saying.")
	print (" ")
	print ("In the kitchen you have two options to choose from.")
	print ("Option 1 is to walk through the South-West door.")
	print ("Option 2 is to walk through the South door.")
	print (" ")

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
			print (" ")
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
			print (" ")
			print ("You gave up? I can't believe it. It looks like you lost the game.")
			print (" ")
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
	print ("This room is full of many books, all with so much knowledge to give, but, try as you might, you will not find a map of Dark Moor Pond in here.")
	print (" ")
	print ("You have 3 options to choose from.")
	print ("Option 1 is the door in the North-West corner of the Library.")
	print ("Option 2 is the door on the North wall.")
	print ("Option 3 is the door in the North-East corner of the room.")
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
			print ("I hope you are hungry. It looks like you're headed towards a snack.")
			print (" ")
			kitchen()
		# Choice 3 leads to the Naughty Room
		elif choice == "3":
			correct_answer = True
			print (" ")
			print ("You walk into a dark hallway. Wherever you're headed, it can't be good. The door at the end of the hallway creaks open when you push on it. You have wandered into the Naughty Room.")
			print (" ")
			naughty_room()
		# Or user can choose to quit
		elif choice == "q":
			correct_answer = True
			print (" ")
			print ("You gave up? I can't believe it. It looks like you lost the game.")
			print (" ")
			exit()
		else:
			print (" ")
			print ("It looks like you didn't choose one of the options that you were given. There were 3 or you could give up. Go ahead and make one of the proper choices.")
			library()



def naughty_room():
	print (" ")
	print ("Welcome to the Naughty Room.")
	print (" ")
	print ("Kids do bad things and sometimes there's no way to stop them. That's why the Naughty Room was created in the early 1800's. The room is soundproof, so don't bother screaming. At least you aren't locked in. You don't have to stay here. The children always did.")
	print (" ")
	print ("You have 4 options to choose from.")
	print ("Option 1 is the door in the South-West corner of the room.")
	print ("Option 2 is the door on the West wall.")
	print ("Option 3 is the door in the North-East corner of the room.")
	print ("Option 4 is the door in the South-East corner of the room.")
	print (" ")

	# set flag to false for correct_answer variable
	correct_answer = False

	while correct_answer == False:
		#list the choices that the user has
		choice = input("Which of the 4 options do you choose from?    ")
		# Option 1 is the Library
		if choice == "1":
			correct_answer = True
			print (" ")
			print ("I think I smell parchment paper.")
			print (" ")
			library()		
		# Option 2 is the Viewing Deck
		elif choice == "2":
			correct_answer = True
			print (" ")
			print ("I hope you brought a jacket. Where you're headed, it's cold and foggy.")
			print (" ")
			viewing_deck()
		# Option 3 is the Green House
		elif choice == "3":
			correct_answer = True
			print (" ")
			print ("You didn't happen to bring a trowel or some potting soil, did you?")
			print (" ")
			green_house()
		# Option 4 is the Parking Lot
		elif choice == "4":
			correct_answer = True
			print (" ")
			print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			print ("I'm getting a good feeling....")
			print (" ")
			parking_lot()
		# Or the user can quit the game
		elif choice == "q":
			correct_answer = True
			print (" ")
			print ("You gave up? I can't believe it. It looks like you lost the game.")
			print (" ")
			exit()
		# If one of the 5 options is not chosen...
		else:
			print (" ")
			print ("Please choose one of the choices you've been given. There are 4 options, but you seem to have chosen an option that does not match the choices you have to make.")
			print(" ")
			naughty_room()


def viewing_deck():
	print (" ")
	print ("Welcome to the Viewing Deck.")
	print (" ")
	print ("You are in the middle of all the buildings. You may be able to tell that from looking around, but it may also be too foggy for you to see past your nose.")
	print (" ")
	print ("You have 2 options to choose from.")
	print ("Option 1 is to head West into the hallway door.")
	print ("Option 2 is to head East, across the deck and into the door you find there.")
	print (" ")

	# set flag to false for correct_answer variable
	correct_answer = False

	while correct_answer == False:
		#list the choices that the user has
		choice = input("Which of the 2 options do you choose from?    ")
		# Option 1 is the Lodge
		if choice == "1":	
			correct_answer = True
			print (" ")
			print ("You may be heading back to a place that has become all too familiar. Keep trying.")
			print (" ")
			lodge()
		# Option 2 is the Naughty Room
		elif choice == "2":
			correct_answer = True
			print (" ")
			print ("Did you do something naughty?")
			print (" ")
			naughty_room()
		elif choice == "q":
			correct_answer = True
			print (" ")
			print ("I have to be honest. I didn't think you'd give up that easily. I guess you just don't get to have that brand new Audi.")
			print (" ")
			exit()
		else:
			print (" ")
			print ("You only have two options here (or you can quit). You didn't supply the proper response for your choice. Try again-- you got this!")
			print (" ")
			viewing_deck()

def green_house():
	print (" ")
	print ("Welcome to the Green House.")
	print (" ")
	print ("A hundred years ago, this was a beautiful place where nature was abundant. Now, the windows are broken, the roof is decrepit. Be careful to not fall through the floor.")
	print (" ")
	print ("You have 2 options to choose from.")
	print ("Option 1 is go to the door in the South-West corner.")
	print ("Option 2 is to choose the door in the South-East corner.")
	print (" ")

	# set flag to false for correct_answer variable
	correct_answer = False

	while correct_answer == False:
		#list the choices that the user has
		choice = input("Which of the 2 options do you choose from?    ")
		# Option 1 is the Naughty Room
		if choice == "1":
			correct_answer = True
			print (" ")
			print ("Somebody must have been misbehaving...")
			print (" ")
			naughty_room()
		# Option 2 is the parking lot
		elif choice == "2":
			correct_answer = True
			print (" ")
			print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			print ("I'm getting a good feeling....")
			print (" ")
			parking_lot()
		# User chooses to quit	
		elif choice == "q":
			correct_answer = True
			print (" ")
			print ("You were only one different decision away from success. It's too bad you gave up.")
			print (" ")
			exit()
		# Improper option is input
		else:
			print (" ")
			print ("It seems that you did not choose between the two possible options supplied to you. Please try again.")
			print (" ")
			green_house()

def parking_lot():
	print ("!!!!!! SUCCESS !!!!!!")
	print ("You made it to the parking lot!")
	print ("Hop in your new car and get the hell out of Dark Moor Pond. You're safe now. Next time, be careful where you wake up...")
	print (" ")
	print (" ")

main()