mydict = {'1' : 10,'2': 20, '3': 'Thirty'} # dictionaries are unordered key-value pairs

print(mydict['3'])
mydict['2'] = 'twenty'.upper()

print(mydict['2'])

print(mydict)

print(mydict.keys()) # returns the list of keys
print(mydict.values()) # returns the list of values

print(mydict.items()) #returns a list of key-value pair as tuples

print(len(mydict))