quantity = 0

#stores stock
products = [ {"name" : "milk" , "price" : 0.75 , "quantity" : 100},
        
             {"name" : "bread" , "price" : 1.00 , "quantity" : 50},

             {"name" : "flour" , "price" : 1.25 , "quantity" : 300},

             {"name" : "eggs" , "price" : 1.00 , "quantity" : 30},

             {"name" : "beef" , "price" : 5.00 , "quantity" : 20}]

#stores customer items
basket = [{"name" : "milk" , "quantity" : quantity},
          {"name" : "bread" , "quantity" : quantity},
          {"name" : "flour" , "quantity" : quantity},
          {"name" : "eggs" , "quantity" : quantity},
          {"name" : "beef" , "quantity" : quantity},]

print("Welcome to the shop!\n")

#loop returns user back to the menu
shopping = True
while shopping == True:

    while True:
        try:                 #user menu
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
    
    #Shows all items, their price and stock
    if menu_choice == 1:
        for stock in range(0,len(products)):
            print(products[stock]["name"],"costs £" + str(products[stock]["price"]) , ":" , products[stock]["quantity"] , "in stock. \n")

    #Shows the user basket
    elif menu_choice == 2:
        total = 0
        for index in range (0,len(basket)):   
            total = total + basket[index]["quantity"] * products[index]["price"]

        if total == 0:
            print("Your basket is empty!")

        else:
            for index in range (0,len(basket)):
                single_item_total = basket[index]["quantity"] * products[index]["price"]

                if single_item_total != 0:
                    print(basket[index]["name"] , basket[index]["quantity"] , "unit(s)  £" + str(single_item_total))
            print("Your total is £" + str(total) , "\n")

    #Lets the user chooose his items      
    elif menu_choice == 3:
            menu_check = True
            while menu_check == True:
                while True:
                    try:
                        purchase_choices = {int(choice) for choice in input("select which items you want to buy \n"
                                                                            "1. Milk \n"
                                                                            "2. Bread \n"
                                                                            "3. flour \n"
                                                                            "4. eggs \n"
                                                                            "5. beef \n").split()}
                        purchase_choices = list(purchase_choices)
                        #checks if the user input is an actual option
                        error_found = 0
                        for check in range(0,len(purchase_choices)):
                            if purchase_choices[check] < 1 or purchase_choices[check] > 5:
                                error_found = 1
                                print("Please only enter numbers on the menu\n")
                                break

                        if error_found == 0:
                            menu_check = False
                        break

                    except ValueError:
                        print("Please enter only numbers\n")
                    
            for index in range (0,len(purchase_choices)):

                #saves the stock and basket amounts to return to if user orders too much
                stock_save = products[purchase_choices[index]-1]["quantity"]
                basket_save = basket[purchase_choices[index]-1]["quantity"]

                while True:
                    try:
                        while True:
                            print("How much" , basket[purchase_choices[index]-1]["name"] , "do you want? \n" )
                            how_much = int(input())
                            if how_much < 1 :
                                print("You cant order negative / zero amounts!")
                            else:
                                break
                              #Calculates the new basket and stock contents
                        basket[purchase_choices[index]-1]["quantity"] = basket[purchase_choices[index]-1]["quantity"] + how_much
                        products[purchase_choices[index]-1]["quantity"] = products[purchase_choices[index]-1]["quantity"] - how_much
                        break
                    except ValueError:
                        print("Enter the amount you want using numbers")
                    #prevents user from order more than available and restored the original stock and basket
                if products[purchase_choices[index]-1]["quantity"] < 0:
                    print("We do not have that much in stock\n")
                    products[purchase_choices[index]-1]["quantity"] =  stock_save
                    basket[purchase_choices[index]-1]["quantity"] = basket_save

    #lets the user remove items
    elif menu_choice == 4:
        while True:
            total = 0
            for index in range (0,len(basket)):   
                total = total + basket[index]["quantity"] * products[index]["price"]
            if total == 0:
                print("Your basket is already empty!")
                break
            menu_check = True
            while menu_check == True:
                while True:
                    try:
                        return_choices = {int(choice) for choice in input(" select which items you want to remove \n"
                                                                                    "1. Milk \n"
                                                                                    "2. Bread \n"
                                                                                    "3. flour \n"
                                                                                    "4. eggs \n"
                                                                                    "5. beef \n").split()}
                        return_choices = list(return_choices)
                        error_found = 0
                        #checks if the user input is an actual option
                        for check in range(0,len(return_choices)):
                            if return_choices[check] < 1 or return_choices[check] > 5:
                                error_found = 1
                                print("Please only enter numbers in the menu")
                                break
                        if error_found == 0:
                            menu_check = False
                            break
                    except ValueError:
                                    print("Please enter only numbers\n")
                        
                            
                for index in range (0,len(return_choices)):
                    #saves the stock and basket amounts to return to if tries to return too much
                    stock_save = products[return_choices[index]-1]["quantity"]
                    basket_save = basket[return_choices[index]-1]["quantity"]

                    while True:
                        try:
                            while True:
                                print("How much" , basket[return_choices[index]-1]["name"] , "do you want to return?") 
                                how_much = int(input())
                                if how_much < 1:
                                    print("please dont enter negative / amounts")
                                else:
                                    break
                                #calculates the new basket and stock
                            basket[return_choices[index]-1]["quantity"] = basket[return_choices[index]-1]["quantity"] - how_much
                            products[return_choices[index]-1]["quantity"] = products[return_choices[index]-1]["quantity"] + how_much
                            break
                        except ValueError:
                            print("Please enter only numbers")
                            #checks that the user didnt attempt to return too much and restores the stock and basket
                    if basket[return_choices[index]-1]["quantity"] < 0:
                        print("You attempted to return too much items")
                        products[return_choices[index]-1]["quantity"] =  stock_save
                        basket[return_choices[index]-1]["quantity"] = basket_save
            break

    #lets the user checkout
    elif menu_choice == 5:
         while True:
            total = 0
            for index in range (0,len(basket)):
                total = total + basket[index]["quantity"] * products[index]["price"]
            if total == 0:
                print("You cant checkout with an empty basket!")
                break
            print("Your total is £" + str(total) , "\n")  
            choice = input("Do you want to checkout? Y/N\n")

            if choice.upper() == "Y":
                print("Thanks for visiting!\n")
                shopping = False
                break

            elif choice.upper() == "N":
                print("Please continue shopping!\n")
                break

            else:
                print("Please enter Y or N\n")

    #lets the user leave the shop without checking out
    elif menu_choice == 6:
        while True:
            choice = input("Are you sure you want to leave? Y/N ")
            if choice.upper() == "Y":
                print("See you soon!")
                shopping = False
                break

            elif choice.upper() == "N":
                print("Please continue shopping!")
                break
            else:
                print("Please enter Y or N")

    elif menu_choice < 1 or menu_choice > 6:
        print("Please select using a number from the list of options")

input()
