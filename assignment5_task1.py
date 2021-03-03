divider = "\n"+"*"*40+"\n"

# 1. Create a list of car makes, or if you like you can use the list you made for assignment 3, 
#    just make sure that you include “bmw” and “mg”, and check that all the car makes are stored
#    in the list in lowercase letters so you can see the difference in the next step
car_makes = ['nissan','skoda','volkswagen','toyota','hyundai','honda','bmw',
                'ford','lada','ferrari','dacia','volvo','fiat','isuzu','rover','mg']

# 2. Iterate over the list, printing each car make in title case, unless it is bmw or mg. 
#    If it is, print it in uppercase.
print(divider)
for car_make in car_makes:
    if car_make in ['bmw','mg']:
        print(car_make.upper())
    else:
        print(car_make.title())

# 3. The customers are classed according to the type of car they buy. Iterate over the list,
#    and according to the type of car, print a message stating the class of the customer. As an example:
#        If they buy cars like Ford, Toyota, Kia, MG they are classed as Bronze customers
#        If they buy cars like BMW, Audi, Mercedes they are Silver customers
#        If they buy cars like Chrysler, Ferrari, Lamborghini they are Gold customers
print(divider)
for car_make in car_makes:
    if car_make in ['bmw','ferrari']:
        print(f"Customers who buy {car_make.title() if car_make not in ['bmw', 'mg'] else car_make.upper()} are Gold customers.")
    elif car_make in ['nissan','volkswagen','toyota','honda','ford','volvo']:
        print(f"Customers who buy {car_make.title() if car_make not in ['bmw','mg'] else car_make.upper()} are Silver customers.")
    else:
        print(f"Customers who buy {car_make.title() if car_make not in ['bmw','mg'] else car_make.upper()} are Bronze customers.")

# Getting some practice two-dimensional arrays
# print(divider)
# car_categories = [['nissan','silver']
#             ,['skoda','silver']
#             ,['volkswagen','silver']
#             ,['toyota', 'silver']
#             ,['lada', 'bronze']
#             ,['honda', 'silver']
#             ,['bmw', 'gold']]
# for car in car_categories:
#     print(f"Customers who buy {car[0]} are {car[1]} customers.")

# Getting some practice with dictionaries
# print(divider)
# car_categories = [{"car": "nissan","category": "silver"}
#             ,{"car": "lada","category": "bronze"}
#             ,{"car": "bmw","category": "gold"}]
# for car_category in car_categories:
#     print(f"Customers who buy {car_category['car']} are {car_category['category']} customers.")