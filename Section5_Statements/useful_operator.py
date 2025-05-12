# for num in range(10):
#     print(num)


# for num in range(3,10):
#     print(num)


# for num in range(10, -1, -1):
#     print(num)


# print(list(range(10, -1, -1)))

# word = 'Hello'
# count = 0

# for letter in word:
#     print(f'The value of index {count} is {letter}')
#     count += 1


# word = 'abcde'
# index = 0

# for _ in word:
#    print(word[index])
#    index +=1

# word = 'abcdefghi'

# for index,letter in enumerate(word):
#     print(f'Index:{index}\nLetter:{letter}\n')


# list1 = [1,2,3]
# list2 = ['a','b','c']
# list3 = [100,200,300,400]

# for item in zip(list1,list2,list3):
#     print(item)

# for a,b,c in zip(list1,list2,list3):
#     print(a,c)

# print(list(zip(list1,list2,list3)))

# print('x' in [1,2,3])

# print ('x' in 'Hello')

d = {'Key1':'test'}

print('Key1' in d)
print('test' in d.values())


mylist = [1,2,3,4,455,56]
print(min(mylist))
print(max(mylist))

from random import shuffle

shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,100))
print(randint(0,100))
print(randint(0,100))
print(randint(0,100))
print(randint(0,100))


result = input("Enter your age:")
print(f'You enter {result}')
result = int(result)
print(type(result))