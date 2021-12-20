import sys

sys.stdout.write("Welcome to your friendly outfit suggestor.\n"
"In celsius, What is the current temperature today?\n")
Plus25=['T-shirt','shoes','shorts','hat']
Minus25=['T-Shirt','Jacket','Shoes','Jeans']

weather=int(sys.stdin.readline())
if weather>=25:
    sys.stdout.write("I would suggest "+str(Plus25)+" for "+str(weather)+" degrees")
if weather<=25:
   sys.stdout.write("I would suggest "+str(Minus25)+" for "+str(weather)+" degrees")

    
