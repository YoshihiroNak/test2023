# spam =0
# while spam < 5:
#     print("Hello")
#     spam += 1

# print("Done")

# for spam in range(1, 11, 2):
#     print(f"Hello {spam}")

import random

count = int(input("How many rendom integers? "))
for i in range(count):
    print(random.randint(1, 100))