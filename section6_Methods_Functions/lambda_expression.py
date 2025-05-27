def square(num):
    return num **2

nums = [1,2,3,4,5]

for num in map(square, nums):
    print(num)


print(list(map(square, nums)))

def splicer(str):
    if len(str) % 2 == 0:
        return 'Even'
    else:
        return str[0]

names = ['John', 'Catherine', 'Alex', 'Emily', 'Chris']

for name in map(splicer, names):
    print(name)


# Filter function to apply a func as a condition
def check_even(num):
    return num % 2 ==0

l = [1,2,3,4,5,6]

print(list(filter(check_even, l)))


# lambda expresion example 1
square = lambda num: num**2

print(square(3))

print(list(map(lambda num:num**2, l)))

# lambda expresion example 2
names = ['Andy', 'John', 'Catherine', 'Alex', 'Emily', 'Chris', 'Sarah', 'Michael']

print(list(map(lambda name: name[::-1], names)))