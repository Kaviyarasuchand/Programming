# Function with variable-length arguments
def sum_values(*args):
    total = 0
    for num in args:
        total += num
    return total

# Call the function with different number of arguments
print("Sum:", sum_values(1, 2, 3))  # Output: 6
print("Sum:", sum_values(1, 2, 3, 4, 5))  # Output: 15