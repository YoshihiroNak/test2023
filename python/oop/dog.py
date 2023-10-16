# my_dog = {'name': 'Ted', 'age': 15, 'breed': 'Border Collie'}

# def create(name, age, breed):
#     new_dog = {
#         'name' : name,
#         'age' : age,
#         'breed' : breed
#     }
#     return new_dog

# def walk(dog):
#     dog['walk'] += 1

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age



    def greet(self, prefix):
        # print(spam)
        print(f'{prefix} {self.name}!')


