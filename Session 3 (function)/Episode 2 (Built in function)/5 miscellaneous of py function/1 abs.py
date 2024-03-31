#1. abs()

#Basic Usage: Returns the absolute value of a number.

num = -10
print("Absolute value:", abs(num))

#Advanced Usage: Using list comprehension to get absolute values of all numbers in a list.
numbers = [-3, -2, -1, 0, 1, 2, 3]
abs_values = [abs(x) for x in numbers]
print("Absolute values:", abs_values)