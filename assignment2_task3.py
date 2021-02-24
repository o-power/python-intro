# Why use comments?
# Comments are useful to help you and others understand what a piece of code is for
# or why you chose to code something in a particular way.
# Toggle comments on and off with CTRL+/ on Windows and Command+/ on Mac.

# Constants should be named using uppercase.
# This is important because Python doesn't stop you changing constants
# so the naming convention indicates to the developer that it shouldn't be changed.
MAX_CAPACITY = 30

num_1 = 3
num_2 = 5

# To repeat a string, use the repetition operator
divider = "\n" + "*"*20 + "\n"

# Example 1: using str() to cast a number to a string
print(divider)
print(str(num_1) + " plus " + str(num_2) + " equals " + str(num_1 + num_2))

num_1 = 108
num_2 = 100

# Example 2: using f string
print(divider)
print(f"{num_1} minus {num_2} equals {num_1 - num_2}")

num_1 = 16
num_2 = 0.5

# Example 3: using f string again
print(divider)
print(f"{num_1} multiplied by {num_2} equals {num_1*num_2}")

num_1 = 16
num_2 = 2

# Example 4: using f string again
print(divider)
print(f"{num_1} divided by {num_2} equals {num_1/num_2}")

# Example 5: using floor division operator
print(divider)
print(f"{num_1} divided by {num_2} equals {num_1//num_2}")

num_3 = 498

# Example 6: using two different approaches to formatting strings
print(divider)
print("The number I choose is {}".format(num_3))
print(f"The number I choose is {num_3}")

# Example 7: getting rid of a TypeError
print(divider)
print("This is a number: " + str(num_1) + ", but it's been cast to a string")

num_1 = 0.1
num_2 = 0.2
num_3 = num_1 + num_2

# Example 8: formatting a number in a string
print(divider)
print("{} plus {} equals {:.1f}".format(num_1, num_2, num_3))
print(f"{num_1} plus {num_2} equals {num_3:.1f}")