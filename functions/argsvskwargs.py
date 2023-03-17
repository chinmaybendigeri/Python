
# *args takes n number of arguments as tuple values from function call
# **kwargs takes n number of arguments as dictinoary from function call

def myfunc1(*args):
    print(args)
    for pos,item in enumerate(args):
        print(pos,item)
    if 100 in args:
        print("You have won {} rupees".format(args[0]))
    else:
        print("Better luck next time!")

myfunc1(20,100,50,3)

def myfunc2(**kwargs):
    print(kwargs)
    for item in kwargs.items():
        print(item)
    if kwargs['food'] == 'pizza':
        print("Yum Yum Yum!")
    else:
        print("No pizza, Still hungry!")


myfunc2(drinks='Coco-cola',food = 'pizza', rest='sleep')