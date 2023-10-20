# display a main
# display shows up when the user clicks
def welcome():
    print("")
    print("*** Welcome to the catering services for your party! ***")
    print("")


# description
def description():
    pass
# Budget checking
def budjet():
    print("Please choose your budget for your party")
    print("")
    print("")
    print("$ 100 Chinese food, Press '1'")
    print("")
    print("$ 150 Mexican food, Press '2'")
    print("")
    print("$ 200  Thai  food,  Press '3'")
    print("")
# choose a plan
def plan():
    user_plan = input("Please press the number: ")

    if user_plan == '1':
        chinese_food()

    elif user_plan == '2':
        mexicon_food()

    elif user_plan == '3':
        thai_food()

# Chinese food function
def chinese_food():
    print("")
    print("***Chinese food***")
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
        optional()
# Mexico food function
def mexicon_food():
    print("***Mexican food***")
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
# Thai food function
def thai_food():
    print("***Thai food***")
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
# choose a main
def dish():

        pass
# choose optional
def optional():
    print("")
    print("Would you like to add DESSERTS?")
    user_opt = input("Please press y/n: ")
    if user_opt.lower() == 'y':
        dessert()
    elif user_opt.lower() == 'n':
        pass

# desserts
def dessert():
    print("dessert")
# alcoholic
def alcohol():
    pass
# fill allergy
def  allergy():
    pass
# conform display
def conform():
    pass
# try again or exit
def exit():
    pass

welcome()
budjet()
plan()