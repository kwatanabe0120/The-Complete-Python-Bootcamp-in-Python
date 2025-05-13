def my_func(*arg):
    print(type(arg))
    print(sum(arg))

def my_func2(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print(f'My choice of fruite is {kwargs['fruit']}')
    

# my_func(10,20,30,490)
my_func2(fruit = 'Apple', test = 'test', hello = 23749823)