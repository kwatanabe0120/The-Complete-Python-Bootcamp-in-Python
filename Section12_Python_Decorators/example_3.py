def hello(name = 'Jose'):
    print('The hello() function has been executed!')
# func in func so the scope is limited to the parent func
    def greet():
        return '\t This is the greet() func inside hello!'
    
    def welcome():
        return '\t This is the welcome() func inside hello!'

    print('I am going to return a function!!')
    if name == 'Jose':
        return greet
    else:
        return welcome


my_new_func = hello()
print('\n\n\n')
print(my_new_func())

# function has definition of function inside, and return the function
def cool():
    def super_cool():
        return 'I am very cool!'
    return super_cool

some_func = cool()

print(some_func())
