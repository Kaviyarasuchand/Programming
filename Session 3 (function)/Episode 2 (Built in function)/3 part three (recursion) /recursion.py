def factorial(n):
    """Recursive function to calculate factorial"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Testing the recursive function
number = 5
print("Factorial of", number, "is", factorial(number))
