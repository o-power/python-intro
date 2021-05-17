# Question 1
# print("Question 1")
# serial_number = ""
# sections = ""

# while not serial_number:
#     valid = False
#     serial_number = input("Enter serial number (ddd-dd-dddd): ")
#     sections = serial_number.split("-")

#     if len(sections) == 3:
#         if len(sections[0]) == 3 and len(sections[1]) == 2 and len(sections[2]) == 4:
#             if sections[0].isdigit() and sections[1].isdigit() and sections[2].isdigit():
#                 valid = True
#     print(valid)

# Question 2
# print("Question 2")
# def get_root(a, b):
#     if a >= 0:
#         result = a**(1/b)
#     else:
#         result = -(-a)**(1/b)
#         if a % 2 == 0:
#             result = "Result is an imaginary number"
    
#     return result

# print(get_root(4,2))
# print(get_root(-9,2))
# print(get_root(-4,2))

# Question 6
# Prime numbers are numbers that have only 2 factors: 1 and themselves
# num = 2
# while num <= 100:
#     is_prime_number = True

#     for i in range(2, num):
#         if num % i == 0:
#             is_prime_number = False
#             break
    
#     if is_prime_number == True:
#         print(num)
    
#     num += 1

# Question 8
# print((3 + (4/2)) + 5)

# Question 10
# rooms = {1: 'Dining Room', 2: 'Function Room with Bar'}
# room = int(input('Enter the room number: '))
# if not room in rooms:
#     print('The room does not exist.')
# else:
#     print('You have chosen the '+rooms[room])

# Question 11
# x = "20"
# y = 3
# a = x * y
# print(a)
# print(type(a)) # string 2020202

# x = 6
# y = 3
# a = x/y
# print(a)
# print(type(a)) # float

# x = 2.5
# y = 1
# a = x/y
# print(a)
# print(type(a)) # float

# Question 12
# print(type(+21E11)) # float
# print(+21e11)
# print(type(0.0)) # float
# print(type("False")) # str
# print(type(True)) # bool

# Question 14
# print("sunday".capitalize())

# Question 18
# numList = [1,2,3,4,5]
# alphaList = ['a','b','c','d','e']

# print(numList is alphaList) # False
# print(numList == alphaList) # False

# numList = alphaList

# print(numList is alphaList) # True
# print(numList == alphaList) # True

# Question 19
# a = 11
# b = 4
# print(a/b) # 2.75
# print(a//b) # 2
# print(a%b) # 3

# Question 20
# x = eval(input("Enter a number for the equation: "))
# y = (-x)**4

# Question 21
# print(2*(3+3)**2 - (4**2)*2)

# Question 22
# import random
# import string

# def get_random_string(length):
#     """Returns a random lowercase string of the given length."""
#     letters = string.ascii_lowercase
#     result_str = ''.join(random.choice(letters) for i in range(length))
#     #print("Random string of length", length, "is:", result_str)
#     return result_str

# serial_numbers = [get_random_string(5) for i in range(50)]
# print(serial_numbers[:])
# print(serial_numbers[:-5])

# Question 26
# randint(start,stop) is an alias for randrange(start, stop+1).

# Question 27
# import os
# def get_first_line(filename, mode):
#     if os.path.isfile(filename):
#         with open(filename, 'r') as file:
#             return file.readline()
#     else:
#         return None

# print(get_first_line('words.txt','r'))

# Question 28
# numbers = open('numbers.txt','r')
# eof_flag = False
# while not eof_flag:
#     line = numbers.readline()
#     #print(f"Line: {line}")
#     if line != '':
#         if line != "\n":
#             print(line, sep='')
#     else:
#         print("End of file")
#         eof_flag = True
#         numbers.close()

# Question 35
# import sys
# try:
#     readf = open('read.txt','r')
#     writef = open('write.txt','w')
# except IOError:
#     print('cannot open the file', f_name)
# else:
#     count = 1
#     for line in readf:
#         print(line.rstrip())
#         writef.write('line' + str(count) + ': ' + line)
#         count += 1
#     readf.close()
#     writef.close()
