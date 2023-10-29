# import main
import pyfiglet
import time
from colorama import Fore

# Calculate total price

price = []

# Plans
# There are 3 types of menu which include id, menu and price
# It is easy to see, add and remove items
# These prices and name of menus are linked other functions
# So just changing here will be reflected in other functions
# And also there are main dish menu and drink menu as well

plan1 = {"id": 1, "menu": "Chinese Food", "price": 100}
plan2 = {"id": 2, "menu": "Mexican Food", "price": 150}
plan3 = {"id": 3, "menu": "Thai Food", "price": 200}


def plan(id, menu, price):
    print(f"Press: {id}")
    print(menu)
    print(f"${price}")
    print("------------")

# Main dishes

dish1 = {"id": 1, "menu": "Crispy Fried Chicken", "price": 0}
dish2 = {"id": 2, "menu": "Roasted Pork Belly", "price": 20}
dish3 = {"id": 3, "menu": "Angus Beef Steak", "price": 40}


def dish(id, menu, price):
    print(f"Press: {id}")
    print(menu)
    print(f"${price}")
    print("------------")


# Drinks

drink1 = {"id": 1, "menu": "Nothing", "price": 0}
drink2 = {"id": 2, "menu": "Beer", "price": 20}
drink3 = {"id": 3, "menu": "Beer Wine Sake", "price": 40}


def drink(id, menu, price):
    print(f"Press: {id}")
    print(menu)
    print(f"${price}")
    print("------------")


# This function expresses the title of this application
# And also it shows the 3 types of details of the menus
# feature 1

def welcome():
    print(pyfiglet.figlet_format("Catering services for your party"))
    print(Fore.LIGHTGREEN_EX +"Please check our catering menus and price list\n"
        "After selecting menus, you can check the total price\n")
    print(f"Our {plan1['menu']} menu includes spring rolls, Gyozas, Dim-Sum and Pudding\n")
    print(f"Our {plan2['menu']} menu includes TACOS, Burritos, Pozole and Corn Cake\n")
    print(f"Our {plan3['menu']} menu includes Pad Thai, Som Tum, Tom Yum Goong and Roti\n")

# feature 1

def show_plan():
    time.sleep(.5)
    plan(**plan1)
    plan(**plan2)
    plan(**plan3)

def show_dish():
    time.sleep(.5)
    dish(**dish1)
    dish(**dish2)
    dish(**dish3)

def show_drink():
    time.sleep(.5)
    drink(**drink1)
    drink(**drink2)
    drink(**drink3)

# Plans
# Users select one of the menu by pressing the number [1 or 2 or 3]
# feature 2

def select_plan():

    while True:
        user_num = input("Please press the number: ")
        if user_num == "1":
            price.append(plan1["price"])
            return plan1["menu"]
        elif user_num == "2":
            price.append(plan2["price"])
            return plan2["menu"]
        elif user_num == "3":
            price.append(plan3["price"])
            return plan3["menu"]
        else:
            print(Fore.RED + "Something went wrong. Please try again")

# Main dish
# Users select one of the main dish by pressing the number [1 or 2 or 3]

def select_dish():

    while True:
        user_num = input("Please press the number: ")
        if user_num == "1":
            price.append(dish1["price"])
            return dish1["menu"]
        elif user_num == "2":
            price.append(dish2["price"])
            return dish2["menu"]
        elif user_num == "3":
            price.append(dish3["price"])
            return dish3["menu"]
        else:
            print(Fore.RED + "Something went wrong. Please try again")

# Drinks
# Users select one of the drink menu by pressing the number [1 or 2 or 3]

def select_drink():

    while True:
        user_num = input("Please press the number: ")
        if user_num == "1":
            price.append(drink1["price"])
            return drink1["menu"]
        elif user_num == "2":
            price.append(drink2["price"])
            return drink2["menu"]
        elif user_num == "3":
            price.append(drink3["price"])
            return drink3["menu"]
        else:
            print(Fore.RED + "Something went wrong. Please try again")






