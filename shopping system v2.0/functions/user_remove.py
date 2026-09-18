
# option 4
#------------------#
def op4(products , basket):
    quantity_check = True
    while quantity_check == True:
        total = 0
        for index in range(0, len(basket)):
            total = total + basket[index]["quantity"] * products[index]["price"]
        if total == 0:
            print("Your basket is already empty!")
            break

        menu_check = True
        while menu_check == True:
            while True:
                try: # Print out which items the user can remove based of what is in products
                    print("Select which items you want to return:")
                    for options in range(0,len(products)):
                        print(f"{options+1}. {products[options]["name"]}")

                    return_choices = {int(choice) for choice in input().split()}
                    return_choices = list(return_choices)

                    # checks if the user input is an actual option
                    error_found = 0
                    for check in range(0, len(return_choices)):
                        if return_choices[check] < 1 or return_choices[check] > len(products):
                            error_found = 1
                            print("Please only enter numbers on the menu\n")
                            break
        
                    if error_found == 0:
                        menu_check = False
                    break
        
                except ValueError:
                    print("Please enter only numbers\n")
        
        for index in range(0, len(return_choices)):
            returning = True
            while returning == True:
                try:
                    print("How much", basket[return_choices[index]-1]["name"], "do you want to return? \n")
                    how_much = int(input())
                    if how_much < 1:
                        print("You can't return negative / zero amounts !")

                    elif how_much > basket[return_choices[index]-1]["quantity"]:
                        print("You attempted to return too much")
                        while True:
                            choice = input("Do you want to return a different amount? Y/N\n")

                            if choice.upper() == "Y":
                                break
                            elif choice.upper() == "N":
                                returning = False
                                break
                            else:
                                print("please enter Y or N")

                    else:
                        # Calculates the new basket and stock contents
                        basket[return_choices[index] -1]["quantity"] = basket[return_choices[index]-1]["quantity"] - how_much
                        products[return_choices[index] -1]["quantity"] = products[return_choices[index]-1]["quantity"] + how_much
                        quantity_check = False
                        returning = False

                except ValueError:
                    print("Enter the amount you want using numbers")

    return(products , basket)