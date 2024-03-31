#9. zip()

#Basic Usage: Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print("Zipped pairs:", list(zipped))

#Advanced Usage: Unzipping a list of tuples into separate lists.
data = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*data)
print("Numbers:", numbers)
print("Letters:", letters)
