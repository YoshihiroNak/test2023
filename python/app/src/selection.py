import plan, dish, main





plan1 = {
    "id" : 1,
    "menu": "Chinese Food",
    "price" : 100
}

plan2 = {
    "id" : 2,
    "menu": "Mexican Food",
    "price" : 150
}

plan3 = {
    "id" : 3,
    "menu": "Thai Food",
    "price" : 200
}

def plan(id, menu, price):
    print(f"Press {id}")
    print(menu)
    print(f"${price}")

dish1 = {
    "id" : 1,
    "menu": "Crispy Fried Chicken",
    "price" : 0
}

dish2 = {
    "id" : 2,
    "menu": "Roasted Pork Belly",
    "price" : 20
}

dish3 = {
    "id" : 3,
    "menu": "Angus Beef Steak",
    "price" : 40
}

def dish(id, menu, price):
    print(f"Press {id}")
    print(menu)
    print(f"${price}")

drink1 = {
    "id" : 1,
    "menu": "Nothing",
    "price" : 0
}

drink2 = {
    "id" : 2,
    "menu": "Beer",
    "price" : 20
}

drink3 = {
    "id" : 3,
    "menu": "Beer, Wine, Sake",
    "price" : 40
}

def drink(id, menu, price):
    print(f"Press {id}")
    print(menu)
    print(f"${price}")



def select(user_num):
    if user_num == "1":
        main.price.append(plan1["price"])
        return plan1["menu"]
    elif user_num == "2":
        main.price.append(plan2["price"])
        return plan2["menu"]
    elif user_num == "3":
        main.price.append(plan3["price"])
        return plan3["menu"]
    else:
        print("Somrthing went wrong. Please try again")


def choice(user_num):
    if user_num == "1":
        main.price.append(dish1["price"])
        return dish1["menu"]
    elif user_num == "2":
        main.price.append(dish2["price"])
        return dish2["menu"]
    elif user_num == "3":
        main.price.append(dish3["price"])
        return dish3["menu"]
    else:
        print("Somrthing went wrong. Please try again")

def drink(user_num):
    if user_num == "1":
        main.price.append(dirnk1["price"])
        return dirnk1["menu"]
    elif user_num == "2":
        main.price.append(drink2["price"])
        return drink2["menu"]
    elif user_num == "3":
        main.price.append(drink3["price"])
        return drink3["menu"]
    else:
        print("Somrthing went wrong. Please try again")