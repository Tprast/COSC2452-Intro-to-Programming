import sys
from collections import deque


#IIE03
#Ironing list program


#Program initial intro and flavour
sys.stdout.write("*Sigh.. It's ironing day today*\n")
sys.stdout.write("*You arrange the creased items to be ironed in a stack*\n")
#List of items to be ironed
creased=deque(["blue shirt","business shirt","white shirt","dress pants","chinos"])
"""Lists out items that need to be ironed into a list that is line seperated for ease of visual viewing"""
def show_creased():
    for x in creased:
        sys.stdout.write (x + "\n")
show_creased()


#Program flavour text
sys.stdout.write("*You set up the iron, put on a podcast and get started*\n")
#Program automatically executes list removal to simulate time passing IRL
creased.popleft()
creased.popleft()
creased.popleft()
#new prompts
sys.stdout.write("*10 minutes later you see that your creased stack is down to:*\n")
show_creased()
#program examines list
#new inputs
sys.stdout.write("*Your partner approaches holding a new item*\n")
sys.stdout.write("What is the new item\n")
#inputs new list item
creased1=("")
creased1=sys.stdin.readline().strip()
sys.stdout.write("Hey do you mind ironing this " +(creased1)+ " for me?\n")
sys.stdout.write("*do you mind? Maybe, but you can't say no to your partner can you*\n")
sys.stdout.write("They place the " +(creased1)+ " on your stack\nYour creased stack is now:\n")
creased.append(creased1)
show_creased()
#new inputs
sys.stdout.write("*You have a nagging feeling that another item that needed to be ironed.. what was it again?*\n")
#inputs new list item
creased2=("")
creased2=sys.stdin.readline().strip()
creased.append(creased2)
#flavour text, shows remaining items in the list
sys.stdout.write("You remember now: " +(creased2)+ " have been added to your stack\n")
sys.stdout.write("*You put on another podcast to get through the rest of the stack*\n")
show_creased()
sys.stdout.write("It's going to be a long day..you've still got some ironing ahead")
   
    
main()



 

