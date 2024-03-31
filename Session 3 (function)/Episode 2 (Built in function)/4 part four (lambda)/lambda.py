# Example 1: Basic Lambda Function
add = lambda x, y: x + y
print("Sum of 3 and 5:", add(3, 5))  # Output: 8

# Example 2: Sorting a List of Tuples by Second Element
data = [(1, 'apple'), (3, 'banana'), (2, 'orange')]
data_sorted = sorted(data, key=lambda x: x[1])
print("Sorted Data:", data_sorted)  # Output: [(1, 'apple'), (3, 'banana'), (2, 'orange')]

# Example 3: Filtering Even Numbers from a List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)  # Output: [2, 4, 6, 8, 10]

# Example 4: Mapping Square Function to a List
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared Numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]
