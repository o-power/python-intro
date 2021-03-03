# 1. Create two string variables, one containing the customer’s choice of sauce and the other 
#    containing the customer’s choice of base
sauce = 'Tomato'
base = 'Thin Crust'

# 2. Create a list of toppings the customer wants on their pizza
toppings = ['Pepperoni', 'Onion', 'Mushroom', 'Pineapple', 'Sweetcorn', 'Mozzarella']

# 3. Create three Boolean flags:
#    sauce_is_available = True
#    base_is_available = True
#    topping_is_available = True
sauce_is_available = True
base_is_available = True
topping_is_available = True

# 4. Now, create four lists, but make sure one of the customer’s chosen toppings isn’t in the lists:
#    A list of available sauces
#    A list of available bases
#    A list of available vegetable toppings
#    A list of available meat toppings
available_sauces = ['Tomato', 'Pesto', 'Bechamel', 'Garlic', 'BBQ']
available_bases = ['Thin Crust', 'Thick Crust', 'Chicago Deep Dish', 'Gluten Free']
available_veg_toppings = ['Onion', 'Mushroom', 'Pineapple', 'Mozzarella', 'Cheddar', 'Red Pepper']
available_meat_toppings = ['Pepperoni', 'Chicken', 'Sausage', 'Bacon']

# 5. Write an if-else chain to check the customer’s choice of sauce against the list of options,
#    printing one message if the sauce is available and another if it is not. If the sauce is 
#    not available, set the relevant Boolean flag to False
if sauce in available_sauces:
    print(f"Your chosen sauce, {sauce}, is available.")
else:
    print(f"Your chosen sauce, {sauce}, is not available.")
    sauce_is_available = False

# 6. Repeat step 5, this time for the customer’s choice of base
if base in available_bases:
    print(f"Your chosen base, {base}, is available.")
else:
    print(f"Your chosen base, {base}, is not available.")
    base_is_available = False

# 7. Iterate over the customer’s list of requested toppings to check each topping against both 
#    vegetable and meat topping lists for availability. Use an if-elif-else chain to do the
#    following in whatever order seems best to you:
#       Tell the customer if their topping is available
#       Tell the customer if their topping is not available – remember to set the Boolean flag to False
#       Display a special message if the customer chose pineapple on their pizza, and if pineapple 
#       isn’t in the list of available toppings remember to set the Boolean flag to False
for topping in toppings:
    if topping in available_veg_toppings or topping in available_meat_toppings:
        print(f"Your chosen topping, {topping}, is available.")
    else:
        print(f"Your chosen topping, {topping}, is not available.")
        topping_is_available = False
    
    if topping == 'Pineapple':
        print(f"Pineapple is a controversial topping!")

# 8. Now you need to build a string message for the customer to know the state of their pizza. 
#    Use three if-else chains to change what will be added to the string depending on whether 
#    the Boolean flags are True or False, a few example outputs are on the following page.
message = "Your order is complete! "
if sauce_is_available:
    message += "It has a sauce, "
else:
    message += "It has no sauce, "

if base_is_available:
    message += "it has a base, "
else:
    message += "It has no base, "

if topping_is_available:
    message += "and it has all the toppings you wanted! "
else:
    message += "and it doesn't have all the toppings you wanted! "

message += "Enjoy your pizza!"

# 9. Print the string created in step 8.
print(message)