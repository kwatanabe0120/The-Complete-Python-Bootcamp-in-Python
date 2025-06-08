# Polymorphism

class Dog():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print(f'My name is {self.name}, WOOF!')

class Cat():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print(f'My name is {self.name}, MEOW!')

def pet_speak(pet):
    pet.speak()

my_dog = Dog('Pon')
my_cat = Cat('Hana')

for animal in [my_dog, my_cat]:
    animal.speak()
    
pet_speak(my_dog)

# -----------------------------------
class Animal1:
    def speak(self):
        raise NotImplementedError("Implement in Other class")

class Dog1(Animal1):
    def speak(self):
        print("Woof!")

my_dog = Dog1()
my_dog.speak()
