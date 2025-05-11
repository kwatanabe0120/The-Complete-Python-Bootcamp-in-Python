my_iterable = [1,2,3,4,5,6,7,8,9,10]

for num in my_iterable:
    print('Hello')


for num in my_iterable:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd num {num}')

sum = 0
for num in my_iterable:
    sum += num

print(sum)

sum = 0
for num in my_iterable:
    sum += num
    print(sum)


for letter in 'Hello World':
    print(letter)

for _ in 'Hello World':
    print('Variable is not used')

my_list = [(1,2),(3,4),(5,6),(7,9)]

for a,b in my_list:
    print(a*b)


d = {'k1':1, 'k2':2,'k3':3}

for num in d:
    print(num)

d = {'k1':1, 'k2':2,'k3':3}

for num in d.values():
    print(num)



d = {'k1':1, 'k2':2,'k3':3}

for num in d.items():
    print(num)