# A dealership stocks cars from different manufacturers. 
# They have asked you to write a program to manage the different manufacturers they stock.

# a. Create an appropriately named list and populate it with at least 10 manufacturers, 
#    making sure you don’t add them in alphabetical order
manufacturers = ['Nissan','Skoda','Volkswagen','Toyota','Hyundai','Honda'
                ,'Ford','Lada','Ferrari','Dacia','Volvo','Fiat','Isuzu','Rover']

# b. Display the entire list in one go using the sorted() method
print(sorted(manufacturers))

# c. Display the entire list again for comparison, this time without calling any methods on it
print(manufacturers)

# d. Display the list in reverse. Note that the list is only to be reversed, not sorted
manufacturers.reverse()
print(f'Reversed list: {manufacturers}')
manufacturers.reverse()

# e. The dealership wants a “live” backup copy of their list, create a backup list that
#    updates with any changes made to the original list
manufacturers_backup = manufacturers

# f. To test the backup list, add a new manufacturer to the original list, then display the
#    backup list to confirm that it reflects the changes to the original list
manufacturers.append('Aston Martin')
print(manufacturers_backup)

# g. The dealership also wants a copy of the original list that they can manipulate without 
#    changing the original list. Make a copy of the entire list
manufacturers_copy = manufacturers[:]

# h. Permanently sort the new copy of the list, then display it and the original list using 
#    the same print statement, but make sure the two lists print on different lines. 
#    This is to allow you to compare the two lists, confirming the original list wasn’t modified along with the copy
manufacturers_copy.sort()
print(f'Sorted copy: {manufacturers_copy}')
print(f'Original list: {manufacturers}')

# i. The dealership decide they want three subsets of the sorted list. Slice the sorted 
#    list into three alphabetically grouped lists, for example A to H, I to Q, R to Z
# method 1
a_to_h = manufacturers_copy[:7]
i_to_q = manufacturers_copy[7:10]
r_to_z = manufacturers_copy[10:]
#print(a_to_h)
#print(i_to_q)
#print(r_to_z)

# method 2
a_to_h = []
i_to_q = []
r_to_z = []
for manufacturer in manufacturers_copy:
    if manufacturer[0].lower() < 'i':
        a_to_h.append(manufacturer)
    elif manufacturer[0].lower() < 'r':
        i_to_q.append(manufacturer)
    else:
        r_to_z.append(manufacturer)

# print(a_to_h)
# print(i_to_q)
# print(r_to_z)

# j. Display the three subset lists as part of a formatted string. If you think the output is too messy,
#    try using whitespace character combinations to make it more readable. Note: if your VS Code terminal 
#    is getting too cluttered, click in the terminal and type clear, then press enter. This will give you a clear area in your terminal
print(f'\nA to Z: {a_to_h}\nI to Q: {i_to_q}\nR to Z: {r_to_z}')