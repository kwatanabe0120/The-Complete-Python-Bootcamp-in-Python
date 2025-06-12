def add(num1, num2):
    print(num1+num2)

n1 = 10
n2 = input('Please enter number: ')

try:
    add(n1, n2)
except:
    print('The add function did not work correctly.')
else:
    # Since input retures str, this never happens
    print('You successfully used the add function.')