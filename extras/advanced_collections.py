from collections import Counter
from collections import namedtuple
from collections import defaultdict

# Counter is a class which can be used to count unique values in an object
list_of_nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3]

count_nums = Counter(list_of_nums)

print(count_nums)

print(list(count_nums))

print(Counter('Chinmay'))

# named tuples can be used to access the tuple values using their names
normal_tuple = ('a', 'b', 'c')
print(normal_tuple)
print(normal_tuple[1])

named_tuple = namedtuple('Dog', ['name', 'breed'])
print(type(named_tuple))

sammy = named_tuple('Sammy', 'Lab')
print(sammy.breed)
print(sammy[0])
print(sammy)

# default dictionary returns default value when non existent key is passed
my_dict = defaultdict(lambda : 0)
my_dict['One'] = 1
my_dict['Two'] = 2
print(my_dict.items())
print(my_dict['Wrong'])
