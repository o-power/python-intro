
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
# first make a copy
print("*"*50)
words = ['cat','window','defenestrate']
for w in words[:]:
    if len(w) > 6:
        words.insert(0,w)
print(words)