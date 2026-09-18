
# option 1 
#------------------#
def op1(products):
    for stock in range(0, len(products)):
        print(products[stock]["name"], "costs £" + str(products[stock] ["price"]), ":", products[stock]["quantity"], "in stock. \n")


# option 2
#------------------#
def op2(products , basket):
    total = 0
    for index in range(0, len(basket)):
        total = total + basket[index]["quantity"] * products[index]["price"]
            
    if total == 0:
        print("Your basket is empty!")
            
    else:
        for index in range(0, len(basket)):
            single_item_total = basket[index]["quantity"] * products[index]["price"]
            
            if single_item_total != 0:
                print(basket[index]["name"], basket[index]["quantity"], "unit(s)  £" + str(single_item_total))
        print("Your total is £" + str(total), "\n")

