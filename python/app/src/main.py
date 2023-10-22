import sys

class Calculation:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return print(self.balance)
    

user = Calculation(balance=0)
# balance = 0
# user.deposit(100)
# user.deposit(100)
user.get_balance()


# display a main
# display shows up when the user clicks
# Need to make it easy to see



def welcome():
    print("")
    print("*** Welcome to the catering services for your party! ***")
    print("")
    print("Would you like to have a look?")
    print("")
    user_select = input("Please press y/n: ")
    if user_select == "y":
        description()
    elif user_select == "n":
        print("Thank you very much")
        sys.exit(0)
    else:
        print("Something went wrong")

    budget()
# Amount function







# description
# More information for user to understand our service easily
def description():
    pass
# Budget checking
def budget():
    print("Please choose your budget for your party")
    print("")
    print("")
    print("$ 100 Chinese food, Press '1'")
    print("")
    print("$ 150 Mexican food, Press '2'")
    print("")
    print("$ 200  Thai  food,  Press '3'")
    print("")
    plan()

# choose a plan
# Need to make error handling
def plan():
    # while True:
        user_plan = input("Please press the number: ")
        total_price = 0
        if user_plan == '1':
            # total_price(100)
            # print(total_price)
            user.deposit(100)
            user.get_balance()
            chinese_food()
            # $100
        elif user_plan == '2':
            # total_price(150)
            # print(total_price)
            user.deposit(150)
            user.get_balance()
            mexicon_food()
            # $150
        elif user_plan == '3':
            # total_price(200)
            # print(total_price)
            user.deposit(200)
            user.get_balance()
            thai_food()
            # $200
        else:
            print("Something went wrong. Please try again")
            # try_again = input("Please press y/n: ")
            # if try_again == 'y':
            # break
        # print("Something went wrong. Please try again")
            # return print("Something went wrong. Please try again")



# Chinese food function
# Need to make error handling
# Need to create '2' and '3'
# Need to calculate
def chinese_food():
    # while True:
        print()
        print("")
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
        user_dish = input("Please press the number: ")

        if user_dish == '1':
            user.get_balance()
            option1()
            # $100
        elif user_dish == '2':
            user.deposit(20)
            user.get_balance()
            option1()
            # #120
        elif user_dish == '3':
            user.deposit(40)
            user.get_balance()
            option1()
            # $140
        else:
            print("Something went wrong. Please try again")
# Mexico food function
def mexicon_food():
    # while True:
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

        user_dish = input("Please press the number: ")

        if user_dish == '1':
            user.get_balance()
            option2()
            # $150
        elif user_dish == '2':
            user.deposit(20)
            user.get_balance()
            option2()
            # $170
        elif user_dish == '3':
            user.deposit(40)
            user.get_balance()
            option2()
            # $190
        else:
            print("Something went wrong. Please try again")

# Thai food function
def thai_food():
    # while True:
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

        user_dish = input("Please press the number: ")

        if user_dish == '1':
            user.get_balance()
            option3()
            # $200
        elif user_dish == '2':
            user.deposit(20)
            user.get_balance()
            option3()
            # $220
        elif user_dish == '3':
            user.deposit(40)
            user.get_balance()
            option3()
            # $240
        else:
            print("Something went wrong. Please try again")
# choose a main
def dish():

        pass
# choose option
def option1():
    # while True:
        print("")
        print("Would you like to add DESSERTS?")
        user_opt = input("Please press y/n: ")
        if user_opt.lower() == 'y':
            dessert1()
        elif user_opt.lower() == 'n':
            a_option()
        else:
            print("Something went wrong. Please try again")

def option2():
    # while True:
        print("")
        print("Would you like to add DESSERTS?")
        user_opt = input("Please press y/n: ")
        if user_opt.lower() == 'y':
            dessert2()
        elif user_opt.lower() == 'n':
            a_option()
        else:
            print("Something went wrong. Please try again")

def option3():
    # while True:
        print("")
        print("Would you like to add DESSERTS?")
        user_opt = input("Please press y/n: ")
        if user_opt.lower() == 'y':
            dessert3()
        elif user_opt.lower() == 'n':
            a_option()
        else:
            print("Something went wrong. Please try again")

# desserts
def dessert1():
    # while True:
        print("")
        print("[+$10] Tofu Pudding")
        # chinese dessert inputs
        chi_des = input("Please press y/n: ")
        if chi_des.lower() == 'y':
            user.deposit(10)
            user.get_balance()
            a_option()
        elif chi_des.lower() == 'n':
            a_option()
        else:
            print("Something went wrong. Please try again")

    # Mixican dessert inputs
def dessert2():
    # while True:
        print("")
        print("[+$10] Sweet Mexican corn cake")

        chi_des = input("Please press y/n: ")
        if chi_des.lower() == 'y':
            user.deposit(10)
            user.get_balance()
            a_option()
        elif chi_des.lower() == 'n':
            a_option()
        else:
            print("Something went wrong. Please try again")

    # Thai dessert inputs
def dessert3():
    # while True:
        print("")
        print("[+$10] Banana Roti")

        chi_des = input("Please press y/n: ")
        if chi_des.lower() == 'y':
            user.deposit(10)
            user.get_balance()
            a_option()
        elif chi_des.lower() == 'n':
            a_option()
        else:
            print("Something went wrong. Please try again")
# choose another option
def a_option():
    # while True:
        print("")
        print("Would you like to add alcoholic?")
        user_a_opt = input("Please press y/n: ")
        if user_a_opt.lower() == 'y':
            alcohol()
        elif user_a_opt.lower() == 'n':
            allergy()
        else:
            print("Something went wrong. Please try again")
# alcoholic

def alcohol():
    # while True:
        print("")
        print("alcohol")
        print("[+$30] BEER, WINE, SAKE")
        # chinese dessert inputs
        chi_des = input("Please press y/n: ")
        if chi_des.lower() == 'y':
            user.deposit(30)
            user.get_balance()
            allergy()
        elif chi_des.lower() == 'n':
            allergy()
        else:
            print("Something went wrong. Please try again")
    # fill allergy
    # Input form


def  allergy():
    
    print("")
    print("Please fill out your food allergies if you have")
    user_allergy = input("Do you have any food allergies?: ")
    print("")
    print(f"Your food allergy: {user_allergy}")
    conform()



# conform display
# Need to be with plan and total
def conform():
    print("")
    print("Please comfirm your plan")
    # print(total_price)
    user.get_balance()
    print("")
    end()

# try again or exit
def end():
        print("Would you like to try again?")
        user_exit = input("Please press y/n: ")
        if user_exit == 'y':
            welcome()
        elif user_exit == 'n':
            print("")
            print("Thank you for choosing us.")
            sys.exit(0)
            
            
            
        else:
            print("Thank you for choosing us.")
            sys.exit(1)
            
            
welcome()
