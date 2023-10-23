import sys

# Calclaration
class Calculation:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return print(f"Your total prine is ${self.balance}")
    
    # def get_plan(self, name):
    #     return print(self.name)
    
    def reset_balance(self):
        self.balance = 0

# class Display:
#     def __init__(self, plan , main_dish, dessert, alcohol):
#         self.plan = plan
#         # self.main_dish = main_dish
#         # self.dessert = dessert
#         # self.alcohol = alcohol
#     def set_plan(self, plan):
#         self.plan = plan
#     def get_plan(self):
#         return print(self.plan)

plans = []

# Set user balance
# balance = 0
# user.deposit(100)
# user.deposit(100)
# user.get_balance()

user = Calculation(balance=0)
# user = Display(plan=None)
# More information for user to understand our service easily

# Budget checking
def budget():
    print(f"\n"
    "*** Welcome to the catering services for your party! ***"
    "\n")

    print("Please choose your budget for your party"
    "\n"
    "\n"
    "$ 100 Chinese food, Press '1'\n"
    "\n"
    "$ 150 Mexican food, Press '2'\n"
    "\n"
    "$ 200  Thai  food,  Press '3'\n"
    "\n"
    )
# Display what user chose at the end
# choose a plan
# Need to make error handling
def plan():
    # while True:
        user_plan = input("Please press the number: ")
        if user_plan == '1':
            plans.append("Chinese food")
            # print(plans)
            user.deposit(100)
            # user = Calculation(name="Cninese")
            chinese_food()
            # $100
        elif user_plan == '2':
            plans.append("Mexican food")
            user.deposit(150)
            mexicon_food()
            # $150
        elif user_plan == '3':
            plans.append("Thai food")
            user.deposit(200)
            thai_food()
            # $200
        else:
            print("Something went wrong. Please try again")


# Display the main what the user chose at the end
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
            plans.append("Chicken Fried Rice")
            dessert1()
            # $100
        elif user_dish == '2':
            user.deposit(20)
            plans.append("Char Siu Park")
            dessert1()
            # #120
        elif user_dish == '3':
            user.deposit(40)
            plans.append("Mongolian Beef")
            dessert1()
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
            plans.append("Mexican Lime Chicken")
            dessert2()
            # $150
        elif user_dish == '2':
            user.deposit(20)
            plans.append("Pork Carnites")
            dessert2()
            # $170
        elif user_dish == '3':
            user.deposit(40)
            plans.append("Barbacoa Beef")
            dessert2()
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
            plans.append("Thai Fried Cheiken")
            dessert3()
            # $200
        elif user_dish == '2':
            user.deposit(20)
            plans.append("Thai Basil Pork Belly")
            dessert3()
            # $220
        elif user_dish == '3':
            user.deposit(40)
            plans.append("Pad Gra Prow")
            dessert3()
            # $240
        else:
            print("Something went wrong. Please try again")
# choose a main
def dish():

        pass

# Display the deseert what the user entered
# desserts
def dessert1():
    # while True:
        print("")
        print("Would you like to add DESSERTS?")
        print("[+$10] Tofu Pudding")
        # chinese dessert inputs
        chi_des = input("Please press y/n: ")
        if chi_des.lower() == 'y':
            user.deposit(10)
            plans.append("Tofu Pudding")
            a_option()
        elif chi_des.lower() == 'n':
            a_option()
        else:
            print("Something went wrong. Please try again")

    # Mixican dessert inputs
def dessert2():
    # while True:
        print("")
        print("Would you like to add DESSERTS?")
        print("[+$10] Sweet Mexican corn cake")

        chi_des = input("Please press y/n: ")
        if chi_des.lower() == 'y':
            user.deposit(10)
            plans.append("Sweet Mexican corn cake")
            a_option()
        elif chi_des.lower() == 'n':
            a_option()
        else:
            print("Something went wrong. Please try again")

    # Thai dessert inputs
def dessert3():
    # while True:
        print("")
        print("Would you like to add DESSERTS?")
        print("[+$10] Banana Roti")

        chi_des = input("Please press y/n: ")
        if chi_des.lower() == 'y':
            user.deposit(10)
            plans.append("Banana Roti")
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
# Display alcohol information        
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
            plans.append("BEER, WINE, SAKE")
            allergy()
        elif chi_des.lower() == 'n':
            allergy()
        else:
            print("Something went wrong. Please try again")
    # fill allergy
    # Input form

# Display the user's allergy  
def  allergy():
    
    print("")
    print("Please fill out your food allergies if you have")
    user_allergy = input("Do you have any food allergies?: ")
    print("")
    print(f"Your food allergy: {user_allergy}")
    confirm()



# Confirm what is your plan finally
# plan, main dish, desserts, alcohol and allergy
# Need to be with plan and total
def confirm():
    print("")
    print("Please comfirm your plan")

    # print(total_price)
    user.get_balance()
    print(plans)
    end()

# try again or exit
def end():
        print("Would you like to try again?")
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
    
# main
def main():

    budget()
    plan()

main()