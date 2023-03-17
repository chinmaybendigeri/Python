from random import randint
from random import shuffle

mylist = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

print(mylist2[2])
# enumerate is used to get the  list item along with their index
for index,num in enumerate(mylist):
    print(index,num)

# zip will create a new list with tuple containing 1st element from list1 and list2 and so on
newlist = list(zip(mylist,mylist2))
print(newlist)

for i,num in zip(mylist,mylist2):
    print(i)
    print(num)

for i in list(range(10,20)):
    print(i)

x = randint(0,10)
print(x)

shuffle(mylist)
print(mylist)

# list comprehensions
mergedList = [x**2 for x in mylist for x in mylist if x % 2 == 0]
print(mergedList)