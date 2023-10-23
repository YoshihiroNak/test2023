import sys
import pyfiglet

# Calclaration
class Calculation:
    def __init__(self, balance):
        self.balance = balance

    def price(self, amount):
        self.balance += amount

    def get_balance(self):
        return print(f"Your total prine is ${self.balance}")
    
    def reset_balance(self):
        self.balance = 0

plans = {}

user = Calculation(balance=0)

# main
def main():
    budget()
    while True:
        user_plan = input("Please press the number: ")
        if user_plan == '1':
            plans["food"] = 'Chinese food'
            user.price(100)
            chinese_food()
        elif user_plan == '2':
            plans["food"] = 'Mexican food'
            user.price(150)    
            mexicon_food()
        elif user_plan == '3':
            plans["food"] = 'Thai food'
            user.price(200)
            thai_food()
        else:
            print("Something went wrong. Please try again")

# Budget checking
def budget():
    print(pyfiglet.figlet_format("Welcome to the catering services for your party!"))
    
    print("Please choose your budget for your party"
    "\n"
    "\n"
    "$ 100 Chinese food, Press '1'\n"
    "\n"
    "$ 150 Mexican food, Press '2'\n"
    "\n"
    "$ 200  Thai  food,  Press '3'\n"
    )

def chinese_food(): # Chinese food function
        print("*** Chinese food ***")
        print("***")
        print("Our Chinese food menus include spring rolls, dumplings and dim-sum.")
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
                user.get_balance()
                # plans.append("Chicken Fried Rice")
                plans["main_dish"] = "Chicken Fried Rice"
                dessert1()
                # $100
            elif user_dish == '2':
                user.price(20)
                # plans.append("Char Siu Park")
                plans["main_dish"] = "Char Siu  Pork"
                dessert1()
                # #120
            elif user_dish == '3':
                user.price(40)
                # plans.append("Mongolian Beef")
                plans["main_dish"] = "Mongolian Beef"
                dessert1()
                # $140
            else:
                print("Something went wrong. Please try again")


def mexicon_food(): # Mexico food function
        print("*** Mexican food ***")
        print("***")
        print("Our Mexican food menus include TACOS, Burritos and Pozole.")
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
                user.get_balance()
                plans["main_dish"] = "Mexican Lime Chicken"
                dessert2()
            elif user_dish == '2':
                user.price(20)
                plans["main_dish"] = "Pork Carnitas"
                dessert2()
            elif user_dish == '3':
                user.price(40)
                plans["main_dish"] = "]Barbacoa Beef"
                dessert2()
            else:
                print("Something went wrong. Please try again")

def thai_food(): # Thai food function
        print("*** Thai food ***")
        print("***")
        print("Our Thai food menus include Pad Thai, Som Tum and Tom Yum Goong.")
        print("***")
        print("Please select your main dish")
        print("")
        print("[+$0]Thai Fried Cheiken, Press '1'")
        print("")
        print("[+$20]Thai Basil Pork Belly, Press '2'")
        print("")
        print("[+$40]Pad Gra Prow,  Press '3'")
        print("")
        # select_menu(200, "Thai food")
        while True:

            user_dish = input("Please press the number: ")

            if user_dish == '1':
                user.get_balance()
                plans["main_dish"] = "Thai Fried Cheiken"
                dessert3()

            elif user_dish == '2':
                user.price(20)
                plans["main_dish"] = "Thai Basil Pork Belly"
                dessert3()

            elif user_dish == '3':
                user.price(40)
                plans["main_dish"] = "Pad Gra Prow"
                dessert3()

            else:
                print("Something went wrong. Please try again")


def dessert1(): # chinese dessert input
        print("")
        print("Would you like to add DESSERTS?")
        print("[+$10] Tofu Pudding")
        # chinese dessert inputs
        while True:

            chi_des = input("Please press y/n: ")
            if chi_des.lower() == 'y':
                user.price(10)
                plans["dessert"] = "Tofu Pudding"
                a_option()
            elif chi_des.lower() == 'n':
                plans["dessert"] = None
                a_option()
            else:
                print("Something went wrong. Please try again")


def dessert2():   # Mixican dessert inputs
        print("")
        print("Would you like to add DESSERTS?")
        print("[+$10] Sweet Mexican corn cake")
        while True:

            chi_des = input("Please press y/n: ")
            if chi_des.lower() == 'y':
                user.price(10)
                plans["dessert"] = "Sweet Mexican corn cake"
                a_option()
            elif chi_des.lower() == 'n':
                plans["dessert"] = None
                a_option()
            else:
                print("Something went wrong. Please try again")


def dessert3():   # Thai dessert input
        print("")
        print("Would you like to add DESSERTS?")
        print("[+$10] Banana Roti")
        while True:

            chi_des = input("Please press y/n: ")
            if chi_des.lower() == 'y':
                user.price(10)
                plans["dessert"] = "Banana Roti"
                a_option()
            elif chi_des.lower() == 'n':
                plans["dessert"] = None
                a_option()
            else:
                print("Something went wrong. Please try again")

# choose another option
def a_option():
        print("")
        print("Would you like to add alcoholic?")
        while True:

            user_a_opt = input("Please press y/n: ")
            if user_a_opt.lower() == 'y':
                alcohol()
            elif user_a_opt.lower() == 'n':
                plans["alcohol"] = None
                allergy()
            else:
                print("Something went wrong. Please try again")



def alcohol():
        print("")
        print("[+$30] BEER, WINE, SAKE")
        while True:

            chi_des = input("Please press y/n: ")
            if chi_des.lower() == 'y':
                user.price(30)
                plans["alcohol"] = "BEER, WINE, SAKE"
                allergy()
            elif chi_des.lower() == 'n':
                plans["alcohol"] = None
                allergy()
            else:
                print("Something went wrong. Please try again")

def  allergy():
    
    print("Please fill out your food allergies if you have\n")
    plans["allergy"] = input("Do you have any food allergies?: ")
    confirm()


def confirm():
    print("\nPlease comfirm your plan\n")
    user.get_balance()
    print(f"*** {plans["food"]} ***")
    print(f"Main Dish : {plans["main_dish"]}")
    print(f"Dessert : {plans["dessert"]}")
    print(f"Alcoholic : {plans["alcohol"]}")
    print(f"Food allergy: {plans["allergy"]}")
    end()

# try again or exit
def end():
        print("Would you like to try again?\n")
        user_exit = input("Please press y/n: ")
        if user_exit == 'y':
            user.reset_balance()
            plans.clear()
            main()

        elif user_exit == 'n':
            print("")
            print("Thank you for choosing us.")
            sys.exit(0)
            
        else:
            print("Thank you for choosing us.")
            sys.exit(1)


if __name__ == "__main__":
    main()
