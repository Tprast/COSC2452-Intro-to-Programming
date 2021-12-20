# Car Dealer

import sys
import random

list=['Mazda','Toyota','Subaru','Ford','Holden']
intlist=[123,2654,3156,4332,5873,64357,7363,8097,91245,105544,1183524,5345612]
sys.stdout.write("Our cars today: \n")
for x in list:
   print(x)
sys.stdout.write('What is your name?\n')
name=input()
name=name.capitalize()
sys.stdout.write('What car do you want to buy?\n')
choice = input()
choice=choice.capitalize()

if choice in list:
   sys.stdout.write('Ok!')
   sys.stdout.write(" Thanks for your visit,"+str(name)+". Take your " +str(choice)+"\n" )
   randListNum=random.choice(intlist)
   sys.stdout.write("Your plate number is :" + str(randListNum) +"\n")
else:
   while choice not in list:
      sys.stdout.write('Print car brand from the list : ')
      choice = input()
      choice=choice.capitalize()
      if choice in list:
        sys.stdout.write('Ok!')
        sys.stdout.write("Thanks for your visit,"+str(name)+". Take your " +str(choice)+"\n")
        randListNum=random.choice(intlist)
        sys.stdout.write("Your plate number is :" + str(randListNum) +"\n")
