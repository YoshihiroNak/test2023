nums = [10, 14, 21, 50, 5, -6]

def square(value):
    return value ** 2

# def cube(value):
#     return value ** 3

# squared_nums = []
# for num in nums:
#     squared_nums.append(squared(num))

# squared_nums = list(map(lambda num: num ** 3, nums))

squared_nums = [num ** 2 for num in nums if num % 2 == 0]

# even_numbers = list(filter(lambda num: num % 2 == 0, nums))

print(squared_nums)