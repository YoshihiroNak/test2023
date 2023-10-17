import rpg 

aragorn = rpg.Ranger('Aragorn', 'Human', 100, 50)
galadriel = rpg.Mage('Galadriel', 'Elf', 120, 75)
frodo = rpg.Burglar('Frodo', 'Hobbit', 50, 25)
saruman = rpg.Wizard('Saruman', 'Human', 80, 100)
frodo.inv.set_currency(10, 5, 0)
print(frodo.inv.get_currency())
print(frodo.inv.__dict__)

# insrance
chest = rpg.Chest(['Iongsword', 'iron helm'], 2, 25, 50)

saruman.battle(aragorn)

galadriel.battle(aragorn)

# print(chest.inv.__dict__)
# print(aragorn.__dict__)
print(galadriel.__dict__)
# print(frodo.__dict__)

# frodo Loots a chest
# chest.inv.transfer(frodo.inv)

# print(frodo.inv.__dict__)
# print(frodo.inv.get_currency())
# print(chest.inv.__dict__)