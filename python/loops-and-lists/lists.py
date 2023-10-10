spam =["cat", "dog", "bird"]
eggs = [12, 78, 100, 54, 42]
foo = ["yoshi", 36, 185.0]
tic_tac_toe = [
    ['','o',''], 
    ['x','o', ''],
    ['','x', '']
]

# index = 1
# for animal in spam:
#     print(f"{index}. {animal}")
#     index += 1

    # index = 1
# for index, animal in enumerate(spam):
#     print(f"{index}. {animal}")
    # index += 1


    # # # print(spam)

# x = "dog" in spam
# print(x)

def display_person(person):
    # name = person[0]
    # age = person[1]
    # hieght = person[2]
    name, age, hieght = person
    print(f"{name} is {age} yeara old and {hieght}cm tall")

# display_person(foo)

spam.insert(1, "kangaroo")
x = spam.pop()
print(x)