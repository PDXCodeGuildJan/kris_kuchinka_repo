def main():
   link = LinkedList()
   link.add(4)
   link.add(2)
   link.add(86)
   link.add(4)
   link.add(7)
   print("Current list:", link)
   link.remove(4)
   print("List after first 4 is removed:", link)
   link.remove(4)
   print("List after second 4 is removed:", link)
   print("Success! Attempt to remove a third 4 yielded no crashes!")
   link.remove(4)
   
   # Output of above code:
   # -------------------------
   # Current list: 4 2 86 4 7 
   # List after first 4 is removed: 2 86 4 7 
   # List after second 4 is removed: 2 86 7 
   # Attempt to remove a third 4 yielded no crashes

   def remove(self, number):
      # ------- What needs to happen?
      # Assign variable number to the number you want to remove
      # Point previous number to number after the number being removed
      # Make number to be removed point to nothing 
      # Find the number in the list 


# -----> This is some shorthand of a solution I found online, but it used functions that they had created during the previous part of the tutorial. 
# -----> I can't seem to get my brain thinking this morning, so I will comment out what I see going on in this function
      # First assign the current value to the number passed into the function 
      current = number
      # Set previous to none, because we don't yet know what it's previous number is and will need to assign a value to it while we loop through the list
      previous = None
      # Set the found "flag" to False so that the loop can be exited if nothing is found or if it becomes True then you know you've found the number
      found = False
      # Loop through the list while current number exists and found is still False
      while current and found is False:
         # if current is found than assign it's absolute value to the current variable
         if current == current:
            # since current number is found, set the found flag to True
            found = True
         # if the number is not found
         else:
            # set the previous variable to be the value of current, thus starting to move through the list
            previous = current
            # then set the current value variable to the value of the next number in the line
            current = current.next
      # This loop is how we find the number we are looking for. It changes variable values by progressing through, looking for a match to the number that we want to remove starting at the beginning of the list. If the first number in the list is not what you want to remove then assign the previous variable to the value of the current variable, thus moving forward in the list.
      if current is None:
         print("Number is not in the list.")
      if previous is None:
         self.head = current.next
      else: 
         previous.next(current.next)


"""Final Comments: This feels like an absolute and utter failure. And it is. Sometimes we have to fail to learn. I want to get the excuses out of the way-- today I'm tired and was running late. I didn't have the full hour, but clearly I wouldn't have finished the function if I had the full hour. Honestly, I'm going through a really hard time. Now, moving away from the excuses...

   I'm trying not to worry right now, because I feel like I get the concept of what needs to happen, but I can't implement it in Python. I could sit and talk to the Rubber Duck or Tiffany or Patrick and maybe get somewhere, but I don't know how to translate that knowledge into the python language. A HUGE struggle for me in this was not having other functions that I would have implemented, had I started this from scratch. I would love to talk about this with you when you have time.

   I hope you aren't disappointed. I NEVER do good on "pop quizzes". My anxiety takes over, rendering me useless. I feel really embarrassed. Again, I'm sorry.
   """














