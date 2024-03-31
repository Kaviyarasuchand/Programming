#3. min()

#Basic Usage: Returns the minimum item from an iterable.
numbers = [3, 5, 1, 7, 9]
print("Minimum number:", min(numbers))

#Advanced Usage: Finding the shortest word in a list of strings.
words = ["apple", "banana", "orange", "grape"]
shortest_word = min(words, key=len)
print("Shortest word:", shortest_word)
