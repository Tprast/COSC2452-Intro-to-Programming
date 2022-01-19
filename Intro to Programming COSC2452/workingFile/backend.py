import sys
#back of house. Has the inner workings of the dealership/one big inventory.

#Creates Init and assigns a List Value
#This list houses all the cars sold by Snakes Car Dealership
def init_stock_list():
    snakes_car_stocklist=["Rav4",
                      "Colorado",
                      "HiLux",
                      "Triton",
                      "X-Trail",
                      "CR-V",
                      "Forrester",
                      "Golf",
                      "Ranger",
                      "CX-5",
                      "Landcruiser",
                      "Camry",
                      "Passat",
                      "Lancer",
                      "Imprezza",
                      "Tesla",
                      "Ranger",
                      "Touareg",
                      "Focus",
                      "Escape",
                      "Mustang",
                      "Porsche"]
    return snakes_car_stocklist

def purchased_list():
    purchased_list=[]
    return purchased_list

def traded_list():
    traded_list=[]
    return traded_list

#Purchasing option for the user
#This code interacts with the front end system - removing the user purchase,
#checked against the list and then updating the list with the depopulated vehicle.
#returns purchased vhicle to the user.
def Buy_option(snakes_car_stocklist,user_purchase,user_purchased_list):
    #snakes_car_stocklist.remove(user_purchase)
    user_purchased_list.append(user_purchase)
    return "The "+str(user_purchase)+" has now been removed from our stock list.\nRemember to upsell insurance and extended warranties.\n"

#Trade in option for the user, "sells" a car to the dealership
#This section adds user input to the program and then adds that input to the list of
#available stock at the dealership.
#returns the input to the user.
def Trade_option(snakes_car_stocklist,user_trade_in,user_traded_list):
   #snakes_car_stocklist.append(user_trade_in)
    user_traded_list.append(user_trade_in)
    return "We will happily purchase your "+str(user_trade_in)+".\nPlease browse our stock if you'd like to use the value of your trade-in\nto purchase a new vehicle."

def load_from_file(file_name,user_purchased_list,user_traded_list):
    file_obj=open(file_name,"r")
    
    line=file_obj.readline()
    while(line!=""):
        fields=line.strip().split(",")
        Buy_option(fields[0],user_purchased_list,user_purchased_list)
        Trade_option(fields[1],user_traded_list,user_traded_list)
        line=file_obj.readline()
        
    file_obj.close()

def save_to_file(file_name,user_purchased_list,user_traded_list):
    file_obj=open(file_name,"w")
    len_records=len(user_traded_list)
    len_records2=len(user_purchased_list)
    output=""
    index=0
    while(index<len_records):
        output+=str(user_traded_list[index])+","+str(user_purchased_list[index])+"\n"
        index+=1
        
    file_obj.write(output)
    
    file_obj.close()
        
