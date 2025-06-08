# Inheritance

class Animal():
    def __init__(self):
        print('Animal created!')
    def who_am_i(self):
        print('I am an animal')
    def eat(self):
        print('I am eating')

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print('Dog created!')
    
    # overwrite animal's method
    def eat(self):
        print('I am a dog and eating')

my_dog= Dog()
my_dog.eat()


