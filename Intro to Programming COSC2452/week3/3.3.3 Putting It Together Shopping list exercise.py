#3.3.3 shopping list program
#Meet requirements of the assessment

import sys
from collections import deque

#Program initial intro and flavour
sys.stdout.write("*You walk into the local shops and look down at your shopping list*\n")
sys.stdout.write("Todays shopping list is:\n")
#Shopping list
shoppingList=deque(["chocolate","pasta","pesto","lemon","parsley"])
"""Prints shopping list into seperate lines of text for a visual representation of an actual
shopping list"""
def show_shoppingList():
    for x in shoppingList:
        sys.stdout.write (x + "\n")
show_shoppingList()

#flavour text
sys.stdout.write("*As you walk through the aisles you think to yourself*\n")
#call to action and first inputs
sys.stdout.write("Is there anything on special I should add to my basket today?\n")
#reads inuts and adds to shoppingList
special=sys.stdin.readline().strip()
shoppingList.append(special)
#confirms special is added to list
sys.stdout.write(special + " is added to your basket.\n")
#anotther call to action to amend list with flavour text
sys.stdout.write("..anything else?\n")
special2=sys.stdin.readline().strip()
shoppingList.append(special2)
#confirms special 2 is added to the list
sys.stdout.write(special2 + " is added to your basket.\n")
#prints basket to show all new items
"""code removed as it clutters display
sys.stdout.write("In your basket you now have:\n")
#show_shoppingList()"""
#call to action that removes first item in shopping list
sys.stdout.write("That might be too many things, I'll just put the " +str(shoppingList[0])+ " back.\n")
shoppingList.popleft()
#lists items left in the basket
sys.stdout.write("in your basket you now have:\n")
show_shoppingList()
#flavour text and end of program
sys.stdout.write("that's okay, I was kind of craving " +str(shoppingList[5])+ " today\n")
sys.stdout.write("Maybe we can get something a Mars Bar at the checkout though..")






