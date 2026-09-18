
# option 3
#------------------#
def op3 (products , basket):
    menu_check = True
    while menu_check == True:
        while True:
            try: # Print out which items the user can order based of what is in products
                print("Select which items you want to buy:")
                for options in range(0,len(products)):
                    print(f"{options+1}. {products[options]["name"]}")

                purchase_choices = {int(choice) for choice in input().split()}
                purchase_choices = list(purchase_choices)

                # checks if the user input is an actual option
                error_found = 0
                for check in range(0, len(purchase_choices)):
                    if purchase_choices[check] < 1 or purchase_choices[check] > len(products):
                        error_found = 1
                        print("Please only enter numbers on the menu\n")
                        break
    
                if error_found == 0:
                    menu_check = False
                break
    
            except ValueError:
                print("Please enter only numbers\n")
    
    for index in range(0, len(purchase_choices)):
        ordering = True
        while ordering == True:
            try:
                print("How much", basket[purchase_choices[index]-1]["name"], "do you want? \n")
                how_much = int(input())
                if how_much < 1:
                    print("You can't order negative / zero amounts !")

                elif how_much > products[purchase_choices[index]-1]["quantity"]:
                    print("We do not have that much in stock")
                    while True:
                        choice = input("Do you want to order a different amount? Y/N\n")

                        if choice.upper() == "Y":
                            break
                        elif choice.upper() == "N":
                            ordering = False
                            break
                        else:
                            print("please enter Y or N")

                else:
                     # Calculates the new basket and stock contents
                    basket[purchase_choices[index] -1]["quantity"] = basket[purchase_choices[index]-1]["quantity"] + how_much
                    products[purchase_choices[index] -1]["quantity"] = products[purchase_choices[index]-1]["quantity"] - how_much
                    ordering = False

            except ValueError:
                print("Enter the amount you want using numbers")

    return(products , basket)  