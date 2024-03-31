#11. filter()
#Basic Usage: Constructs an iterator from elements of an iterable for which a function returns true.
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

#Advanced Usage: Filtering a dictionary based on a condition.
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_data = dict(filter(lambda item: item[1] > 2, data.items()))
print("Filtered data:", filtered_data)