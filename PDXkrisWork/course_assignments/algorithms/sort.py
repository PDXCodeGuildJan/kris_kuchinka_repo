# Created by: Kris Kuchinka
# Creation Date: 2015.01.13
# Last Date Modified: 2015.01.19

#----->
# Assignment at PDX Code Guild
# Instructor: Tiffany
# Teaching Assistant: Patrick
# Goal: Create a series of sorting algorithms that can be used in later work
#---------

########################################################################################################################################################################
###########--------->>>>>>> Main Function for Testing <<<<<<<---------##############
####################################################################################


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

	numbers_3 = [45, 0, -1, 39, 40]
	print("\n-----> Implementation of my bubble_sort function:")
	print("Unsorted List: {}".format(numbers_3))
	print("Result{}".format(bubble_sort(numbers_3)))
	print("----------")

	numbers_4 = [41, 2, 3, -1, 55, 66, 77, 91, 4]
	print("\n-----> Implementation of my merge_sort function:")
	print("Unsorted List: {}".format(numbers_4))
	print("Result{}".format(merge_sort(numbers_4)))
	print("----------")


########################################################################################################################################################################
##########--------->>>>>>> Swap Function for Algorithm <<<<<<<---------#############
####################################################################################

def swap(chosen_list, index_1, index_2):
	holding = chosen_list[index_1]
	chosen_list[index_1] = chosen_list[index_2]
	chosen_list[index_2] = holding
	return chosen_list


########################################################################################################################################################################
########--------->>>>>>> End Swap Function for Algorithm <<<<<<<---------###########
####################################################################################






########################################################################################################################################################################
###########--------->>>>>>> Selection Sort Algorithm <<<<<<<---------###############
####################################################################################

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

####################################################################################
######################## -----> Coding Attempts <----- #############################
####################################################################################

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


########################################################################################################################################################################
#########--------->>>>>>> End Selection Sort Algorithm <<<<<<<---------#############
####################################################################################



###############################################################################################################################################################################--------->>>>>>> Bubble Sort Algorithm <<<<<<<---------######################
####################################################################################

#----->
# Definition: "Bubble sort is a sorting algorithm that works by repeatedly       # stepping through lists that need to be sorted, comparing each pair of adjacent # items and swapping them if they are in the wrong order. This passing procedure # is repeated until no swaps are required, indicating that the list is sorted.  # Bubble sort gets its name because smaller elements bubble toward the top of 
# the list [Definition found at http://bit.ly/23aM0UA]
#---------

#----->
# Goal: Create a Bubble Sort Algorithm that can be used in the future.
#---------

####################################################################################
######################## -----> Coding Attempts <----- #############################
####################################################################################

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

########################################################################################################################################################################
##########--------->>>>>>> End Bubble Sort Algorithm <<<<<<<---------###############
####################################################################################




###############################################################################################################################################################################--------->>>>>>> Merge Sort Algorithm <<<<<<<---------#######################
####################################################################################

#----->
# Definition: 
# Given two lists, merge them together into a third list which is sorted.
#---------

#----->
# Goal: Create a Merge Sort Algorithm that can be used in the future.
#---------

####################################################################################
######################## -----> Coding Attempts <----- #############################
####################################################################################


# define the merger sort function and feed it the parameter of a given list
def merge_sort(given_list):
	"""Implement the merge sort algorithm"""
	# Split the list into two halves, if more than 1 unit
	# If the length of the parameter fed to the function is greater than 1...
	if len(given_list) > 1:
		# initialize index variables for start, end and middle
		start = 0
		# the end of index location is the same as the total length of the given_list parameter
		end = len(given_list)
		# to find the middle index value, divide the given_list parameter by integer value of 2
		mid = len(given_list) // 2
		# separate into two lists and assign them values....
		# first_sorted variable is the list that spans from the start of the list to the middle, which is established above
		# second_sorted variable is the list that spans from the middle (established above) to the end, which is also established above
		first_sorted, second_sorted = given_list[start:mid], given_list[mid:end]
		# first_sorted = Sort the first half using merge_sort
		# the merge sort function helps find the first_sorted list using merge_sort function recursively
		first_sorted = merge_sort(first_sorted)
		# second_sorted = Sort the second half using merge_sort function recursively
		second_sorted = merge_sort(second_sorted)
		#	Merge the two sorted halves back together into a merged list called given list. The merge function takes two parameters and is defined below
		given_list = merge(first_sorted, second_sorted)
	
	# After using the merge function and putting the first and second sorted lists together, put them into the variable "given_list" (refer to above) and return it
	return given_list
		
# create a merge function that takes two lists and puts them together in proper order. Parameters are list_1 and list_2
def merge(list_1, list_2):
	""" Given two lists, merge them together into a third list, which is sorted."""
	# set the value of the index number for the first list
	index_1 = 0
	# set the value of the index number for the second list
	index_2 = 0
	# set the value of the index destination
	index_destination = 0
	# find the length of first list parameter and assign it to a variable
	length_1 = len(list_1)
	# find the length of the second list parameter and asssign it to a variable
	length_2 = len(list_2)
	# assign a variable to the final list. It needs to have a value (which is none-- still a  value, but not 0 or null) and multiply it by the length_1 and length_2 sum
	list_destination = [None] * (length_1 + length_2)

	# loop while the following condition consists: index_1 is less than length_1 AND index 2 is less than length_2
	while index_1 < length_1 and index_2 < length_2:
		# if the index value of list 1 (which is set to 0 originally) is less than the index value at index_2 of list_2 (which is also originally set to 0) do the following:
		if list_1[index_1] < list_2[index_2]:
			# assign the value of the number in the index location of the first list and put it in the the final list that is being compiled in the first index location (which is set at 0)
			list_destination[index_destination] = list_1[index_1] 
			# increment the index value of index_destination so that the next number does not overwrite the same value as the previous one
			index_destination += 1
			# increment the quantity of the index location for the first list to move through the list and not repeat values 
			index_1 += 1
		else:
			# if the value of index_2 for list_2 is less than list_1[index_1]:
			list_destination[index_destination] = list_2[index_2]
			# increment index_destination to put the value into the proper part of the final list
			index_destination += 1
			# increment the value of index location 2 so that the list can continue to be moved forward and through as it is compared to the other
			index_2 += 1 

	# 
	while index_1 < length_1:
		list_destination[index_destination] = list_1[index_1]
		index_destination += 1
		index_1 += 1 

	while index_2 < length_2:
		list_destination[index_destination] = list_2[index_2]
		index_destination += 1
		index_2 += 1 

	return list_destination

########################################################################################################################################################################
##########--------->>>>>>> End Merge Sort Algorithm <<<<<<<---------################
####################################################################################


#----->
# Call Main Function to run program testing of different sorting algorithms. Def # Main is at the top of this file
#---------
# Only run when file is called specifically (use if conditional)
if __name__ == "__main__":
	main()












