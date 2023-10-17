# with open('shopping.txt') as f:
#     for line in f:
#         print(line.strip())
    # data = f.readlines()
    # print(repr(data))

# data2 = f.read(10)
# remenber until we get

# f.close()

# print(repr(data2))

# shopping_list = []
# with open('shopping.txt') as f:
#     data = f.read()
#     shopping_list = data.split('\n')
#     # for line in f:
#     # shopping_list.append(line.strip())

# print(shopping_list.strip)

# shows = [
#     'The Manalorian',
#     'The Wicher',
#     'The X-Files'
# ]

# with open('tv-show.txt','w' ) as f:
#     # f.write('\n'.join(show))
#     for s in shows:
#         f.write(f'{s}\n')

item = input('What do you need to buy?')
with open('shopping.txt', 'a') as f:
    # a means append
    f.write(f'\n{item}')
