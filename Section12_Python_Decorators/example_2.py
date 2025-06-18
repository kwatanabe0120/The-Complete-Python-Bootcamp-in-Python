def hello():
    print('The hello() function has been executed!')
# func in func so the scope is limited to the parent func
    def greet():
        return '\t This is the greet() func inside hello!'
    
    def welcome():
        return '\t This is the welcome() func inside hello!'

    print(greet())
    print(welcome())    
    print('This is the end of the hello function!')



hello()

# out of scope
# greet()