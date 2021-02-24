# A box company have hired you to program their customer order system.
# 1. The client has a set of square boxes sizes that they will always produce. 
#    Create a tuple of at least 3 box sizes (hint: this will only be one integer
#    value per box as they are square boxes)
box_sizes = (2,5,7,10)

# 2. print the tuple of box sizes the way you would have printed a list in assignment 3, 
#    by placing the tuple name directly into a print statement
print(box_sizes)

# 3. Print the entire tuple again, this time using a for loop to build the string to be printed.
#    When you print your string, the output should look like this (don’t worry about the trailing
#    comma at the end of the string for now): 10, 20, 30, 40, 50, Decide what you want to place 
#    before the loop, in the loop, and after the loop to achieve the same output
message = ""
for box_size in box_sizes:
    message += str(box_size) + ", "
print(message)

# 4. The client wants output that is easy to read. In your output, how might you ensure there is 
#    a blank line before and after the string is displayed? Adapt the code you wrote in the
#    previous step to achieve the requested output
message = "\n"
for box_size in box_sizes:
    message += str(box_size) + ", "
message += "\n"
print(message)

# 5. The client decides to add a new size to their range of box sizes. Overwrite the tuple so it
#    will contain all the original box sizes plus one more at the end of the tuple. Hint: you 
#    can concatenate the original tuple with the new value, for example: the_tuple = the_tuple + new_value
box_sizes += (11, )

# 6. Create a string to print the tuple to make sure it contains all the original box sizes as well
#    as the new one. Make sure you do the following, storing all of it in the one string variable:
#    a. The string should first state the size of the new box by accessing the correct tuple element, 
#       then state that the original box sizes are about to be listed
#    b. Next, use a for loop to iterate over the slice of the tuple that contains all original box
#       sizes but not the new one – use negative notation to ensure that the slice ends in the right place
#    c. Each loop should add the current element to the string in such a way that they will all 
#       display on individual lines
#    d. Finally, after the loop, display the string variable in a print statement, ensuring that there 
#       is a blank line in the output after the string is displayed
message = "The size of the new box is: " + str(box_sizes[-1])
message += "\nThe original box sizes are about to be listed!"
for box_size in box_sizes[:-1]:
    message += "\n"+str(box_size)
message += "\n"
print(message)

# 7. The client wants to be able to display a list of their available box sizes for their customers. 
#    Use a for loop to do the following:
#    a. The client wants the output to have a line of text introducing the list, and a line after 
#       it that invites orders
#    b. They also want each box size to be displayed on separate lines with a message, for example 
#       “10 inches square”
#    c. Again, make sure the output has a space after it so any future output will be separated from
#       it by a blank line
message = "Hello! This is a list of our available box sizes:"
for box_size in box_sizes:
    message += "\n"+str(box_size)+" inches square"
message += "\nWe welcome all orders, big or small!\n"
print(message)

# 8. The client wants a list of volumes for their box sizes. Use a for loop to create a list of box 
#    volumes using the tuple of box sizes. Make sure it works before moving on to the next step!
#box_volumes = []
#for box_size in box_sizes:
#   box_volumes.append(box_size**3)
#print(box_volumes)

# 9. “Comment out” the for loop you created in step 8, and use a list comprehension to do the same thing
box_volumes = [box_size**3 for box_size in box_sizes]
#print(box_volumes)

# 10. Finally, write a for loop that iterates over the list of box volumes and displays a message on each 
#     iteration. Make sure you use the tuple of box sizes to get the correct box size for the volume, don’t 
#     try and “hard code” it! You should use the index() method from slide 43. Each iteration should 
#     produce output similar to the following: The volume of a 10-inch square box is 1000 cubic inches.
for box_volume in box_volumes:
    print(
            f"The volume of a {box_sizes[box_volumes.index(box_volume)]}"
            f"-inch box is {box_volume} cubic inches."
        )