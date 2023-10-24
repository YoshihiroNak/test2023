import funcs, dish
def menu():
    menu = {
        "1": {
            "name": "Chinese food",
            "options": {
                "1": "Chicken Fried Rice",
                "2": "Char Siu Pork",
                "3": "Mongolian Beef",
            }
        },
        "2": {
            "name": "Mexican food",
            "options": {
                "1": "Mexican Lime Chicken",
                "2": "Pork Carnitas",
                "3": "Barbacoa Beef",
            }
        },
        "3": {
            "name": "Thai food",
            "options": {
                "1": "Thai Fried Chicken",
                "2": "Thai Basil Pork Belly",
                "3": "Pad Gra Prow",
            }
        }
    }

    user_plan = input("Please press the number: ")
    if user_plan == "1":
        dish.chinese_food()
    elif user_plan == "2":
        dish.mexicon_food()
    elif user_plan == "3":
        dish.thai_food()

    if user_plan in menu:
        selected_menu = menu[user_plan]
        print(f"*** {selected_menu['name']} ***")
        
        user_dish = input("Please press the number for your main dish: ")
        
        
        if user_dish in selected_menu["options"]:
            selected_dish = selected_menu["options"][user_dish]
            print(f"You selected {selected_dish}")
            # Handle dessert and other choices here
        else:
            print("Invalid main dish selection")
    else:
        print("Invalid menu selection")

























    # if __name__ == "__main__":
    # funcs()