def my_name(num):
    def inner_function(spam):
        if num == 42:
            spam('Life, the universe anad everythin')
        else:
            spam()

    return inner_function


@my_name(42)
def greet(name):
    print(f'Hello, {name}')

greet()

