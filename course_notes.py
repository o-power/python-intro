# ====== Lesson 1 ======
print("*"*20, "Lesson 1", "*"*20)

# The pydoc module automatically generates documentation about Python.
# To start the Python REPL:
# $ python
# >>> help("input")
# Type q to quit.
# $ python -m pydoc input
# >>> help()
# Type quit to exit help.
# Type quit() to exit the Python REPL.

# when we assign a new value to a variable, we change the memory location that the variable references
age = 40
print(f'id: {id(age)}') # memory address
print(f'type: {type(age)}')
print(f'value: {age}\n')

age = 44
print(f'id: {id(age)}') # age now points to a new memory location
print(f'type: {type(age)}')
print(f'value: {age}\n')

# y is x returns True is y and x point to the same memory location e.g.
x = "test"
y = x
print(f"id(x) is: {id(x)}")
print(f"id(y) is: {id(y)}")
print(f"y is x returns: {y is x}") # True
print(f"x is y returns: {x is y}\n") # True

a = "banana"
b = "bananas"
print(f"id(a) is: {id(a)}")
print(f"id(b) is: {id(b)}")
print(f"b is a returns: {b is a}") # False
print(f"a is b returns: {a is b}\n") # False

c = "banana"
d = "banana"
print(f"id(c) is: {id(c)}")
print(f"id(d) is: {id(d)}")
print(f"d is c returns: {d is c}") # True (as string is short)
print(f"c is d returns: {c is d}\n") # True

# ====== Lesson 2 ======
print("*"*20, "Lesson 2", "*"*20)

message = "brown"
print("The",message,"fox.")
print("The "+message+" fox.")
print(f"The {message} fox.")
print("The {} fox.\n".format(message))
print("This is a message.", end = " ")
print("This is a second message.\n")

print(f"{8/4}") # 2.0
print(f"{8/3}") # 2.666
print(f"{8//3}\n") # 2

# big numbers - to help programmer type it in, underscores not displayed
big_number = 75_000_000_000
print(big_number)

# multiple assignments on one line
x, y = 6, 7

# None
print("\nChecking for None")
x = None

if x:
    print("Do you think None is True?")
elif x is False:
    print ("Do you think None is False?")
else:
    print("None is not True, or False, None is just None...")

if x is None:
    print("Check for None using is None\n")

# ====== Lesson 3 ======
print("*"*20, "Lesson 3", "*"*20)

list_1 = [1,2]
list_2 = [3,4]
list_3 = list_1 + list_2
list_4 = list_3*3
print(list_4) # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

# del list_name[item index]
# removed_item = list_name.pop(item index)
# list_name.remove('item value')

# If modifying the sequence you are iterating over while inside the loop
# first make a copy; otherwise the below would be an infinite loop.
words = ['cat','window','defenestrate']
for w in words[:]:
    if len(w) > 6:
        words.insert(0,w)
print(words)

words = ['cat','window','defenestrate']
for x in range(len(words)):
    if len(words[x]) > 6:
        words.insert(0,words[x])
print(words)

# ====== Lesson 4 ======
print("*"*20, "Lesson 4", "*"*20)

# tuples with one item need a comma
my_tuple = (20)
print(type(my_tuple))

my_tuple = (20,)
print(type(my_tuple))

# ====== Lesson 5 ======
print("*"*20, "Lesson 5", "*"*20)

# ====== Lesson 6 ======
print("*"*20, "Lesson 6", "*"*20)

# new_list = [expression for item in iterable if condition == True]

# ====== Lesson 7 ======
print("*"*20, "Lesson 7", "*"*20)

# A key can only occur once in a dictionary.
customer_1 = {}
customer_1['name'] = 'Joe Bloggs'
customer_1['age'] = 24
print(f"Customer 1: {customer_1}")
del customer_1['age']
print(f"Customer 1 (after del): {customer_1}\n")

# clear()
customer_1 = {'name': 'Joe Bloggs', 'age': 24}
print(f"Customer 1: {customer_1}")
customer_1.clear()
print(f"Customer 1 (after .clear()): {customer_1}\n")

# pop()
customer_1 = {'name': 'Joe Bloggs', 'age': 24}
print(f"Customer 1: {customer_1}")
age = customer_1.pop('age')
print(f"Customer 1 (after .pop()): {customer_1}")
print(f"Age: {age}\n")

# popitem()
customer_1 = {'name': 'Joe Bloggs', 'age': 24}
print(f"Customer 1: {customer_1}")
popped_item = customer_1.popitem()
print(f"Customer 1 (after .popitem()): {customer_1}")
print(f"Popped item: {popped_item}\n")

# get()
# Useful to avoid the KeyError error message
customer_1 = {'name': 'Joe Bloggs', 'email': 'joe_bloggs@gmail.com'}
print(f"Customer 1: {customer_1}")
try:
    age = customer_1['age']
