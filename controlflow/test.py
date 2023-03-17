# go through the string and print each world starting with s
statement = 'python is super cool and simple easy to learn and code'
for s in statement.split(" "):
    if s.lower().startswith('s'):
        print(s)

# above problem using list comprehensions
[print(s) for s in statement.split(" ") if s.startswith('s')]

# print even numbers from 0 to 10
[print(num) for num in range(0,11) if num % 2 == 0]

# go through the string and if the length of a word is even print "even"
for s in statement.split(' '):
    if len(s) % 2 == 0:
        print("even")
    else:
        print(s)

# write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the
# number and for the multiples of 5 print "Buzz" and for numbers which are multiples of 3 & 5 print "FizzBuzz"

for number in range(0,101):
    if number % 3 ==0 and number % 5 ==0:
        print("FizzBuzz")
    elif number % 3 ==0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# create a list of the first letter of every word in a string -> use list comprehensions
newlist = [s[0] for s in statement.split(" ")]
print(newlist)

print(newlist.count('s'))