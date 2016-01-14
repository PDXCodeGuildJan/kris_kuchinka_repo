# Created by: Kris Kuchinka
# Creation Date: 2015.01.13
# Last Date Modified:

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
# First use basic English and explain the algorithm (ie the pattern) in a way that a 
# computer can understand (the computer just wants to be told what to
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
# My step by step solution: (in quazi-pseudocode)
#----------
# Name a function "selection_sort" and feed the function a list of numbers
#	>>>>> make the list a variable called "list_feed"
# Once the list is established and fed to the function, it is time to create two more variables
#   >>>>> variable called "unsorted_list" (refer below for uses)
#	>>>>> variable called "sorted_list" (refer below for uses)

#----------

#----->
# List of probable variables that will be needed:
#----------
#	>>>>> list_feed (list variable to be passed as argument to the 
#	selection_sort function)
#	>>>>> unsorted_list (pass the list value of list_feed into this variable)
#   >>>>> sorte