
import sys
import colorama
from colorama import Fore
from functions import (price, welcome, show_plan, show_dish, show_drink, select_plan, select_dish, select_drink)
import time
colorama.init(autoreset=True)


# Main 
def main():
    welcome()
    show_plan()
    # Choose a plan
    user_menu = select_plan()
    print("Please choose one of the main dish from here.")

    show_dish()
    # Choose a main dish
    user_dish = select_dish()


    print("Would you like to add alcoholic?")
    show_drink()
    # Choose a drink
    user_drink = select_drink()

    allergy = input("Please fill out your food allergies if you have:\n")

    print("\nPlease comfirm your plan\n")
    time.sleep(1)
    print(f"*** {user_menu} ***")
    print(f"Main Dish : {user_dish}")
    print(f"Alcoholic : {user_drink}")
    print(f"Food allergy: {allergy}")
    print(f"Your total price : ${sum(price)}\n")
    time.sleep(1)
    print("Would you like to try again?\n")

    end()

# users select to try again or exit
def end():
    while True:
        user_exit = input("Please press y/n: ")
        if user_exit.lower() == 'y':
            price.clear()
            main()
        elif user_exit.lower() == 'n':
            print("Thank you for choosing us.")
            sys.exit(0)
            
        else:
            print(Fore.RED + "Something went wrong. Please try again")
            sys.exit(1)

if __name__ == "__main__":
    main()