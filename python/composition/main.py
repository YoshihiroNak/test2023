import rpg 

aragorn = rpg.Character('Aragorn', 'Human')
galadriel = rpg.Character('Galadriel', 'Elf')
frodo = rpg.Character('Frodo', 'Hobbit')

frodo.inv.set_currency(10, 5, 0)
print(frodo.inv.get_currency())
print(frodo.inv.__dict__)

# insrance
chest = rpg.Chest(['Iongsword', 'iron helm'], 2, 25, 50)

print(chest.inv.__dict__)
# print(aragorn.__dict__)
# print(galadriel.__dict__)
# print(frodo.__dict__)

# frodo Loots a chest
chest.inv.transfer(frodo.inv)

print(frodo.inv.__dict__)
print(frodo.inv.get_currency())
print(chest.inv.__dict__)