t = (1,2,3)

print(type(t))
print(len(t))

t = ('one',2)
print(t[0])

t = ('a','a','b')
print(t.count('a'))
print(t.index('a'))
print(t.index('b'))

l = [1,2,3]
t = (1,2,3)

l[0] = 'one'
print(l)

# Error
# t[0] = 'one'
# print(t)
