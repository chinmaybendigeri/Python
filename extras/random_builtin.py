import random
import math

print(math.floor(4.34))
print(math.ceil(4.78))
print(round(4.12))
print(round(4.5))
print(round(6.5))
print(round(7.5))
print(round(9.5))
print(round(8.5))

print(math.pow(10, 2))

print(random.randint(0, 10))

mylist = list(range(0, 10))
print(mylist)

my_num = random.choice(mylist)
print(my_num)

print(random.choices(mylist, k=10)) # with repetition
print(random.sample(mylist, k=10))  # without repetition
