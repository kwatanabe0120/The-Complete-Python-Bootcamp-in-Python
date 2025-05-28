# LEGB rule,
# Will read in order of Local,
# Enclosing,fuction locals, Global and Built-in

# Global
name = "Global string"

def greet():
    # Enclosing
    name = 'Sammy'

    def greet_Sammy():
        # Local
        name = 'I am a local'
        print("Hey "+name)
    
    greet_Sammy()

greet()


# Scope example

x = 50

def func(x):
    print(f'x is {x}')

    x = 200
    print(f'I locally changed x to {x}')

func(x)

x = 50

# Usually return and assin the global variable to make it clear
def func():
    global x
    print(f'x is {x}')


    x = 'New value'
    print(f'I locally changed x to {x}')

func()
print(f'This is x value now {x}')