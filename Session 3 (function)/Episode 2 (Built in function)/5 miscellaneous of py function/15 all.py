#19. all()
#Basic Usage: Returns True if all elements of an iterable are true.
values = [True, True, False, True]
print("All values are true:", all(values))

#Advanced Usage: Checking if all numbers in a list are even.
numbers = [2, 4, 6, 8, 9]
print("All numbers are even:", all(x % 2 == 0 for x in numbers))
