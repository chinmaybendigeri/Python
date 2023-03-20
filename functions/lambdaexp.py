# map
# filter
mylist = [1,2,3,4,5]


def square(number):
    return number ** 2


print(list(map(square,mylist)))

print(list(map(lambda x: x ** 2, mylist)))

def is_even(number):
    return number % 2 == 0

print(list(filter(is_even, mylist)))

print(list(filter(lambda x: x % 2 == 0, mylist)))
