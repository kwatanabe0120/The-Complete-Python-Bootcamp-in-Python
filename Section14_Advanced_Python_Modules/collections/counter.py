from collections import Counter


my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
my_list2 = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
my_string = 'aaaaabbbbbccccccvvvvv'
my_sentence = 'This is a sample sentence for counting letters'


print(Counter(my_list))
print(Counter(my_list2))
print(Counter(my_string))
print(Counter(my_sentence))
print(Counter(my_sentence.split()))


letters = 'aaaaaabbbbbbvcvvvvvv'
c = Counter(letters).most_common(3)
print(c)


from collections import defaultdict
print('-------------------------------------------')

d = defaultdict(lambda: 30)
d['correctKey'] = 100
print(d['correctKey'])
print(d['wrongKey'])
print(d)



from collections import namedtuple
print('-------------------------------------------')
Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(age=5,breed='Husky',name='Sam')
type(sammy)
print(sammy)
print(sammy.age)
print(sammy[0])