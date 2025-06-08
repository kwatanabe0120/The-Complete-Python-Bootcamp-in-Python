# Class sample
class Sample():
    pass

# Datetype is based on class
my_sample = Sample()
print(type(my_sample))

# Init is a constructor 
class Dog():
    species = 'mammal'

    def __init__(self, breed, name, age, spots):
        self.breed = breed
        self.name = name
        self.age = age
        self.spots = spots

    def bark(self, number):
        return f'WOOOF! My name is {self.name} and the number is {number}'    
    

my_dog = Dog(breed='Huskie', name="John", age=10, spots=False)
print(f"My Dog - Name: {my_dog.name}, Breed: {my_dog.breed}, Age: {my_dog.age}, Spots: {my_dog.spots}")


new_dog = Dog(breed='Lab', name="Haru", age=12, spots=False)
print(f'\nNewDog is {new_dog.species} always')
print(new_dog.bark(number=30))