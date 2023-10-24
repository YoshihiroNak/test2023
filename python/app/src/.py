import sys

class Calculation:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return f"Your total price is ${self.balance}"

plans = {}

def budget():
    print("*** Welcome to the catering services for your party! ***\n")
    print("Please choose your budget for your party\n")
    print("$100 Chinese food, Press '1'\n")
    print("$150 Mexican food, Press '2'\n")
    print("$200 Thai food, Press '3'\n")

def select_menu(price, food_name):
    user_plan = input("Please press the number: ")
    if user_plan in ('1', '2', '3'):
        plans["food"] = food_name
        user.deposit(price)
    else:
        print("Something went wrong. Please try again")

def chinese_food():
    print("*** Chinese food ***\n")
    print("Our Chinese food menus include spring rolls, dumplings, and dim-sum.\n")
    print("Please select your main dish\n")
    print("[+$0] Chicken Fried Rice, Press '1'\n")
    print("[+$20] Char Siu Pork, Press '2'\n")
    print("[+$40] Mongolian Beef, Press '3'\n")
    select_menu(100, "Chinese food")

def mexican_food():
    print("*** Mexican food ***\n")
    print("Our Mexican food menus include TACOS, Burritos, and Pozole.\n")
    print("Please select your main dish\n")
    print("[+$0] Mexican Lime Chicken, Press '1'\n")
    print("[+$20] Pork Carnitas, Press '2'\n")
    print("[+$40] Barbacoa Beef, Press '3'\n")
    select_menu(150, "Mexican food")

def thai_food():
    print("*** Thai food ***\n")
    print("Our Thai food menus include Pad Thai, Som Tum, and Tom Yum Goong.\n")
    print("Please select your main dish\n")
    print("[+$0] Thai Fried Chicken, Press '1'\n")
    print("[+$20] Thai Basil Pork Belly, Press '2'\n")
    print("[+$40] Pad Gra Prow, Press '3'\n")
    select_menu(200, "Thai food")

def select_dessert(dessert_name):
    chi_des = input("Please press y/n: ")
    if chi_des.lower() == 'y':
        user.deposit(10)
        plans["dessert"] = dessert_name
    elif chi_des.lower() == 'n':
        plans["dessert"] = None
    else:
        print("Something went wrong. Please try again")

def dessert1():
    print("\nWould you like to add DESSERTS?\n")
    print("[+$10] Tofu Pudding\n")
    select_dessert("Tofu Pudding")

def dessert2():
    print("\nWould you like to add DESSERTS?\n")
    print("[+$10] Sweet Mexican corn cake\n")
    select_dessert("Sweet Mexican corn cake")

def dessert3():
    print("\nWould you like to add DESSERTS?\n")
    print("[+$10] Banana Roti\n")
    select_dessert("Banana Roti")

def select_alcohol(alcohol_name):
    chi_des = input("Please press y/n: ")
    if chi_des.lower() == 'y':
        user.deposit(30)
        plans["alcohol"] = alcohol_name

def alcohol():
    print("\nalcohol\n")
    print("[+$30] BEER, WINE, SAKE\n")
    select_alcohol("BEER, WINE, SAKE")

def allergy():
    print("Please fill out your food allergies if you have\n")
    user_allergy = input("Do you have any food allergies?: ")
    print(f"\nYour food allergy: {user_allergy}")
    confirm()

def confirm():
    print("\nPlease confirm your plan\n")
    print(user.get_balance())
    print(f"*** {plans['food']} ***")
    print(f"Main Dish: {plans['main_dish']}")
    print(f"Dessert: {plans['dessert']}")
    print(f"Alcoholic: {plans['alcohol']}")
    end()

def end():
    print("Would you like to try again?\n")
    user_exit = input("Please press y/n: ")
    if user_exit == 'y':
        user.reset_balance()
        plans.clear()
        main()
    elif user_exit == 'n':
        print("Thank you for choosing us.")
        sys.exit(0)
    else:
        print("Thank you for choosing us.")
        sys.exit(1)

def main():
    user = Calculation()
    budget()
    user_plan = input("Please press the number: ")
    if user_plan == '1':
        chinese_food()
    elif user_plan == '2':
        mexican_food()
    elif user_plan == '3':
        thai_food()
    else:
        print("Something went wrong. Please try again")

if __name__ == "__main__":
    main()
