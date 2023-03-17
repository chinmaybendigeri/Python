# write a program that asks user to guess the correct cup  after the shuffle

# initial list
mylist = [' ', 'O', ' ']

# shuffle the list
from random import shuffle


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


# user guess
def user_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Guess the Index: 0,1 or 2 ")

    return int(guess)


# check the user guess
def check_user_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!!!")
    else:
        print("Wrong!!!")
        print(mylist)

my_mixed_list = shuffle_list(mylist)

guess = user_guess()

check_user_guess(my_mixed_list,guess)