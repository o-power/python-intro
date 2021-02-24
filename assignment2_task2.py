num_1 = 3
num_2 = 5

divider = "\n" + "*"*20 + "\n"

print(divider)
#print("{} plus {} equals {}".format(num_1, num_2, num_1 + num_2))
#print("{0} plus {1} equals {2}".format(num_1, num_2, num_1 + num_2))
#print(f"{num_1} plus {num_2} equals {num_1 + num_2}")
print(str(num_1) + " plus " + str(num_2) + " equals " + str(num_1 + num_2))

num_1 = 108
num_2 = 100

print(divider)
print(f"{num_1} minus {num_2} equals {num_1 - num_2}")

num_1 = 16
num_2 = 0.5

print(divider)
print(f"{num_1} multiplied by {num_2} equals {num_1*num_2}")

num_1 = 16
num_2 = 2

print(divider)
print(f"{num_1} divided by {num_2} equals {num_1/num_2}")

print(divider)
print(f"{num_1} divided by {num_2} equals {num_1//num_2}")

num_3 = 498

print(divider)
print("The number I choose is {}".format(num_3))
print(f"The number I choose is {num_3}")

print(divider)
#print("This is a number: " + num_1 + ", but it's been cast to a string")
#TypeError: can only concatenate str (not "int") to str
print("This is a number: " + str(num_1) + ", but it's been cast to a string")

num_1 = 0.1
num_2 = 0.2
num_3 = num_1 + num_2

print(divider)
print("{} plus {} equals {:.1f}".format(num_1, num_2, num_3))
