x = 50
while x < 5:
    print(f'Current value = {x}')
    x += 1
else:
    print('The condition is evaluated as false')


x = [1,2,3]

for item in x:
    pass
    
print('end of my script')
# 
name = 'Sammy'

for letter in name:
    if letter == 'a':
        continue
    print(letter)



name = 'Sammy'

for letter in name:
    if letter == 'm':
        break
    print(letter)


