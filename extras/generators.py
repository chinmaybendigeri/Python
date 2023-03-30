# generators return one value at a time from a series of values
# it helps in better memory management as it doesn't save all the values in memory
import random


def cubes_without_generator(n):
    cube_list = []
    for num in range(n):  # range itself is a generator
        cube_list.append(num ** 3)

    return cube_list


for x in cubes_without_generator(10): print(x)
print(cubes_without_generator(10))


def cubes_gen(n):
    for num in range(n):
        yield num ** 3  # using yield is memory efficient


for x in cubes_gen(10):
    print(x)
print(cubes_gen(10))

cubes = cubes_gen(10)
print(next(cubes))  # print the first element in the generator
print(next(cubes))  # print the second element in the generator

name = 'Chinmay'
name_iter = iter(name)  # returns an iterable object on which we can use next function

print(next(name_iter))  # this will print C
print(next(name_iter))  # this will print h


# create a square generator till a number

def square_gen(n):
    for number in range(n):
        yield number ** 2


for x in square_gen(10):
    print(x)


# create generator which generators n numbers within a range (low,high)

def random_gen(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


for number in random_gen(0, 10, 12):
    print(number)
