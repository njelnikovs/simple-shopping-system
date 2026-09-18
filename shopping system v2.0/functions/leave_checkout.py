
# option 5
#------------------#
def op5(products , basket , shopping):
    while True:
        total = 0
        for index in range(0, len(basket)):
             total = total + basket[index]["quantity"] * products[index]["price"]
        if total == 0:
            print("You cant checkout with an empty basket!")
            break
        print("Your total is £" + str(total), "\n")
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
    return(shopping)


# option 6
#------------------#
def op6(shopping):
 while True:
    choice = input("Are you sure you want to leave? Y/N ")
    if choice.upper() == "Y":
        print("See you soon!")
        shopping = False
        break

    elif choice.upper() == "N":
        print("Please continue shopping!")

    else:
        print("Please enter Y or N")
    return(shopping)