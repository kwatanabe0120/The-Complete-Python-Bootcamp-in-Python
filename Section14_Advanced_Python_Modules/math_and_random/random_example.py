import random

random.seed(42)
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))

print('='*50)
my_list = list(range(0,21))
print(my_list)

print(random.choice(my_list))

print('='*50)

# sample with replacement
print(random.choices(population=my_list, k=10))

# sample without replacement
print(random.sample(population=my_list, k=10))



print('='*50)
random.shuffle(my_list)
print(my_list)


print('='*50)
print(random.uniform(a=0,b=100))