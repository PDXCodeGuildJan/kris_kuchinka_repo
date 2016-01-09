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

# First, list out the functions line by line
def lodge():
	print("Welcome to the lodge. Maybe you have stayed with us before. I'm sure you wouldn't remember, so don't bother...")
	print("In the lodge, you have 3 options to choose from.")
	print("Option 1 is to head to the door in the forward, left diagnol corner of the Lodge.")
	print("Option 2 is to head to the door in the forward, right diagnol corner of the Lodge.")
	print("Option 3 is to head straight forward to the door on the opposite end of the Lodge.")
	print("Or you can simply type 'q' and give up, but that wouldn't be any fun, now would it?")
	choice = input("Which choice do you choose? Option 1, 2 or 3?   ")
	# Choice 1 leads to the Kitchen
	if choice == "1":
		kitchen()
	# Choice 2 leads to the Library
	elif choice == "2":
		library()
	# Choice 3 leads to the Viewing Deck
	elif choice == "3":
		viewing_deck()
	# The ultimate out--> they quit:-(
	elif choice == "q":
		exit()
	# repeat the options
	else:
		lodge()

lodge()


def kitchen():
	print("Welcome to the Kitchen.")
def library():
	print("Welcome to the Library.")
def naughty_room():
	print("Welcome to the Naughty Room.")
def viewing_deck():
	print("Welcome to the Viewing Deck.")
def green_house():
	print("Welcome to the Green House.")
def parking_lot():
	print("You made it to the parking lot!")


def main():
	print("Welcome message to be placed here...")

	