#import sys
#back of house. Has the inner workings of the dealership/one big inventory.

#Creates Init and assigns a List Value
#This list houses all the cars sold by Snakes Car Dealership
def init():
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

#Purchasing option for the user
#This code interacts with the front end system - removing the user purchase,
#checked against the list and then updating the list with the depopulated vehicle.
#returns purchased vhicle to the user.
def Buy_option(user_purchase,snakes_car_stocklist):
    snakes_car_stocklist.remove(user_purchase)
    return "The "+user_purchase+" has now been removed from our stock list.\nRemember to upsell insurance and extended warranties.\n"

#Trade in option for the user, "sells" a car to the dealership
#This section adds user input to the program and then adds that input to the list of
#available stock at the dealership.
#returns the input to the user.
def Trade_option(user_trade_in,snakes_car_stocklist):
    snakes_car_stocklist.append(user_trade_in)
    return "We will happily purchase your "+user_trade_in+".\nPlease browse our stock if you'd like to use the value of your trade-in\nto purchase a new vehicle."

                            
        
