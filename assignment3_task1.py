# b. Create a list called names and assign at least three names to it at the same time
names = ['Chico','Harpo','Groucho']

# c. Print the list
print(names)

# d. Add at least two new names to the list, using append() and insert()
names.append('Laurel')
names.insert(0,'Hardy')
print(names)

# e. Print each name in the list (EXCEPT THE LAST ONE) one at a time by accessing the elements individually
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# f. Now you need to print the last name. This time, use len() to get the length of the list,
#    and modify that number to make sure you don’t get an index error
print(names[len(names)-1])

# g. Use negative notation to assign a new name to the second to last element in the list
names[-2] = 'Morecambe'
print(names)

# h. Create and print an f-string that uses len() in the f-string to state the number of
#    elements in the list, and then prints the first element and two other elements as part of the same f-string
message = f'There are {len(names)} items in the list.\nThe first one is {names[0]}.\nAnother two are {names[1]} and {names[2]}.'
print(message)

# i. Use pop() to remove the third element in the list, storing it in a variable
name = names.pop(2)

# j. Print the removed name in an f-string as part of a message. 
#    In the same f-string, also print the list to show what names are left in it
print(f'{name} was popped! The list is now {names}.')

# k. Choose one of the remaining names and use remove() to remove it from the list.
#    As before, after the name has been removed from the list, print it as part of
#    an f-string message along with the rest of the list to demonstrate that it is no longer in the list
name = 'Morecambe'
names.remove(name)
print(f'{name} was removed! The list is now {names}.')

# l. Use the del keyword to delete the list
del names

# m. To confirm that the list has been deleted, attempt to print it out. Use comments to explain in your own words what happens
print(names)
# NameError: name 'names' is not defined
# We get the error above as there is now no object called names.