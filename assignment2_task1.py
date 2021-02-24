name = " \t\nJoe\n\t Bloggs\n\t "
divider = "\n*******************************************\n"
message =  "START>" + name + "<END"

print(divider)
print(message)

message = "START>" + name.lstrip() + "<END"

print(divider)
print(message)

message = "START>" + name.rstrip() + "<END"

print(divider)
print(message)

message = "START>" + name.strip() + "<END"

print(divider)
print(message)

print(divider)
print("Do-re-mi, the first three notes just happen to be\rDO-RE-MI-FA-SO-LA-TI-DO")

print(divider)
#print('It's a test!')
#SyntaxError: invalid syntax
print('It\'s a test!')