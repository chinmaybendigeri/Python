mylist = [1,2,3,4,5,6,7,8,9,10]

for n in mylist:
    if n % 2 ==0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

mydict = {'key1': 100 , 'key2': 200, 'key3': 300}

for x in mydict: # this will print all the keys
    if x == 'key2':
        print("i found key2")
    elif x == 'key1':
        print("i found key1")
    else:
        print("i dont know what key is this!")

mytuplelist = [(1,2),(4,6),(7,8),(3,9)]

for k,v in mytuplelist:
    print(k)
    print(v)

