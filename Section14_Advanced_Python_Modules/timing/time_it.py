import timeit


def func_one(n):
	return [str(num) for num in range(n)]

def func_two(n):
	return list(map(str, range(n)))


stmt = '''
func_one(1000)
'''

setup = '''
from __main__ import func_one
'''

print(timeit.timeit(stmt,setup,number=100000))

stmt = '''
func_two(1000)
'''

setup = '''
from __main__ import func_two
'''
print(timeit.timeit(stmt,setup,number=100000))