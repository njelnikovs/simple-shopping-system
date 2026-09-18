from functions.display import op1 , op2
from functions.user_order import op3
from functions.user_remove import op4
from functions.leave_checkout import op5 , op6

quantity = 0

# stores stock
products = [{"name": "milk", "price": 0.75, "quantity": 100},

            {"name": "bread", "price": 1.00, "quantity": 50},

            {"name": "flour", "price": 1.25, "quantity": 300},

            {"name": "eggs", "price": 1.00, "quantity": 30},

            {"name": "beef", "price": 5.00, "quantity": 20},

            {"name": "chicken", "price": 3.00, "quantity": 50}]

# stores customer items
basket =[]

# creates the dictionary list for the basket based off what is in products
for index in range (0,len(products)):
    basket.append ({
        "name" : products[index]["name"],
        "quantity" : 0 })

print("Welcome to the shop!\n")

# loop returns user back to the menu
shopping = True

while shopping == True:
    while True:
        try:  # user menu
            menu_choice = int(input("1. View products\n"
                                    "2. View basket\n"
                                    "3. Add items\n"
                                    "4. Remove items\n"
                                    "5. Checkout\n"
                                    "6. Exit\n \n"))
            break
        except ValueError:
            print("Please enter only numbers \n")
    print()

    # Shows all items, their price and stock
    if menu_choice == 1:
        op1(products)

     
    # Shows the user basket
    elif menu_choice == 2:
        op2(products , basket)
       
    # Lets the user chooose his items
    elif menu_choice == 3:
        op3(products , basket)
       
    # lets the user remove items
    elif menu_choice == 4:
        op4(products , basket)

    # lets the user checkout
    elif menu_choice == 5:
       shopping =  op5(products , basket , shopping)

    # lets the user leave the shop without checking out
    elif menu_choice == 6:
        shopping = op6(shopping)

    elif menu_choice < 1 or menu_choice > 6:
        print("Please select using a number from the list of options")

input()
