import sys


#SSD Sales
#SSDSizes, Stored as INT list for math referencing
SSDSizes=[128,256,512,1000,2000]
#Variable for price per GB - created as variable so price can be altered
PricesPerGB=3
sys.stdout.write("Hi There! Welcome to Pythons SSD Sales service\n\
Our SSD's come in a range of sizes:\n")
for s in SSDSizes:
    sys.stdout.write ("\n-"+str(s)+"GB")
sys.stdout.write("\nWhich size would you like to buy?(Please enter a number)\n")
Purchased=int(sys.stdin.readline())
PurchasedPrice=[Purchased*PricesPerGB]
if Purchased in SSDSizes:
    sys.stdout.write("You've selected the "+str(Purchased)+"GB model. This will cost:")
    for pp in PurchasedPrice:
        sys.stdout.write("$"+str(pp))
        sys.stdout.write("\nHere is your receipt.\nThanks for shopping with Pythons SSD Sales Service!")
else:
    while Purchased not in SSDSizes:
        sys.stdout.write("We do not stock that size.")
        break

