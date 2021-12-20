import sys


#SSD Sales
#SSDSizes, Stored as INT list for math referencing
SSDSizes=[128,256,512,1000,2000]
#Variable for price per GB - created as variable so price can be altered
#Variable also required for assignment criteria
PricesPerGB=3
#Introductory preamble. Sys.stdout.write used as part of assignment marking criteria
sys.stdout.write("Hi There! Welcome to Pythons SSD Sales service\n\
Our SSD's come in a range of sizes:\n")
#For loop used to create clean listing or SSDSizes
for s in SSDSizes:
    sys.stdout.write ("\n-"+str(s)+"GB")
sys.stdout.write("\nWhich size would you like to buy?(Please enter a number)\n")
#Input to allow user to have input into program through shell
Purchased=int(sys.stdin.readline())
#Variable#2, This variable will multiply the users input of desired SSD size by the PricesPerGB value as defined above
PurchasedPrice=[Purchased*PricesPerGB]
#IF statement to include or exclude correct or incorrect values
if Purchased in SSDSizes:
    sys.stdout.write("You've selected the "+str(Purchased)+"GB model. This will cost:")
#For statement to create new variable to be used in displaying final purchase price using Purchased*PricePerGB values
#Alternatively, could have used simple sys.stdout.write (PurchasedPrice)
    for pp in PurchasedPrice:
        sys.stdout.write("$"+str(pp))
        sys.stdout.write("\nHere is your receipt.\nThanks for shopping with Pythons SSD Sales Service!")
#If incorrect values inputted by user that doesnt correspond to SSDSizes value the else statement and while loop will be closed.
else:
    while Purchased not in SSDSizes:
        sys.stdout.write("We do not stock that size.")
        break

