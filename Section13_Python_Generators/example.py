# Normal function to create a list of cubes of numbers from 0 to n-1
def create_cubes(n):
    result = []
    for i in range(n):
        result.append(i ** 3)
    return result

for i in create_cubes(10):
    print(i)

# doesn't need to have whole list in memory
def generate_cubes(n):
    for i in range(n):
        yield i ** 3

for cube in generate_cubes(10):
    print(cube)