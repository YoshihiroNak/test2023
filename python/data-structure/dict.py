my_dog = {'name': 'Ted', 'age': 15, 'breed': 'Border Collie'}

my_dog['age'] = 16

print(my_dog)

# dogs = [
#     {'name': 'Ted', 'age': 15, 'breed': 'Border Collie'},
#     {'name': 'Loki', 'age': 3, 'breed': 'Border Collie'}
# ]
my_dog['owner'] = 'Matt'

# for k, v in my_dog.items():
#     print(f'The value of "{k}" is {v}')

print(my_dog.get('state', 'Unknown'))