def can_convert_to_int(x):
    """Returns True if x can be converted to an int."""
    try:
        int(x)
        return True
    except ValueError:
        return False

def choose_base(available_bases):
    """Returns the choosen base."""
    base = input("Choose a base: ").strip()
    base_is_available = False

    while base_is_available:
        if base.lower() in available_bases:
            print("You have choosen {base} as your base.")
        else:
            print("{base} is not available.")
            print("The available bases are: {available_bases}")
    
    return base

def choose_sauce(available_sauces):
    # sauce = 'Tomato'
    # sauce_is_available = True
    # if sauce in available_sauces:
    #     print(f"Your chosen sauce, {sauce}, is available.")
    # else:
    #     print(f"Your chosen sauce, {sauce}, is not available.")
    #     sauce_is_available = False
    pass

def choose_toppings(available_toppings):
    # toppings = ['Pepperoni', 'Onion', 'Mushroom', 'Pineapple', 'Sweetcorn', 'Mozzarella']
    # topping_is_available = True
    # for topping in toppings:
#     if topping in available_veg_toppings or topping in available_meat_toppings:
#         print(f"Your chosen topping, {topping}, is available.")
#     else:
#         print(f"Your chosen topping, {topping}, is not available.")
#         topping_is_available = False
    
#     if topping == 'Pineapple':
#         print(f"Pineapple is a controversial topping!")
    pass

def main():
    """Runs the pizza ordering program."""
    message = "="*50
    message += "\n= Welcome to the Pizza Pisa Order System."
    message += "\n="
    message += "\n= Type 'quit' at any time to exit.\n"
    message += "="*50
    print(message)

    available_sauces = ['tomato', 'pesto', 'bechamel', 'garlic', 'bbq']
    available_bases = ['thin crust', 'thick crust', 'chicago deep dish', 'gluten free']
    available_toppings = {'veg': ['onion', 'mushroom', 'pineapple', 'mozzarella', 'cheddar', 'red pepper'],
        'meat': ['pepperoni', 'chicken', 'sausage', 'bacon']}
    
    pizza = {}

    pizza['base'] = choose_base(available_bases, has_not_quit)
    pizza['sauce'] = choose_sauce(available_sauces)
    pizza['toppings'] = choose_toppings(available_toppings)
    print(pizza)

    print("\nThanks for using the Pizza Pisa Order System")

if __name__ == "__main__":
    # Code in here will only execute when the file is run directly    
    main()