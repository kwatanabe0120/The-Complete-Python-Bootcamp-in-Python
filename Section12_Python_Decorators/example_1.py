# Function is just an object so we can pass it
def func():
    return 1

def hello():
    print('Hello')

print(hello)

greet = hello
print(greet)

# del keyword deletes the function's memory only if there is no variable pointing to the function
greet()