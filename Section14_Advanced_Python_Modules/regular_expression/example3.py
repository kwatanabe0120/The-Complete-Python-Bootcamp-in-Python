import re

# | to use or operator
print(re.search(r'dog|cat', 'The cat is here'))

# . is wildcard 
print(re.findall(r'.at', 'The cat in the hat sat there.'))
print(re.findall(r'...at', 'The cat in the hat sat splat.'))

# ^ is the start of sentence
print(re.findall(r'^\d', 'The 1 is a numebr'))

# $ is the end with
print(re.findall(r'\d$', 'The numebr is 100'))
print(re.findall(r'\d+$', 'The numebr is 100'))