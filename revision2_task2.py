def can_convert_to_int(x):
    """Returns True if x can be converted to an int."""
    try:
        int(x)
        return True
    except ValueError:
        return False

def choose_base(available_bases):
    """Returns the choosen base."""
    base_is_available = False

    while not base_is_available:
        base = input("\nChoose a base: ").strip()
        if base.lower() in available_bases:
            base_is_available = True
            print(f"You have choosen {base.title()} as your base.")
        else:
            print(f"{base.title()} is not available.")
            print(f"The available bases are: {[available_base.title() for available_base in available_bases]}")
    
    return base

def choose_sauce(available_sauces):
    """Returns the choosen sauce."""
    sauce_is_available = False

    while not sauce_is_available:
        sauce = input("\nChoose a sauce: ").strip()
        if sauce.lower() in available_sauces:
            sauce_is_available = True
            print(f"You have choosen {sauce.title()} as your sauce.")
        else:
            print(f"{sauce.title()} is not available.")
            print(f"The available sauces are: {[available_sauce.title() for available_sauce in available_sauces]}")
    
    return sauce

def choose_toppings(available_toppings):
    """Returns the choosen toppings."""
    user_has_quit = False
    toppings = []

    while not user_has_quit:
        topping_is_available = False

        while not topping_is_available:
            topping = input("\nChoose a topping. Type 'done' when finished: ").strip()
            if topping.lower() == 'done':
                user_has_quit = True
                break
            elif topping.lower() in available_toppings['veg'] or topping.lower() in available_toppings['meat']:
                topping_is_available = True
                toppings.append(topping)
                print(f"You have choosen {topping.title()} as your topping.")
            else:
                print(f"{topping.title()} is not available.")
                print(f"The available vegetarian toppings are: {[available_topping.title() for available_topping in available_toppings['veg']]}")
                print(f"The available meat toppings are: {[available_topping.title() for available_topping in available_toppings['meat']]}")
    
    return toppings

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

    pizza['base'] = choose_base(available_bases)
    pizza['sauce'] = choose_sauce(available_sauces)
    pizza['toppings'] = choose_toppings(available_toppings)
    
    print("\nYou have order a pizza with:")
    print(f"Base: {pizza['base'].title()}")
    print(f"Sauce: {pizza['sauce'].title()}")
    print(f"Toppings: {[topping.title() for topping in pizza['toppings']]}")

    print("\nThanks for using the Pizza Pisa Order System")

if __name__ == "__main__":
    # Code in here will only execute when the file is run directly    
    main()