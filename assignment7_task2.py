# 1. Declare a variable called row_number, assigning the user input to it. 
#    Prompt the user to enter the number of rows for a triangle of numbers 
row_number = int(input("Enter the number of rows for a triangle of numbers: "))

# 2. Declare a variable called number and initialize it to 1 because that 
#    is the number the triangle will start at
number = 1

# 3. Create the outer for loop. The user will give us the number of rows 
#    the triangle will have, so we want to iterate once for each row. 
#    Use the range() method and pass it the row_number variable.
# 4. Now create the inner for loop to control the number of columns. 
#    This time, we want the number of columns to increase by one on each row, 
#    so use the range() method again, but this time pass it the row variable 
#    of the outer for loop and add 1 to the value
# 5. Inside the inner for loop, print the number, and because we want the numbers 
#    to be printed on the same line, specify the end value for the print statement
# 6. Still inside the inner for loop, increment the number variable
# 7. After the inner for loop has exited but still inside the outer for loop, 
#    use a print statement to move to the next line
# 8. *** THIS STEP IS OPTIONAL *** When you try running the code with more 
#    than four rows, you’ll notice the single digit numbers don’t line up neatly 
#    with the double-digit numbers. The numbers should be flat up against the left 
#    side of the triangle, but it would be nice to get the columns of
#    numbers aligned properly. See if you can get the output to match that of the 
#    third output example.
for row in range(row_number):
    for col in range(row+1):
        print(number, end="  " if number < 10 else " ")
        number += 1
    print()