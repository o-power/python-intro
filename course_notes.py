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
print(f'id: {id(age)}')
print(f'type: {type(age)}')
print(f'value: {age}\n')

age = 44
print(f'id: {id(age)}')
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

print(f"{8/4}") # 2.0
print(f"{8/3}") # 2.666
print(f"{8//3}\n") # 2

# big numbers - to help programmer type it in, underscores not displayed
big_number = 75_000_000_000
print(big_number)

# multiple assignments on one line
x, y = 6, 7

# ====== Lesson 3 ======
print("*"*20, "Lesson 3", "*"*20)

# del list_name[item index]
# removed_item = list_name.pop(item index)
# remove('item value')

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
print("*"*50)
my_tuple = (20)
print(type(my_tuple))

my_tuple = (20,)
print(type(my_tuple))



# clear()
print("*"*50)
customer_1 = {'name': 'Joe Bloggs', 'age': 24}
print(f"Customer 1: {customer_1}")
customer_1.clear()
print(f"Customer 1: {customer_1}")

# pop()
print("*"*50)
customer_1 = {'name': 'Joe Bloggs', 'age': 24}
print(f"Customer 1: {customer_1}")
age = customer_1.pop('age')
print(f"Customer 1: {customer_1}")
print(age)

# popitem()
print("*"*50)
customer_1 = {'name': 'Joe Bloggs', 'age': 24}
print(f"Customer 1: {customer_1}")
popped_item = customer_1.popitem()
print(f"Customer 1: {customer_1}")
print(popped_item)

# get()
print("*"*50)
customer_1 = {'name': 'Joe Bloggs', 'email': 'joe_bloggs@gmail.com'}
print(f"Customer 1: {customer_1}")
age = customer_1.get('age',"Customer's age is unknown")
print(f"Customer 1: {customer_1}")
print(age)

# setdefault()
print("*"*50)
customer_1 = {'name': 'Joe Bloggs', 'email': 'joe_bloggs@gmail.com'}
print(f"Customer 1: {customer_1}")
age = customer_1.setdefault('age', 'Unknown')
print(f"Customer 1: {customer_1}")
print(age)

# items()
print("*"*50)
customer_1 = {'name': 'Joe Bloggs', 'email': 'joe_bloggs@gmail.com'}
print(f"Customer 1: {customer_1}")
customer_items = customer_1.items()
print(customer_items)
print(type(customer_1))
print(type(customer_items))

# keys()
print("*"*50)
customer_1 = {'name': 'Joe Bloggs', 'email': 'joe_bloggs@gmail.com'}
print(f"Customer 1: {customer_1}")
customer_keys = customer_1.keys()
print(customer_keys)
print(type(customer_1))
print(type(customer_keys))

# keys()
print("*"*50)
customer_1 = {'name': 'Joe Bloggs', 'email': 'joe.bloggs@gmail.com', 'email2': 'joe.bloggs@gmail.com'}
print(f"Customer 1: {customer_1}")
customer_values = customer_1.values()
print(customer_values)
print(type(customer_1))
print(type(customer_values))

# Loops
print("*"*50)
for key, value in customer_1.items():
    print(f"Key:Value {key}:{value}")

for key in customer_1:
    print(f"Key {key}")
    print(f"customer_1[Key]: {customer_1[key]}")

for key in customer_1.keys():
    print(f"Key {key}")

for key in sorted(customer_1.keys()):
    print(f"Key {key}")

print("*"*50)
print(customer_1)
for value in customer_1.values():
    print(f"Value {value}")

for value in set(customer_1.values()):
    print(f"Value {value}")

print("This is a message.", end = " ")
print("This is a second message.")

def print_toppings(*toppings):
    """Demo of arbitrary argument lists.

    This just shows that the arbitrary arguments
    are put into a tuple.
    """
    print(toppings)

print_toppings("cheese", "mushrooms", "mozzarella")

def concat(*args, sep="/"):
    return sep.join(args)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# returns "__main__" if script ran as python random.py
# returns "random" if script is imported into another script
# This is often used either to provide a convenient user interface to a module,
#  or for testing purposes (running the module as a script executes a test suite).
print(__name__)

import copy

