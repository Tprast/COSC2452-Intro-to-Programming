import sys

BeerList=['#1 Nail VPA', '#2 Swan Draught', '#3 Single Fin']
sys.stdout.write("Welcome to your virtual Beer Dispenser!\nPlease enter your age:")
ValidAge=18
Age=int(sys.stdin.readline())
while True:
    if Age>=ValidAge:
        sys.stdout.write ("\nAge verified, You are "+str(Age)+" years old. \nHere is our Beer list:\n"+str(BeerList))
        sys.stdout.write("\nWhich product would you like?(Please enter the number show next to the product)\n")
        break
    elif Age<=ValidAge:
        sys.stdout.write ("\nSorry, You must be over 18 years of age to use the Virtual Beer Dispenser program.")
Selection=int(sys.stdin.readline())
#if len(BeerList)!=(1)(2)(3):
#    sys.stdout.write("Please make a valid selection")
#    sys.stdout.write("\nWhich product would you like?(Please enter the number show next to the product)\n")
if Selection==1:
    sys.stdout.write("You have selected "+str(BeerList[0]))
if Selection==2:
    sys.stdout.write("You have selected "+str(BeerList[1]))
if Selection==3:
    sys.stdout.write("You have selected "+str(BeerList[2]))
        
