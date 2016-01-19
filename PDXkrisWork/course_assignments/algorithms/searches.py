# Created by: Kris Kuchinka
# Creation Date: 2015.01.19
# Last Date Modified: 2015.01.19

#----->
# Assignment at PDX Code Guild
# Instructor: Tiffany
# Goal: Create a binary search algorithm
# Class Exercise
#---------

from sort import bubble_sort

def main():
	unsorted_list = ["E", "Z", "L", "O", "B", "F"]
	target_value = "B"

	# Call the search function, catch what it returns (tuple)
	sorted_list, target_index = binary_search(unsorted_list, target_value)

	# Print out our solutions
	# print("I found", target_value, ". It's at, " target_index)

def binary_search(the_list, target_value):
	"""Implements the Binary Search algorithm"""

	# sort the list using our own sort algorithm (imported above)
	sorted_list = bubble_sort(unsorted_list)
	print(sorted_list)


