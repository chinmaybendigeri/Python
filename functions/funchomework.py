# write a function that computes the volume of a sphere given its radius
# 4/3 x pi x r ** 3
import math


def compute_volume(r):
    return (4 / 3) * math.pi * (r ** 3)


print(compute_volume(2))


# write a function that returns true if a number is in given range

def is_in_range(num, low, high):
    return True if num in range(low, high + 1) else False


print(is_in_range(5, 2, 7))


# write a function that calculates the number of upper and lower case letters in a string

def calculate_lower_upper(text):
    count_upper = 0
    count_lower = 0
    for c in text:
        if c.isupper():
            count_upper += 1
        else:
            count_lower += 1
    return count_lower, count_upper


print(calculate_lower_upper("ChinMay"))

# write a function that takes a list and returns a new list with unique elements of the old list

duplicate_list = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6, 6]

print(list(set(duplicate_list)))


def unique_list(mylist):
    i = 0
    j = 1
    unique_list = []
    unique_list.append(mylist[0])
    while j < len(mylist):
        if mylist[i] != mylist[j]:
            unique_list.append(mylist[j])
            i = j
        j += 1
    return unique_list


def alternate_unique_list(mylist):
    unique_list = []
    for x in mylist:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


print(unique_list(duplicate_list))

print(alternate_unique_list(duplicate_list))

# write a simple function to multiply all the numbers in a list

multi_list = [1, 2, 3, 4, 5]


def multiply_list_numbers(mylist):
    if len(mylist) == 0:
        return 0
    result = 1
    for x in mylist:
        result *= x
    return result


print(multiply_list_numbers(multi_list))
print(multiply_list_numbers([]))
