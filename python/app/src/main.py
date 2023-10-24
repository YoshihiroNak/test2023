import funcs
import pyfiglet
import colorama
from colorama import Fore

colorama.init(autoreset=True)


plans = {}
price = []

# print("Welcome")
funcs.budget()
# print("1, chinese, 2, mexican, 3, thai")
while True:
        user_menu = input("Please pass the number: ")

        if user_menu == "1":
                # print("Chinese Main")
                plans["food"] = "Chinese food"
                price.append(100)
        elif user_menu == "2":
                # print("Mexican Main")
                plans["food"] = "Mexican food"
                price.append(150)
        elif user_menu == "3":
                # print("Thai Main")
                plans["food"] = "Thai food"
                price.append(200)
        else:
                print(Fore.RED + "Something went wrong. Please try again")

        funcs.main_dish()
        # print("1, Chicken, 2, Pork, 3, Beef")
        user_dish = input("Please press the number: ")

        if user_dish == "1":
                print("Chicken")
                plans["main_dish"] = "Crispy Fried Chicken"        
        elif user_dish == "2":
                print("Pork")
                plans["main_dish"] = "Roasted Pork Belly"
                price.append(20)
        elif user_dish == "3":
                print("Beef")
                plans["main_dish"] = "Angus Beef Steak"
                price.append(40)
        else:
                print(Fore.RED + "Something went wrong. Please try again")

        print("Would you like to add alcoholic?")

        user_drink = input("Please press y/n: ")

        if user_drink == "y":
                print("Alcohol")
                plans["alcohol"] = "Beer, Wine, Sake"
                price.append(50)
        elif user_drink == "n":
                print("Non alcohol")
                plans["alcohol"] = "Nothing"
        else:
                print(Fore.RED + "Something went wrong. Please try again")
        allergy = input("Please fill out your food allergies if you have:\n")

        print("\nPlease comfirm your plan\n")
        print(f"*** {plans["food"]} ***")
        print(f"Main Dish : {plans["main_dish"]}")
        print(f"Alcoholic : {plans["alcohol"]}")
        print(f"Food allergy: {allergy}")
        print(f"Your total price : ${sum(price)}")


# end()