# Question: Ask for a number and report whether it is even or odd.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# Explanation:
# The input function reads a value from the user as a string.
# int() converts that string to an integer so we can perform arithmetic.
# Using the modulo operator %, we check if the number is divisible by 2.
# If the remainder is 0, it's even; otherwise it's odd.
