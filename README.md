# simple-shopping-system
[README.txt](https://github.com/user-attachments/files/32148695/README.txt)
My first major python project after learning some python basics independently during the first 2 weeks of A level. 

Prior to this I only used different python concepts separately and it was my first time trying to use multiple things together (without guidance).
I wanted to see how much I could do just working things out myself.
I completely forgot about using functions in the process of making this but as stated before I went in blind 
working out the logic and most syntax myself.

I might post an updated version to make the 2 dictionary-list relationship less fragile (once I learn how to do that) and use some functions.

I tried my best to check the code for logic errors. 

functionality:

The program is a mini shop simulator interacted with just using the command line.
The user has 6 options to pick from and gets returned to the "main menu" through a loop (unless they leave / checkout)

option 1 shows the user all the items, prices and number available

option 2 shows the user his basket (if it isn't empty)

option 3 allows the user to add items in specific amounts to their basket , which also takes away from the stock and rolls back if the user requests more items than available

option 4 allows the user to remove items in specific amounts to their basket, which also adds those items back to the stock and rolls back if the user requests to return more than what they have

option 5 allows the user to checkout (if the basket isn't empty)

option 6 allows the user to leave the "shop"

I Tried my best to add error handling properly and everywhere when needed as well as not making it possible for the user to order / remove a negative amount, however I did forget to do all of that initially and had to work my way back.

some things I learned / worked out myself:
. How to access data stored in a dictionary using indexes, I did so by making a list of dictionaries. Got the syntax a little wrong initially but managed to work it out after thinking about it differently.