except KeyError:
    print("We got a KeyError.")
age = customer_1.get('age',"Unknown")
print(f"Customer 1 (after .get()): {customer_1}")
print(f"Age: {age}\n")

# setdefault()
customer_1 = {'name': 'Joe Bloggs', 'email': 'joe_bloggs@gmail.com'}
print(f"Customer 1: {customer_1}")
age = customer_1.setdefault('age', 'Unknown')
print(f"Customer 1 (after .setdefault()): {customer_1}")
print(f"Age: {age}\n")

# items()
customer_1 = {'name': 'Joe Bloggs', 'email': 'joe_bloggs@gmail.com'}
print(f"Customer 1: {customer_1}")
customer_items = customer_1.items()
print("items():")
print(customer_items)
print(type(customer_1))
print(type(customer_items)) # a view object which changes when the dictionary changes
print()

# keys()
customer_1 = {'name': 'Joe Bloggs', 'email': 'joe_bloggs@gmail.com'}
print(f"Customer 1: {customer_1}")
customer_keys = customer_1.keys()
print("keys():")
print(customer_keys)
print(type(customer_1))
print(type(customer_keys))
print()

# values()
customer_1 = {'name': 'Joe Bloggs', 'email': 'joe.bloggs@gmail.com', 'email2': 'joe.bloggs@gmail.com'}
print(f"Customer 1: {customer_1}")
customer_values = customer_1.values()
print("values():")
print(customer_values)
print(type(customer_1))
print(type(customer_values))
print()

# Loops
print(customer_1)
for key, value in customer_1.items():
    print(f"Key:Value {key}:{value}")

print()
for key in customer_1:
    print(f"Key {key}")
    print(f"customer_1[Key]: {customer_1[key]}")

print()
for key in customer_1.keys():
    print(f"Key {key}")

print()
for key in sorted(customer_1.keys()):
    print(f"Key {key}")

print()
for value in customer_1.values():
    print(f"Value {value}")

print()
for value in set(customer_1.values()):
    print(f"Value {value}\n")

# ====== Lesson 8 ======
print("*"*20, "Lesson 8", "*"*20)

pets = ['cat','dog','fish','dog','rabbit']
print(pets)
while 'dog' in pets:
    pets.remove('dog')
print(pets)

print()
for num in range(4):
    print(num)
print()

my_list = []
for num in range(1,11):
    my_list.append(num)
print(my_list)

my_list = [num for num in range(1,11)]
print(my_list)

# ====== Lesson 9 ======
print("*"*20, "Lesson 9", "*"*20)

print(f'19 % 12 = {19%12}')
print(f'-19 % 12 = {19%12}')
# https://rob.conery.io/2018/08/21/mod-and-remainder-are-not-the-same/#:~:text=When%20you%20%E2%80%9Cmod%E2%80%9D%20something%2C,%3A%205%20%25%202%20%3D%201%20

def print_toppings(*toppings):
    """Demo of arbitrary argument lists.

    This just shows that the arbitrary arguments
    are put into a tuple.
    """
    print(toppings)

print_toppings("cheese", "mushrooms", "mozzarella")
print_toppings() # prints an empty tuple

def concat(*args, sep="/"):
    return sep.join(args)

print(concat('C','Documents','Folder'))

