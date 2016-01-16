# Created by: Kris Kuchinka
# Creation Date: 2015.01.13
# Last Date Modified: 2015.01.14

#----->
# Assignment at PDX Code Guild
# Instructor: Tiffany
#----------
# Create a "selection sort" algorithm using python
# The goal is to feed the algorithm numbers and have it do the following:
# 	>>>>>find the smallest number and move it the first position,
#	swapping what was in the first position to wherever the 
#	the current smallest number (now in index 0) was originally 
#	located
#	>>>>>find the second smallest item and move it to the 2nd position, 
#	swapping what was in the 2nd position to wherever it came from
#   >>>>>repeat until you reach the end of the list
# This is a description of what a selection sort algorithm does
#----------

#----->
# First, use basic English and explain the algorithm (i.e. the pattern) in a way that a computer can understand (the computer just wants to be told what to
# do and the process and order to do it in)
#----------
# Processes of Selection Sort Algorithm:
# Given an unsorted list of numbers:
#	>>>>> find the smallest number in the list
#	>>>>> exchange the position of the smallest number with the first 
#		  number in the unsorted list
#   >>>>> update the position of the first number in the unsorted list to be the 
#		  next number in the unsorted list
#	>>>>> repeat the process until unordered list is empty 
#----------

#----->
# My step by step solution: (in pseudocode)
#----------

#----------

#----->
# List of probable variables that will be needed:
#----------

#----------
##############################################################################
#--- Tiffany said this was "gold" and the most "Pythonic way using Python
#--- to do the heavy lifting in the min function, as well as index locator.
def main():
	numbers = [22, 99, 47, -33, 29, 57, 1, 2, 3]
	print("\nUnsorted List: {}".format(numbers))
	print("The following numbers are sorted by my selection_sort_easy function:")
	# "{}".format will fill curly bracket with info following .format function
	print("{}\n".format(selection_sort_easy(numbers)))

	numbers_2 = [47, 0, -2, 100, -100, 58, 1, 2, 3, 500]
	# "Harder" selection sort print out
	print("\nUnsorted List: {}".format(numbers_2))
	print("\nThe numbers were sorted by my selection_sort function:")
	print("{}\n".format(selection_sort(numbers_2)))


def selection_sort_easy(numbers):

	# user would add the desired numbers for sorting to the list variable full_list

	i = 0
	length = len(numbers)
	while i < length:
		# find the smallest number
		small_num = min(numbers[i:])
		# find the smallest number
		# find the index location of the smallest number
		small_num_pos = numbers.index(small_num)
		# swap out index locations between current i and smallest number index
		numbers[i], numbers[small_num_pos] = numbers[small_num_pos], numbers[i]
		# increment index iteration
		i += 1
	return numbers





##############################################################################
#--> is the function that does a selection sort and doesn't let built in functions do the "heavy lifting" for me

def selection_sort(numbers):
	
	# set iteration count to 0 to start at the beginning of the numbers list
	i = 0
	# find the number of values in the numbers variable
	length = len(numbers)
	# if the iteration count is less than the amount of numbers in the list:
	while i < length:
		# There are different variables that represent points that the loop
			# is at. These variables progress and change value during the
			# looping process
		# Variables and what they represent are:
			# low_index--> index location that evaluates and reacts to 
				# cur_index value, that stores where the lowest found num is
			# cur_index--> index location that moves process forward and is 
				# compared to value in location of low_index

		# initiate variables (in this case i=0 (set above), because you are 
			# starting)
		low_index = i
		curr_index = i
		# loop through the current index until it reaches the end of possible
		#	index variables values
		while curr_index < len(numbers):
			# if value of number in lowest index position is greater than 	
			#	the current index....
			if numbers[low_index] > numbers[curr_index]:
				# set the value of the location (index) to the value of the current index location
				# both of these variables are ITERATIONS of the "numbers" list
				low_index = curr_index
				# increment the current_index by one, because the cur_index
				#	moves the process forward
			curr_index += 1

		# swap what is in the i index with what is in the low_index
		holding_chamber = numbers[i]
		numbers[i] = numbers[low_index]
		numbers[low_index] = holding_chamber
		
		i += 1

	return numbers

	

main()











