def say_hello():
    print('Hello')
    print('The best revenge is massive success')

say_hello()

def say_hello(name):
    print(f'Hello {name}')

say_hello('Jose')


def say_hello(name = 'default'):
    print(f'Hello {name}')

say_hello()


def add_num(num1,num2):
    return num1+num2

result = add_num(10,20)
print(result)


def add_num(num1,num2):
    return num1+num2


print(add_num('10', '300'))
