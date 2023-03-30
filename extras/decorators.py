# decorators in python are useful when you want to add extra functionalities to existing function
# without changing the old function

# internally decorators make use of passing old function as argument to new function and returning new function
# to a variable
def my_new_function(old_function):
    def extra_func():
        print("Code before the old function")

        old_function()

        print("code after the old function")

    return extra_func

def hello():
    print("Hi, Hello!")
    return "Executed hello() function!"


some_function = hello  # we are assigning function to a variable and executing from calling variable with ()

print(some_function())






def hello_func(name='chinmay'):
    print(f"Hello, {name}")


def my_function(some_func):  # my_function takes function as an argument
    some_func('Vivek')


my_function(hello_func)

# creating a decorator function


decorated_func = my_new_function(hello)

decorated_func()