def cheeseshop(kind, *args, **kwargs):
    """Demo of arbitrary arguments and arbitrary keyword arguments.
    
    Keyword arguments are put into a dictionary.
    """
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in args:
        print(arg)
    print("-" * 40)
    for kw in kwargs:
        print(kw, ":", kwargs[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# When we use keyword arguments:
# 1. We can often leave out arguments that have default values
# 2. We can rearrange arguments in a way that makes them most readable
# 3. We call arguments by their names to make it more clear what they represent

# def pet_details(animal, name):
#     """Display a pet's details."""
#     print(f'I have a pet {animal}.')
#     print(f'My animal\'s name is {name}')

# pet_details('cat') # TypeError: pet_details() missing 1 required positional argument: 'name'

def pet_details(animal, name='undecided'):
    """Display a pet's details."""
    print(f'I have a pet {animal}.')
    print(f'My animal\'s name is {name}')

pet_details('cat')

# Equivalent function calls
pet_details('cat','Garfield')
pet_details(animal='cat', name='Garfield')
pet_details(name='Garfield', animal='cat')

# returns "__main__" if script ran as python course_notes.py
# returns "course_notes" if script is imported into another script
# This is often used either to provide a convenient user interface to a module,
#  or for testing purposes (running the module as a script executes a test suite).
print(__name__)

# ====== Lesson 10 ======
print("*"*20, "Lesson 10", "*"*20)

# import math
# print(math.ceil(5.3))

# from math import ceil
# print(ceil(5.3))

# import random as r
# print(r.randrange(5, 9))

# from random import randrange as rr
# print(rr(5, 9))

print("\nShallow versus Deep Copy")
import copy
person_1 = {'name': 'Walter Wall', "age": 35, "email": "walter_wall@gmail.com", "profession": "floorer"}
person_2 = {'name': 'Polly Pocket', 'age': 6, 'email': 'polly_pocket@hotmail.com', 'profession': 'Children\'s Entertainer'}
customers = {1234: person_1, 2345: person_2}
customers_shallow_copy = customers.copy()
customers_deep_copy = copy.deepcopy(customers)
person_1.clear()
print(f"Customers Person 1: \n {customers[1234]}")
print(f"Customers Shallow Copy Person 1: \n {customers_shallow_copy[1234]}")
print(f"Customers Deep Copy Person 1: \n {customers_deep_copy[1234]}")

print("\nstrftime()")
# https://docs.python.org/3/library/datetime.html#module-datetime
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
import datetime as dt

# method strftime of datetime class in module dt
# formatted_dt = dt.datetime.strftime(datetime_object, "format codes")

current_time = dt.datetime.now()
print(f"Unformatted date and time: {current_time}")
formatted_time = dt.datetime.strftime(current_time, "%d/%m/%Y %H:%M:%S")
print(f"Formatted date and time: {formatted_time}")

# method strftime of date class in module dt
# formatted_dt = dt.date.strftime(datetime_object, "format codes")

current_date = dt.date.today()
print(f"Unformatted date: {current_date}")
formatted_date = dt.date.strftime(current_date, "%a, %d %b %y")
print(f"Formatted date: {formatted_date}")

print("\nstrptime()")
# new_datetime_object = dt.datetime.strptime("string to parse", "format codes")

current_date = dt.date.today()
#input_date = input("Enter the date of your deadline in the format dd/mm/yyyy format: ")
input_date = '21/06/2021'
deadline = dt.datetime.strptime(input_date, "%d/%m/%Y")
print(f"Your deadline (datetime): {deadline}")
# convert datetime to date
deadline = deadline.date()
print(f"Your deadline (date): {deadline}")
print(f"You have {(deadline - current_date).days} days until your deadline.")

print("\nmath")
from math import pi, ceil, floor
print(f"Value of pi to 15 d.p. is {pi}")
print(f"pi rounded up to the nearest integer is {ceil(pi)}")
print(f"pi rounded down to the nearest integer is {floor(pi)}")

print("\nrandom")
import random
# generate random numbers from 5 (inclusive) to 10 (exclusive) in steps of 2 e.g. 5, 7, 9
for i in range(5):
    print(random.randrange(5, 10, 2), end=" ")
print()
import random
# generate random numbers from 5 (inclusive) to 8 (inclusive) e.g. 5, 6, 7, 8
for i in range(5):
    print(random.randint(5, 8), end=" ")

my_list = [random.randrange(101) for i in range(10)]
print(f"\nOriginal list:\t{my_list}")
random.shuffle(my_list)
print(f"Shuffled list:\t{my_list}")

# ====== Lesson 11 ======
print("*"*20, "Lesson 11", "*"*20)

import io
file_stream = open('numbers.txt','r')
file_contents = file_stream.read()
print("\nStart of file")
print(file_contents)
print("End of file\n")
file_stream.close()

file_stream = open('numbers.txt','r')
first_line = file_stream.readline()
print(first_line)
second_line = file_stream.readline()
print(second_line)
file_stream.close()

import string
def get_random_string(length):
    """Returns a random lowercase string of the given length."""
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    #print("Random string of length", length, "is:", result_str)
    return result_str
file_stream = open('random_text.txt','w')
#text = input('Enter some text to add to file: ')
text = get_random_string(10)
file_stream.write(text)
file_stream.close()

import os
if os.path.isfile('random_text.txt'):
    file_stream = open('random_text.txt','a')
else:
    file_stream = open('random_text.txt','w')
text = get_random_string(10)
file_stream.write(text)
file_stream.close()

with open('numbers.txt','r') as file_stream:
    file_contents = file_stream.read()
print("\nStart of file")
print(file_contents)
print("End of file\n")

with open('numbers.txt','r') as file_stream:
    file_contents = file_stream.readlines()
print("\nStart of file")
for line in file_contents:
    # use rstrip() as print will add a newline character
    #print(line.rstrip())
    print(line, end='')
print("\nEnd of file\n")

print("Exception Handling\n")
# 1. Syntax Errors
# 2. Logic Errors
# 3. Runtime Errors

# x = float(input('Enter a dividend: '))
# y = float(input('Enter a divisor: '))
# try:
#     print(f'The quotient is: {x/y}')
# except ZeroDivisionError:
#     print("You can't divide by zero")

print("Demo of while loops with try except")
while True:
    while True:
        try:
            x = float(input('Enter a dividend: '))
            y = float(input('Enter a divisor: '))
            break
        except ValueError:
            print("Please enter a number. Try again!")
    try:
        print(f'The quotient is: {x/y}')
        break
    except ZeroDivisionError:
        print("You can't divide by zero")

print("\nDemo of multiple except blocks, an else block and a finally block")
try:
    x = float(input('Enter a dividend: '))
    y = float(input('Enter a divisor: '))
    print(f'The quotient is: {x/y}')
# you can stack except blocks
except ValueError:
    print("Please enter a number. Try again!")
except ZeroDivisionError:
    print("You can't divide by zero")
except:
    print('Something went wrong')
# else block runs only when try is successful
else:
    print('You successfully divided a number')
# finally block will always run
finally:
    print('Thanks')

print("\nDemo of raise")
try:
    x = float(input('Enter a dividend: '))
    y = float(input('Enter a divisor: '))
    print(f'The quotient is: {x/y}')
except ValueError:
    print("Please enter a number. Try again!")
except:
    if y == 0:
        raise
    print('Something went wrong')
else:
    print('You successfully divided a number')
finally:
    print('Thanks')

print("\nDemo of sys.exc_info()")
import sys
try:
    x = float(input('Enter a dividend: '))
    y = float(input('Enter a divisor: '))
    print(f'The quotient is: {x/y}')
except:
    print(sys.exc_info()[0]) # type
    print(sys.exc_info()[1]) # value
    print(sys.exc_info()[2]) # traceback
    print('Something went wrong')
else:
    print('You successfully divided a number')
finally:
    print('Thanks')

# ====== Lesson 12 ======
print("*"*20, "Lesson 12", "*"*20)

import csv

print('\nWriting to a CSV')
with open('customers.csv', mode='w', newline='') as fbs:
    customers_file = csv.writer(fbs, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='"')
    
    customers_file.writerow(['firstname', 'lastname', 'age', 'email'])
    customers_file.writerow(['john', 'smith', 35, 'js@outlook.com'])
    customers_file.writerow(['mary', 'ryan', 43, 'mr@hotmail.com'])

with open('agents.csv', mode='w', newline='') as fbs:
    field_names = ['firstname', 'lastname', 'age', 'email']
    agents_file = csv.DictWriter(fbs, fieldnames=field_names)

    agents_file.writeheader()
    agents_file.writerow({'age': 35, 'firstname':'john', 'lastname':'smith', 'email':'js@outlook.com'})
    agents_file.writerow({'firstname':'mary', 'lastname':'ryan', 'age': 43, 'email':'mr@outlook.com'})

print('\nReading a CSV')
print('csv.reader()')
with open('capitals.csv', mode='r') as fbs:
    capitals = csv.reader(fbs)
    is_first = True
    for row in capitals:
        if is_first:
            print(f"{'    '.join(row).title()}")
            is_first = False
        else:
            print(f"{row[0].title()}    {row[1].title()}    {row[2].title()}")

# to avoid indexing errors
print('\ncsv.DictReader()')
with open('capitals.csv', mode='r') as fbs:
    capitals = csv.DictReader(fbs)
    is_first = True
    for row in capitals:
        if is_first:
            print(f"{'    '.join(row).title()}")
            is_first = False
        else:
            print(f"{row['Country'].title()}    {row['Capital'].title()}    {row['Population'].title()}")

# serialization: convert a Python object into a string in the JSON format
# deserialization: convert a string in the JSON format into a Python object

print('\nSerialization')
customers = {
    123456: {'name': 'Walter Wall', "age": 35, "email": "walter_wall@gmail.com", "profession": "floorer"},
    234567: {'name': 'Polly Pocket', 'age': 6, 'email': 'polly_pocket@hotmail.com', 'profession': 'Children\'s Entertainer'},
    345678: {'name': 'Freda Convict', 'age': 44, 'email': 'freda_convict@yahoo.com', 'profession': 'Prison Warden'}
}

import json

with open('customers.json', 'w') as fbs:
    json.dump(customers, fbs, indent=4)

json_str = json.dumps(customers, indent=4)
print(json_str)

# serialization: data type conversion chart
# Python | JSON
# dict | object
# list, tuple | array
# str | string
# int, float | number
# True | true
# False | false
# None | null

# deserialization: data type conversion chart
# JSON | Python
# object | dict
# array | list
# string | str
# number (int) | int
# number (not int) | float
# true | True
# false | False
# null | None

print('\nDeserialization')
with open('customers.json', 'r') as fbs:
    loaded_data = json.load(fbs)

print(loaded_data)

print(json.loads(json_str))

# ====== Lesson 13 ======
print("*"*20, "Lesson 13", "*"*20)