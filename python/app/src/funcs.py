
import sys
import pyfiglet
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


plans = {}
price = []


# Main
def budget():
    print(pyfiglet.figlet_format("Catering services for your party!"))
    
    print("Please choose your budget for your party"
    "\n"
    "$ 100 Chinese food, Press '1'\n"
    "\n"
    "$ 150 Mexican food, Press '2'\n"
    "\n"
    "$ 200  Thai  food,  Press '3'\n"
    )
    # while True:
    #     user_plan = input("Please press the number: ")
    #     if user_plan == '1':
    #         plans["food"] = 'Chinese food'
    #         price.append(100)
    #         chinese_food() #
    #         # return user_plan
    #     elif user_plan == '2':
    #         plans["food"] = 'Mexican food'
    #         price.append(150)
    #         mexicon_food() #
    #         # return user_plan

    #     elif user_plan == '3':
    #         plans["food"] = 'Thai food'
    #         price.append(200)
    #         thai_food() #
    #         # return user_plan

    #     else:
    #         print(Fore.RED + "Something went wrong. Please try again")

def main_dish(): # Chinese food function
        print("Please select your main dish")
        print("")
        print("[+$0]Crispy Fried Chicken, Press '1'")
        print("")
        print("[+$20]Roasted Pork Belly, Press '2'")
        print("")
        print("[+$40]Angus Beef Steak,  Press '3'")
        print("")

def chinese_food(): # Chinese food function
        print("*** Chinese food ***")
        print("***")
        print("Our Chinese food menus include spring rolls, dumplings, dim-sum and Tofu Pudding.")
        print("***")
        print("Please select your main dish")
        print("")
        print("[+$0]Chicken Fried Rice, Press '1'")
        print("")
        print("[+$20] Char Siu  Pork, Press '2'")
        print("")
        print("[+$40]  Mongolian Beef,  Press '3'")
        print("")
        while True:
    
            user_dish = input("Please press the number: ")

            if user_dish == '1':
                plans["main_dish"] = "Chicken Fried Rice"
                # dessert1()
                alcohol()
                # $100
            elif user_dish == '2':
                price.append(20)
                plans["main_dish"] = "Char Siu  Pork"
                # dessert1() #
                alcohol() #
                # #120
            elif user_dish == '3':
                price.append(40)
                plans["main_dish"] = "Mongolian Beef"
                # dessert1() #
                alcohol() #
                # $140
            else:
                print(Fore.RED + "Something went wrong. Please try again")


def mexicon_food(): # Mexico food function
        print("*** Mexican food ***")
        print("***")
        print("Our Mexican food menus include TACOS, Burritos, Pozole and Sweet Mexican corn cake.")
        print("***")
        print("Please select your main dish")
        print("")
        print("[+$0]Mexican Lime Chicken, Press '1'")
        print("")
        print("[+$20] Pork Carnitas, Press '2'")
        print("")
        print("[+$40]Barbacoa Beef,  Press '3'")
        print("")

        while True:

            user_dish = input("Please press the number: ")

            if user_dish == '1':
                plans["main_dish"] = "Mexican Lime Chicken"
                # dessert2() #
                alcohol () #
            elif user_dish == '2':
                price.append(20)
                plans["main_dish"] = "Pork Carnitas"
                # dessert2() #
                alcohol()
            elif user_dish == '3':
                price.append(40)
                plans["main_dish"] = "Barbacoa Beef"
                # dessert2() #
                alcohol()
            else:
                print(Fore.RED + "Something went wrong. Please try again")


def thai_food(): # Thai food function
        print("*** Thai food ***")
        print("***")
        print("Our Thai food menus include Pad Thai, Som Tum, Tom Yum Goong and Banana Roti.")
        print("***")
        print("Please select your main dish")
        print("")
        print("[+$0]Thai Fried Cheiken, Press '1'")
        print("")
        print("[+$20]Thai Basil Pork Belly, Press '2'")
        print("")
        print("[+$40]Pad Gra Prow,  Press '3'")
        print("")

        while True:

            user_dish = input("Please press the number: ")

            if user_dish == '1':
                plans["main_dish"] = "Thai Fried Cheiken"
                # dessert3() #
                alcohol()

            elif user_dish == '2':
                price.append(20)
                plans["main_dish"] = "Thai Basil Pork Belly"
                # dessert3() #
                alcohol()

            elif user_dish == '3':
                price.append(40)
                plans["main_dish"] = "Pad Gra Prow"
                # dessert3() #
                alcohol()

            else:
                print(Fore.RED + "Something went wrong. Please try again")


# def dessert1(): # Chinese dessert input
#         print("")
#         print("Would you like to add DESSERTS?")
#         print("[+$10] Tofu Pudding")

#         while True:

#             chi_des = input("Please press y/n: ")
#             if chi_des.lower() == 'y':
#                 price.append(10)
#                 plans["dessert"] = "Tofu Pudding"
#                 alcohol() #
#             elif chi_des.lower() == 'n':
#                 plans["dessert"] = None #
#                 alcohol() #
#             else:
#                 print(Fore.RED + "Something went wrong. Please try again")


# def dessert2():   # Mixican dessert inputs
#         print("")
#         print("Would you like to add DESSERTS?")
#         print("[+$10] Sweet Mexican corn cake")
#         while True:

#             chi_des = input("Please press y/n: ")
#             if chi_des.lower() == 'y':
#                 price.append(10)
#                 plans["dessert"] = "Sweet Mexican corn cake"
#                 alcohol() #
#             elif chi_des.lower() == 'n':
#                 plans["dessert"] = None #
#                 alcohol() #
#             else:
#                 print(Fore.RED + "Something went wrong. Please try again")


# def dessert3():   # Thai dessert input
#         print("")
#         print("Would you like to add DESSERTS?")
#         print("[+$10] Banana Roti")
#         while True:

#             chi_des = input("Please press y/n: ")
#             if chi_des.lower() == 'y':
#                 price.append(10)
#                 plans["dessert"] = "Banana Roti"
#                 alcohol() #
#             elif chi_des.lower() == 'n':
#                 plans["dessert"] = None #
#                 alcohol() #
#             else:
#                 print(Fore.RED + "Something went wrong. Please try again")


def alcohol():
        print("Would you like to add alcoholic?")
        print("[+$30] BEER, WINE, SAKE")
        while True:

            chi_des = input("Please press y/n: ")
            if chi_des.lower() == 'y':
                plans["alcohol"] = "BEER, WINE, SAKE"
                price.append(30)
                # allergy() #
                break
            elif chi_des.lower() == 'n':
                plans["alcohol"] = None #
                # allergy() #
                break
            else:
                print(Fore.RED + "Something went wrong. Please try again")

def  allergy():
    
    print("Please fill out your food allergies if you have\n")
    plans["allergy"] = input("Do you have any food allergies?: ")
    # confirm() #


def confirm():
    print("\nPlease comfirm your plan\n")
    print(f"Your total price : ${sum(price)}")
    print(f"*** {plans["food"]} ***")
    print(f"Main Dish : {plans["main_dish"]}")
    print(f"Alcoholic : {plans["alcohol"]}")
    print(f"Food allergy: {plans["allergy"]}")
    # end()

# Try again or exit
def end():
        print("Would you like to try again?\n")
        user_exit = input("Please press y/n: ")
        if user_exit == 'y':
            price.clear()
            plans.clear() 
            budget() #

        elif user_exit == 'n':
            print("")
            print("Thank you for choosing us.")
            sys.exit(0)
            
        else:
            print("Thank you for choosing us.")
            sys.exit(1)



# if __name__ == "__main__":
#     budget()