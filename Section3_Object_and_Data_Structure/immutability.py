name = 'Sam'

# Example 1
# TypeError: 'str' object does not support item assignment
# sentense[0] = 'p'
# print(sentense)

# Example 2
last_letters = name[1:]
print('p'+ last_letters)

# Example 3
test = 'Hello World'
print(test+' is a common greeting')

# Example 4
letter = 'x'
print('\n' + letter*10)

# Example 5
print('\n' + '2'+'3')
print('\n' + str(2+3))

# Example 6
example6 = 'Hello World'
print('\n'+example6.upper())
print('\n'+example6.lower())
print('\n')

print(example6.split())
print(list(example6))
