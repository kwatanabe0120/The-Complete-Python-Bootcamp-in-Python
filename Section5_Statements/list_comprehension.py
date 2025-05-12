# string = 'Hello world'
# l = []
# for letter in string:
#     l.append(letter)

# print(l)


# string = 'Hello world'
# l = [letter for letter in string if letter != ' ']
# print(l)


# string = 'Hello world'
# l = [letter*2 for letter in string if letter != ' ']
# print(l)


# celcius = [0,10,20,34,54.5]
# fahrenheit = [((9/5*temp) + 32) for temp in celcius]
# print(fahrenheit)

list1 = [1,2,3,4]
list2 = [100,200,300,400]
result = []
for num in list1:
    for num2 in list2:
        result.append(num*num2)

print(result)