person_1 = {'name': 'Walter Wall', "age": 35, "email": "walter_wall@gmail.com", "profession": "floorer"}
person_2 = {'name': 'Polly Pocket', 'age': 6, 'email': 'polly_pocket@hotmail.com', 'profession': 'Children\'s Entertainer'}
customers = {1234: person_1, 2345: person_2}
customers_deep_copy = copy.deepcopy(customers)
customers_shallow_copy = customers.copy()
person_1.clear()
print(f"Customers Person 1: \n {customers[1234]}")
print(f"Customers Copy Person 1: \n {customers_shallow_copy[1234]}")
print(f"Customers Copy Person 1: \n {customers_deep_copy[1234]}")

# https://docs.python.org/3/library/datetime.html#module-datetime
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
import datetime as dt
# method strftime of datetime class in module dt
#formatted_dt = dt.datetime.strftime(datetime_object, "format codes")

current_time = dt.datetime.now()
print(f"Unformatted date and time: {current_time}")
formatted_time = dt.datetime.strftime(current_time, "%d/%m/%Y %H:%M:%S")
print(f"Formatted date and time: {formatted_time}")

# method strftime of date class in module dt
#formatted_dt = dt.datetime.strftime(datetime_object, "format codes")

current_date = dt.date.today()
print(f"Unformatted date: {current_date}")
formatted_date = dt.date.strftime(current_date, "%a, %d %b %y")
print(f"Formatted date: {formatted_date}")

# new_datetime_object = dt.datetime.strptime("string to parse", "format codes")

current_date = dt.date.today()
input_date = input("Enter the date of your deadline in the format dd/mm/yyyy format: ")
deadline = dt.datetime.strptime(input_date, "%d/%m/%Y")
print(f"Your deadline (datetime): {deadline}")
# convert datetime to date
deadline = deadline.date()
print(f"Your deadline (date): {deadline}")
print(f"You have {(deadline - current_date).days} days until your deadline.")

# import io
# file_stream = open('pi.txt','r')
# file_contents = file_stream.read()
# print(file_contents)
# file_stream.close()

# file_stream = open('pi.txt','r')
# first_line = file_stream.readline()
# print(first_line)
# second_line = file_stream.readline()
# print(second_line)
# file_stream.close()

# file_stream = open('text.txt','w')
# text = input('Enter some text to add to file: ')
# file_stream.write(text)
# file_stream.close()

# help("os.path")

# if os.path.isfile('text.txt'):
#     file_stream = open('text.txt','a')
# else:
#     file_stream = open('text.txt','w')
# text = input('Enter some text to add to file: ')
# file_stream.write(text)
# file_stream.close()

# with open('text.txt','r') as file_stream:
#     file_contents = file_stream.read()
# print(file_contents)

# with open('text.txt','r') as file_stream:
#     file_contents = file_stream.readlines()

# for line in file_contents:
#     print(line.rstrip())

# Syntax Errors
# Logic Errors
# Runtime Errors

x = float(input('Enter a dividend: '))
y = float(input('Enter a divisor: '))

try:
    print(f'The quotient is: {x/y}')
except ZeroDivisionError:
    print("You can't divide by zero")

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

try:
    x = float(input('Enter a dividend: '))
    y = float(input('Enter a divisor: '))
    
    print(f'The quotient is: {x/y}')
except ValueError:
    print("Please enter a number. Try again!")
except ZeroDivisionError:
    print("You can't divide by zero")
except:
    print('Something went wrong')
else:
    print('You successfully divided a number')
finally:
    print('Thanks')

# try:
#     x = float(input('Enter a dividend: '))
#     y = float(input('Enter a divisor: '))
    
#     print(f'The quotient is: {x/y}')
# except ValueError:
#     print("Please enter a number. Try again!")
# except:
#     if y == 0:
#         raise
#     print('Something went wrong')
# else:
#     print('You successfully divided a number')
# finally:
#     print('Thanks')

import sys

try:
    x = float(input('Enter a dividend: '))
    y = float(input('Enter a divisor: '))
    
    print(f'The quotient is: {x/y}')
except:
    print(sys.exc_info()[0])
    print('Something went wrong')
else:
    print('You successfully divided a number')
finally:
    print('Thanks')