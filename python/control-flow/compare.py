x = int(input('What is x?'))
y = int(input('What is y?'))

if  x < y:
    print('x is less than y')
elif  x > y:
    print('x is greater than y')
else:
    print('x is equal to y')
    
print('Done')

score = int(input('score: '))

if score  >= 90:
    print('HD')
# elif 90 > score >= 80:
elif score >= 80:
    print('D')
elif score >= 70:
    print('CR')
elif score >= 50:
    print('P')
else:
    print('F')

name = input('What is your name?')

match name:
    case 'Harry' | 'Ron' | 'Herminone':
        print('Gryffindorn')
    case 'Draco':
        print('Slytherrin')
    case _:
        print('Mudblood')

shape = input('choose shape square or circle or triangle')

# match shape:
#     case 'square':
#     square_surface_area = x * y
#     x = float(input('Width of squre'))
#     y = float(input('Height of squre'))
#         print(f'Surface area is {square_surface_area} ㎡')

# r = float(input('Radius?'))

# circle_surface_area = r * r * 3.14

# print(f'Circle surface area is {circle_surface_area}')

# b = float(input('Width of triangle'))
# h = float(input('Height of triangle'))

# triangle_surface_area = b * h /2

