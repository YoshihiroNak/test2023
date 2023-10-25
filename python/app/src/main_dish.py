

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

dish(**dish1)
dish(**dish2)
dish(**dish3)
