# import pyfiglet
import colorama
from colorama import Fore

colorama.init(autoreset=True)
# from tenacity import retry, stop_after_attempt


# Plans

plan1 = {"id": 1, "menu": "Chinese Food", "price": 100}

plan2 = {"id": 2, "menu": "Mexican Food", "price": 150}

plan3 = {"id": 3, "menu": "Thai Food", "price": 200}


def plan(id, menu, price):
    print(f"Press: {id}")
    print(menu)
    print(f"${price}")

# Main dishes

dish1 = {"id": 1, "menu": "Crispy Fried Chicken", "price": 0}

dish2 = {"id": 2, "menu": "Roasted Pork Belly", "price": 20}

dish3 = {"id": 3, "menu": "Angus Beef Steak", "price": 40}


def dish(id, menu, price):
    print(f"Press: {id}")
    print(menu)
    print(f"${price}")

# Drinks

drink1 = {"id": 1, "menu": "Nothing", "price": 0}

drink2 = {"id": 2, "menu": "Beer", "price": 20}

drink3 = {"id": 3, "menu": "Beer Wine Sake", "price": 40}


def drink(id, menu, price):
    print(f"Press: {id}")
    print(menu)
    print(f"${price}")

# Plans

def select_plan():

    while True:
        user_num = input("Please pass the number: ")
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


# Main dishes

def select_dish():

    while True:
        user_num = input("Please pass the number: ")
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

def select_drink():

    while True:
        user_num = input("Please pass the number: ")
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

# Calculate total price
price = []

# Main

print("Welcome")
# print(pyfiglet.figlet_format("Catering services for your party!"))
print(f"Our {plan1['menu']} menus include spring rolls, dumplings, dim-sum and Tofu Pudding.\n")
print(f"Our {plan2['menu']}  menus include TACOS, Burritos, Pozole and Sweet Mexican corn cake.\n")
print(f"Our {plan3['menu']} menus include Pad Thai, Som Tum, Tom Yum Goong and Banana Roti.\n")

plan(**plan1)
plan(**plan2)
plan(**plan3)

# Choose a plan
user_menu = select_plan()

# print(Fore.RED + "Something went wrong. Please try again")
print("Please choose one of the main dish from here.")

dish(**dish1)
dish(**dish2)
dish(**dish3)

# Choose a main dish
user_dish = select_dish()

#         print(Fore.RED + "Something went wrong. Please try again")

print("Would you like to add alcoholic?")

drink(**drink1)
drink(**drink2)
drink(**drink3)

user_drink = select_drink()

allergy = input("Please fill out your food allergies if you have:\n")

print("\nPlease comfirm your plan\n")
# print(user_menu)
# print(user_dish)
# print(allergy)
# print(sum(price))
print(f"*** {user_menu} ***")
print(f"Main Dish : {user_dish}")
print(f"Alcoholic : {user_drink}")
print(f"Food allergy: {allergy}")
print(f"Your total price : ${sum(price)}")

