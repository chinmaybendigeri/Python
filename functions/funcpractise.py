# write a function that returns lesser of the two even numbers but if there is one or more odd numbers return the
# greater number

def get_lesser_of_two_even(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return a if a < b else b
    else:
        return a if a > b else b


print(get_lesser_of_two_even(2, 4))
print(get_lesser_of_two_even(2, 5))


# write a function that returns true if in a two word string each word starts with same character
def animal_crackers(two_words):
    mylist = two_words.lower().split(" ")
    return mylist[0][0] == mylist[1][0]


print(animal_crackers("Chinmay sxhinuu"))
print(animal_crackers("Chinmay Cchinuu"))


# write a function that returns true if sum of two numbers is 20 or if either of the number is 20

def is_num_twenty(a, b):
    return a == 20 or b == 20 or a + b == 20


print(is_num_twenty(20, 30))
print(is_num_twenty(30, 30))
print(is_num_twenty(12, 8))


# write a function that will capitize the first and fourth letter of a word

def cap_letters_in_word(word):
    caped_word = word[0].upper() + word[1:3] + word[3].upper() + word[4:]
    return caped_word


print(cap_letters_in_word("chinmay"))


# Given a sentence , return a sentence with the words reversed

def reverse_sentence(sentence):
    mylist = sentence.split(" ")
    mylist.reverse()
    reversed = " ".join(mylist)
    return reversed


print(reverse_sentence("I am home"))
print(reverse_sentence("We are ready"))


# Given a number return true if n is within 10 of either 100 or 200

def check_within_reach(number):
    return abs(100 - number) <= 10 or abs(200 - number) <= 10


print(check_within_reach(105))
print(check_within_reach(89))
print(check_within_reach(190))

# given a list of ints ,return True if the array contains a 3 next to a 3 somewhere
myintlist = [1, 3, 3]


def has_33(mylist):
    for pos, x in enumerate(mylist):
        if x == 3:
            if pos != len(mylist) - 1 and mylist[pos + 1] == 3:
                return True
    return False


print(has_33(myintlist))
print(has_33([1, 3, 4, 3, 5]))
print(has_33([1, 4, 5, 3]))


# given a string return a string where for every character in a string has 2 more characters

def has_more_charaters(text):
    newtext = ''
    for c in text:
        newtext = newtext + c * 3
    return newtext


print(has_more_charaters("chinmay"))


# Given 3 integers between 1 and 11,if their sum is less than or equal to 21,return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total by 10.
# Finally, if the sum even after the adjustment exceeds 21 return 'BUST'

def sum_exceeds_21(a, b, c):
    if a + b + c <= 21:
        return a + b + c
    elif a + b + c - 10 > 21 and 11 in [a, b, c]:
        return a + b + c - 10
    else:
        return 'BUST'


print(sum_exceeds_21(5, 6, 7))
print(sum_exceeds_21(9, 9, 9))
print(sum_exceeds_21(9, 9, 11))
print(sum_exceeds_21(11, 10, 11))


# return the sum of the numbers in the array except ignore sections of numbers with a 6 and extending
# to the next 9(every 6 will be followed by at least one 9). Return 0 for no numbers

def ignore6_followed_9_sections(mylist):
    total = 0
    i = 0
    if len(mylist) == 0:
        return total
    else:
        while i < len(mylist):
            if mylist[i] == 6:
                i += 1
                while i < len(mylist) and mylist[i] != 9:
                    i += 1
            else:
                total = total + mylist[i]
            i += 1
    return total


print(ignore6_followed_9_sections([4, 5, 6, 7, 8, 9]))


# write a function that takes in a list of integers and returns True if it contains 007 in order

def find_spy(mylist):
    spy = ''
    for x in mylist:
        if x in [0, 7]:
            spy = spy + str(x)
    return '007' in spy


print(find_spy([1, 2, 4, 0, 0, 7, 5, 0, 0, 7]))
print(find_spy([1, 7, 2, 0, 4, 5, 0, 7]))


# write a function that returns the number of prime numbers that exist up to and including a given number

def check_is_prime(number_list):
    count = 0
    for number in range(2, number_list + 1):
        if number in [2, 3]:
            count = count + 1
        else:
            is_prime = True
            divisor = round(number / 2)
            while divisor > 1:
                if number % divisor == 0:
                    is_prime = False
                    break
                else:
                    divisor -= 1
            if is_prime:
                count = count + 1
    return count


print(check_is_prime(10))  # 2,3,5,7
print(check_is_prime(100))  # 2,3,5,7,...
