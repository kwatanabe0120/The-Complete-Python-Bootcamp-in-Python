# No.1
def gensquares(N):
    for num in range(N):
        yield num ** 2
        
for x in gensquares(10):
    print(x)
    
# No.2
import random

print('\n')
def rand_num(low,high,n):
    for num in range(n):
        yield random.randint(low, high)
        
for num in rand_num(1,10,12):
    print(num)
    
# No.2
print('\n')
s = 'hello'
s_iter = iter(s)
print(next(s_iter))


# No.3
print('\n')
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)
for item in gencomp:
    print(item)
    

# list comprehension

test = [num for num in [1,5,8,10] if num > 2]

print('\n')
for item in test:
    print(item)