myname = 'Chinmay'
myProfession = "i am a data engineer at Fractal"

print("My name is " + myname,myProfession) # string concatenation

myname = "Vivek Bendigeri" # reassigning whole string is possible but not certain characters of the string

# slicing [start:end:steps] steps -> character jumps
print(myname[::]) # this is similar to printing the variable like myname
print(myname[:4]) # print from start to 4th character in a string
print(myProfession[2::2])

print(myname[::-1]) # this will reverse a string

#print(5 + ';;')  contactenation doesnt work for two different datatypes

#string functions
print(len(myname))

print(myname.upper())
print(myProfession.lower())

print(myname.split("i")) # this returns a list
print(myProfession.split()) # by default it will split based on space character and return a list

# string formatting
print(f'My name is {myname} and my job is that {myProfession}')
print("My name is {0} and my job is {1}".format(myname,myProfession)
      + "I earn {amt:1.2f} much money".format(amt=1500.6728))

