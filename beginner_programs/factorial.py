# Question: Calculate the factorial of a positive integer entered by the user.

n = int(input("Enter a positive integer: "))
result = 1
for i in range(1, n + 1):
    result *= i
print("Factorial of", n, "is", result)

# Explanation:
# We read a number from the user and convert it to an integer.
# result starts at 1 because multiplying by 1 does not change the value.
# The for loop multiplies result by each number from 1 up to n.
# When the loop ends, result contains the factorial of n, which we then print.
