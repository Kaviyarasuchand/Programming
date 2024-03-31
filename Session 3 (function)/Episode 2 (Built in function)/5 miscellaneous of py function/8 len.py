#7. len()
#Basic Usage: Returns the length of an object.
string = "Hello, world!"
print("Length of string:", len(string))

#Advanced Usage: Counting the number of elements in a nested list.
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
total_elements = sum(len(sublist) for sublist in nested_list)
print("Total elements:", total_elements)