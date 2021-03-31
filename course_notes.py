
# help("keywords")

# y is x returns True is y and x point to the same memory location e.g.
print("*"*50)
x = "test"
y = x
print(f"id(x) is: {id(x)}")
print(f"id(y) is: {id(y)}")
print(f"y is x returns: {y is x}")
print(f"x is y returns: {x is y}")

a = "banana"
b = "bananas"
print(f"id(a) is: {id(a)}")
print(f"id(b) is: {id(b)}")
print(f"b is a returns: {b is a}")
print(f"a is b returns: {a is b}")

c = "banana"
d = "banana"
print(f"id(c) is: {id(c)}")
print(f"id(d) is: {id(d)}")
print(f"d is c returns: {d is c}")
print(f"c is d returns: {c is d}")

# big numbers - to help programmer type it in, underscores not displayed
print("*"*50)
big_number = 75_000_000_000
print(big_number)

# multiple assignments on one line
print("*"*50)
x, y = 6, 7

# tuples with one item need a comma
print("*"*50)
my_tuple = (20)
print(type(my_tuple))

my_tuple = (20,)
print(type(my_tuple))

# If modifying the sequence you are iterating over while inside the loop
# first make a copy; otherwise the below would be an infinite loop.
print("*"*50)
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