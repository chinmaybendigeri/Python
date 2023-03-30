import time
import timeit


# we can take the diff in time by measuring current time before and after running algorithm

def func1(n):
    return [str(x) for x in range(n)]


def func2(n):
    return list(map(str, range(n)))

start_time = time.time()
func1(100000)
end_time = time.time()

diff_time = end_time - start_time
print(diff_time)

start_time = time.time()
func2(100000)
end_time = time.time()

diff_time = end_time - start_time
print(diff_time)

# alternatively , timeit module can be used to determine the running time of an algorithm for large number of inputs



setup_one = '''
def func_one(n):
    return [str(x) for x in range(n)]
'''

stat_one = '''
func_one(1000)
'''

setup_two = '''
def func_two(n):
  return list(map(str, range(n)))
'''

stat_two = '''
func_two(1000)
'''


print(timeit.timeit(stat_one, setup_one, number=100000))
print(timeit.timeit(stat_two, setup_two, number=100000))
