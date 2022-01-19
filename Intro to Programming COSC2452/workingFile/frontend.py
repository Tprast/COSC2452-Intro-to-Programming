import sys
#show-room, frontend interacts with the user
import backend





#Form break + menu break are used in formatting for list sections.
#The below variables being assigned.
form_break="\n\
_______________________________________________________________________________\n"
menu_break="\n\
-------------------------------------------------------------------------------\n"

#establishes the main menu for the program to run.
def main():
    snakes_car_stocklist=backend.init_stock_list()
    user_purchased_list=backend.purchased_list()
    user_traded_list=backend.traded_list()
    
    
    
    
     
    menu =""+menu_break+""
    menu+="\nDEALERSHIP MENU\n"+menu_break+""
    menu+="[S]TOCK: Cars for Purchase"+menu_break+""
    menu+="[B]UY: Buy a vehicle from our stocklist"+menu_break+""
    menu+="[T]RADE: Trade-in a vehicle to Snakes Dealership"+menu_break+""
    menu+="[L]oad saved file"+menu_break+""
    menu+="[C]lose program"+menu_break+""
    menu+="\nOPTION:\n"
    sys.stdout.write(menu)
    choice = sys.stdin.readline().strip()

    while(choice!="C"):
#STOCK LIST
#Repeats the value from def init/snakes_car_stocklist back to the user,
#and presents the list in a simple and easy to read manner.
        if (choice=="S"):
            sys.stdout.write("Cars available to purchase at Snakes Dealership:"+form_break+"\n")
            for c in snakes_car_stocklist:
                sys.stdout.write(f"{c.ljust(10)}\n")
                
#BUY = REMOVE ITEM FROM LIST
#Removes items from the pre-established list.
#Allows user to select which vehicle to "purchase" and therefore remove from the list.
        elif (choice=="B"):
            sys.stdout.write("\nwhich car would you like to purchase from our stock list:\n")
            user_purchase=sys.stdin.readline().strip()
            Buy_selected=backend.Buy_option(snakes_car_stocklist,user_purchase,user_purchased_list)
           

            sys.stdout.write(Buy_selected)
           

#TRADE = ADD ITEM TO LIST
#Allows the user to "sell" a vehicle to the dealership, effectively "adding" an item to the list.
#Interacts with the .backend and adds to vehicle to the dealership list.
        elif (choice=="T"):
            sys.stdout.write("\nLooking to trade in your car?\
 Please tell us the Model of your vehicle:\n")
            user_trade_in=sys.stdin.readline().strip()
            trade_in_selected=backend.Trade_option(snakes_car_stocklist,user_trade_in,user_traded_list)
            sys.stdout.write(trade_in_selected)

        elif (choice=="L"):
                try:
                        file_name="my_carstocklist.csv"
                        backend.load_from_file(file_name,user_purchased_list,user_traded_list)
                except:
                        sys.stdout.write("That file, "+file_name+" does not exist, could not be opened or found.. \nTry again..")
            
            
#cycles back to menu when invalid options are given to the program.           
        else:
            sys.stdout.write("Invalid choice!\n")

        sys.stdout.write(menu)
        choice=sys.stdin.readline().strip()
    try:
            file_name=("my_carstocklist.csv")
            backend.save_to_file("car_stocklist.csv",user_purchased_list,user_traded_list)
    except:
            sys.stdout.write("That file, "+file_name+" does not exist, could not be opened or found.. \nTry again..")



main()
            
