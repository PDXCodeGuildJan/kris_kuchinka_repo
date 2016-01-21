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
	unsorted_list = ["E", "Z", "L", "O", "B", "F", "G", "X", "Y", "M", "N"]
	target_value = "X"

	# Call the search function, catch what it returns (tuple)
	sorted_list, target_index = binary_search(unsorted_list, target_value)

	# Print out our solutions
	print("I found", target_value, ". It's at ", target_index)

def binary_search(the_list, target_value):
	"""Implements the Binary Search algorithm"""

	# Sort the list using our own sort algorithm (imported above)
	sorted_list = bubble_sort(the_list)

	# Search for the target value
	
	# Find length of current segment 
	length = len(sorted_list)
	
	# initialize start and end variables
	start = 0
	end = length
	# Determine if middle value is >, <, ==

	# If length >= 1, look for the target:
	while length >= 1:

		# Find the  current middle point of the segment of the list 
		mid = start + (length // 2)

		# If it equals the sought after number, number is found, return middle
		if sorted_list[mid] == target_value:
			return (sorted_list, mid)
		# If greater than, reduce segment to left of middle point, repeat loop
		elif sorted_list[mid] > target_value:
			end = mid

		# If less than, reduce segment to right of middle point, repeat loop
		elif sorted_list[mid] < target_value:
			start = mid + 1

		# Find the current length of the string
		length = len(sorted_list[start:end])



	# If we can't find the index, return -1
	return (sorted_list, -1)



#----->
# Call Main Function to run program testing of different sorting algorithms. Def # Main is at the top of this file
#---------
# Only run when file is called specifically (use if conditional)
if __name__ == "__main__":
	main()


