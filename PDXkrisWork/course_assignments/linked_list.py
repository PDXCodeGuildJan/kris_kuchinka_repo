""" 
Creating/Implementing a Linked List
Created By: Kris Kuchinka
Created On: 2015.02.11
Last Modified:

This is a part of an assignment at Code Guild
"""

class Node():
	"""This is a class that defines a node."""

	def __init__(self, value):
		self.value = value
		self.next_node = None

	def __str__(self):
		return str(self.value)



class Linked_List():
	"""This is a class that defines a linked list."""

	def __init__(self):
		self.head = None

	def search(self, value):
		"""Search through linked list to find a value"""
		pass

	def add(self, value):
		"""Add a Node to the end of Linked_List"""
		# Create node to be added to the list
		new_node = Node(value)

		# Find the end of the list
		if self.head == None:
			self.head = new_node
		else:
			current_node = self.head		
			while current_node.next_node != None:
				current_node = current_node.next_node

			# Add to the end of the list
			current_node.next_node = new_node
	
	def remove(self, value):
		"""Select a node to remove from Linked List. Re-link new list"""
		pass


	def __str__(self):
		"""String-ify the whole list so it prints oh so pretty."""
		temp_list = []
		current_node = self.head

		while current_node:
			temp_list.append(current_node.value)
			current_node = current_node.next_node
			
		return str(temp_list)


