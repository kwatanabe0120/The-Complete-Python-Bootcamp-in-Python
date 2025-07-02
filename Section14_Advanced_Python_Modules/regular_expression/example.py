import re

# basic search with 'in' keyword
text = "The agent's phone number is 408-555-1234. call soon!"
print('phone' in text)


# basic usecase of re module for seaching
patter = 'phone'
print(re.search(patter,text))
print(text[12:17])

patter = 'NOT IN TEXT'
print(re.search(patter,text))

print('='*50)

patter = 'phone'
match = re.search(patter,text)
print(match.span())
print(match.end())

print('='*50)
text = 'My phone once, my phone twice'
match = re.search('phone',text)
# only show the first match in text
print(match)

# show all matches in text
matches = re.findall('phone',text)
print(matches)
print(len(matches))

print('='*50)

for match in re.finditer('phone', text):
	print(match.span())