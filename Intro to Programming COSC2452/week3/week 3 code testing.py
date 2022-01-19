#Import required libraries and modules:
##sys library
##deque module from collections library
import sys
from collections import deque


#Define preliminary list:
shopping_list = deque(["Ice Cream", "Cookies", "Chocolate", "Beer", "More ice cream"])


#Define custom functions:
def print_shopping_list():
    """This function simply prints the 'shopping_list' list and inserts a line break
    in between each item. There are no inputs or requirements from the user other
    than to call the function."""
    for i in shopping_list:
        sys.stdout.write(i + "\n")

def linebr():
    """This function simply prints a line break without repeating code. Used to organise
    and control the flow of the program easily. There are no inputs or requirements
    from the user other than to call the function."""
    sys.stdout.write("\n")


sys.stdout.write("It's time to go shopping... Yay...\n"
                 + "Here's the list so far:\n\n")

#use 'help' function for docstring
print_shopping_list()

#use 'help' function for docstring
linebr()

#Waits for user input, allocates input to variable 'addition', and appends variable
#addition to 'shopping_list' list.
sys.stdout.write("Add one more thing to the list to make the damn journey worth while:\n")
addition = sys.stdin.readline().strip()
shopping_list.append(addition)

#strings text and prints item added to the list.
sys.stdout.write("You added " + addition + ". How original.\n")

linebr()

sys.stdout.write("Here's your current list:\n")
print_shopping_list()

linebr()

#Strings text and prints item at index 0.
sys.stdout.write("I'm not sure you need " + shopping_list[0] + ". I'm going to remove this \
for you. LOL")

linebr()
linebr()

#Rather than proceeding with the program, this section pauses it until the user is able to
#read through the outputs and understand what's going on, and what's going to happen.
input("Press enter to continue. There is legit nothing you can do about it.")
shopping_list.popleft()

linebr()

sys.stdout.write("Here's your new list dude:\n")
print_shopping_list()

linebr()
sys.stdout.write("We done.")
