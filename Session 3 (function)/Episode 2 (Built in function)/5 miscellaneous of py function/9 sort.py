#8. sorted()
#Basic Usage: Returns a new sorted list from the elements of any iterable.
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)

#Advanced Usage: Sorting a list of tuples based on a specific element.
data = [('Alice', 25), ('Bob', 20), ('Charlie', 30)]
sorted_data = sorted(data, key=lambda x: x[1])
print("Sorted data:", sorted_data)
