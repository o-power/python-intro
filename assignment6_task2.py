import uuid

# 1. Create a dictionary called person_1. Decide what you want to use as keys – 
#    you need to think about what you would want to record about a person (for 
#    example maybe their name, age, email) and name your keys accordingly
person_1 = {'name': 'Walter Wall', "age": 35, "email": "walter_wall@gmail.com", "profession": "floorer"}

# 2. Print the dictionary
print(f'Person 1: {person_1}')

# 3. Repeat step 1 and 2 a couple more times using the fromkeys() method, calling the new dictionaries person_2 and person_3. 
#    When creating one of them provide a default value with the fromkeys() method but not with the other, notice the difference 
#    when you print the dictionaries
person_2 = person_1.fromkeys(person_1)
print(f'Person 2: {person_2}')
person_3 = person_1.fromkeys(person_1,'TBD')
print(f'Person 3: {person_3}')
#person_4 = dict.fromkeys(person_1)
#print(person_4)

# 4. Use the update() method to add the details for the two new dictionaries, printing each one after you add the items to
#    make sure it worked
person_2.update({'name': 'Polly Pocket', 'age': 6, 'email': 'polly_pocket@hotmail.com', 'profession': 'Children\'s Entertainer'})
print(f'Person 2: {person_2}')
person_3.update({'name': 'Freda Convict', 'age': 44, 'email': 'freda_convict@yahoo.com', 'profession': 'Prison Warden'})
print(f'Person 3: {person_3}')

# 5. Create a dictionary called customers, adding the three dictionaries as the items – the keys must be unique, so use 
#    account numbers as the keys (these can be integers)
customers = {
    123456: person_1,
    234567: person_2,
    345678: person_3
}

# customers = {
#     uuid.uuid4(): person_1,
#     uuid.uuid4(): person_2,
#     uuid.uuid4(): person_3 
# }

# 6. Iterate over the customers dictionary to display the items. As an example, you could display them in the following way:
for key, value in customers.items():
    print(f"The details for account number {key} are: {value}")
