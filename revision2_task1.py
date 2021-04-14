def can_convert_to_int(x):
    """Returns True if x can be converted to an int."""
    try:
        int(x)
        return True
    except ValueError:
        return False

def view_box_sizes(box_sizes):
    """Displays the available box sizes."""
    message = "\nThe available box sizes are:"
    for box_size in box_sizes:
        message += "\n" + str(box_size) + " inches by " + str(box_size) + " inches"
    print(message)

def view_box_volume(box_sizes):
    """Requests a box size from the user and 
    then calculates and displays the volume."""
    box_size = input("Enter the box size for which the volume is to be calculated: ").strip()
    if can_convert_to_int(box_size):
        box_size = int(box_size)
        if box_size in box_sizes:
            box_volume = box_size**3
            print(f"The volume of a {box_size} inch by {box_size} inch box is {box_volume} cubic inches.")
        else:
            print("This box size is not in the available box sizes.")
    else:
        print("You must enter an integer!")

def add_new_box(box_sizes):
    """Requests a new box size from the user and 
    adds it to the list of available box sizes."""
    new_box_size = input("Enter the new box size: ").strip()
    if can_convert_to_int(new_box_size):
        new_box_size = int(new_box_size)
        if new_box_size in box_sizes:
            print("This box size is already available.")
        else:
            box_sizes.append(new_box_size)
            print("This box size has been added to the available box sizes.")
    else:
        print("You must enter an integer!")
        
def main():
    """Runs the customer order system loop."""
    message = "="*50
    message += "\n= Welcome to the Boxes'R'Us Customer Order System"
    message += "\n="
    message += "\n= Menu Options: "
    message += "\n= 1. View available box sizes."
    message += "\n= 2. View the volume of a box."
    message += "\n= 3. Add a new box size."
    message += "\n="
    message += "\n= Type 'quit' to exit.\n"
    message += "="*50
    print(message)

    box_sizes = [2,3,4,5]

    has_not_quit = True

    while has_not_quit:
        menu_option = input("\nEnter the menu option number: ").strip()

        if menu_option == "quit":
            has_not_quit = False
        elif can_convert_to_int(menu_option):
            menu_option = int(menu_option)
            if menu_option == 1:
                view_box_sizes(box_sizes)
            elif menu_option == 2:
                view_box_volume(box_sizes)
            elif menu_option == 3:
                add_new_box(box_sizes)
            else:
                print("\nYou must enter valid menu option number!")
        else:
            print("\nYou must enter valid menu option number!")

    print("\nThanks for using the Boxes'R'Us Customer Order System")

if __name__ == "__main__":
    # Code in here will only execute when the file is run directly    
    main()