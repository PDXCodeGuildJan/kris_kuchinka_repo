# Created by: Kris Kuchinka
# Creation Date: 2015.01.13
# Last Date Modified: 2015.01.18

#----->
# Assignment at PDX Code Guild
# Instructor: Tiffany
# Teaching Assistant: Patrick
# Goal: Create a series of sorting algorithms that can be used in later work
#---------

##################################################################################################################################################################
###########--------->>>>>>> Main Function for Testing <<<<<<<---------###########
#################################################################################


def main():
	numbers = [0, -2, -4, -192, 192, 47, 38, 99, 100]
	print("\n-----> Implementation of selection_sort_easy function:")
	print("Unsorted List: {}".format(numbers))
	# "{}".format will fill curly bracket with info following .format function
	print("Result:{}".format(selection_sort_easy(numbers)))
	print("----------")

	numbers_2 = [47, 0, -2, -98, 48, 49, 20, 30, 500]
	# "Harder" selection sort print out
	print("\n-----> Implementation of my selection_sort function:")
	print("Unsorted List: {}".format(numbers_2))
	print("Result{}".format(selection_sort(numbers_2)))
	print("----------")

	numbers_3 =[45, 0, -1, 39, 40]
	print("\n-----> Implementation of my bubble_sort function:")
	print("Unsorted List: {}".format(numbers_3))
	print("Result{}".format(bubble_sort(numbers_3)))
	print("----------")



##################################################################################################################################################################
##########--------->>>>>>> Swap Function for Algorithm <<<<<<<---------##########
#################################################################################

def swap(chosen_list, index_1, index_2):
	holding = chosen_list[index_1]
	chosen_list[index_1] = chosen_list[index_2]
	chosen_list[index_2] = holding
	return chosen_list


##################################################################################################################################################################
########--------->>>>>>> End Swap Function for Algorithm <<<<<<<---------########
#################################################################################






##################################################################################################################################################################
###########--------->>>>>>> Selection Sort Algorithm <<<<<<<---------############
#################################################################################

#----->
# Definition: "the selection sort algorithm starts by finding the minimum value
# in the array and moving it to the first position. This step is then repeated
# for the second lowest value, then the third, and so on until the array is 
# sorted." [Definition found at http://che.gg/1RPLeZO]
#---------

#----->
# Goal: Create a Selection Sort Algorithm that can be used in the future. Follow # the process that Tiffany has asked us to follow, so to learn the proper way to # approach these problems.
#---------

#----->
# First: use basic English and explain the algorithm (i.e. the pattern) in a way that a computer can understand (the computer just wants to be told what to
# do and the process and order to do it in)
#---------
# Processes of Selection Sort Algorithm:
# Given an unsorted list of numbers:
#	>>>>> find the smallest number in the list
#	>>>>> exchange the position of the smallest number with the first 
#		  number in the unsorted list
#   >>>>> update the position of the first number in the unsorted list to be the 
#		  next number in the unsorted list
#	>>>>> repeat the process until unordered list is empty 
#---------

##############################################################################
######################## -----> Coding Attempts <----- #######################
##############################################################################

#----->
# Tiffany said this was "gold" and the most "Pythonic way using Python to do the # "heavy lifting" by using the min function, as well as index locator. She asked # me to rename it to selections_sort_easy and then to try again, this time 
# finding programatic ways to accomplish the processes

# She said that this was the way we would be doings things in two weeks and that # she was excited to work with me, based on what she saw below, but that it was # best to do it long form, to enhance my learning experience.
#---------

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

#----->
# Below is my second attempt at the Selection Sort Algorithm, in a more long 
# form way
#---------

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
			#index variables values
		while curr_index < len(numbers):
			# if value of number in lowest index position is greater than 	
			#	the current index....
			if numbers[low_index] > numbers[curr_index]:
				# set the value of the location (index) to the value of the 		#current index location
				# both of these variables are ITERATIONS of the "numbers" list
				low_index = curr_index
				# increment the current_index by one, because the cur_index
					# moves the process forward
			curr_index += 1
		# swap what is in the i index with what is in the low_index
		swap(numbers, i, low_index)

		# holding_chamber = numbers[i]
		# numbers[i] = numbers[low_index]
		# numbers[low_index] = holding_chamber
		
		i += 1

	return numbers

#----->
# Note: 
#---------


##################################################################################################################################################################
#########--------->>>>>>> End Selection Sort Algorithm <<<<<<<---------##########
#################################################################################



###############################################################################################################################################################################--------->>>>>>> Bubble Sort Algorithm <<<<<<<---------#############
#################################################################################

#----->
# Definition: "Bubble sort is a sorting algorithm that works by repeatedly       # stepping through lists that need to be sorted, comparing each pair of adjacent # items and swapping them if they are in the wrong order. This passing procedure # is repeated until no swaps are required, indicating that the list is sorted.  # Bubble sort gets its name because smaller elements bubble toward the top of 
# the list [Definition found at http://bit.ly/23aM0UA]
#---------

#----->
# Goal: Create a Bubble Sort Algorithm that can be used in the future. Follow   # the process that Tiffany has asked us to follow, so to learn the proper way to # approach these problems.
#---------

#----->
# First: use basic English and explain the algorithm (i.e. the pattern) in a way that a computer can understand (the computer just wants to be told what to
# do and the process and order to do it in)
#---------
# Processes of Bubble Sort Algorithm:
# Given an unsorted list of numbers:
#	>>>>> 
#---------

##############################################################################
######################## -----> Coding Attempts <----- #######################
##############################################################################

def bubble_sort(current_list):
	length_unsorted = len(current_list)
	while length_unsorted > 1:
		i = 0
		while i < length_unsorted - 1:
			if current_list[i] > current_list [i + 1]:
				current_list = swap(current_list, i, i+1)
			i += 1
		length_unsorted -= 1
	return current_list








#----->
# Call Main Function to run program testing of different sorting algorithms. Def # Main is at the top of this file
#---------
main()











