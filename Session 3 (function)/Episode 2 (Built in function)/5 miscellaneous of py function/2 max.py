#2. max()

#Basic Usage: Returns the maximum item from an iterable.
numbers = [3, 5, 1, 7, 9]
print("Maximum number:", max(numbers))

#Advanced Usage: Finding the longest word in a list of strings.
words = ["apple", "banana", "orange", "grape"]
longest_word = max(words, key=len)
print("Longest word:", longest_word)
