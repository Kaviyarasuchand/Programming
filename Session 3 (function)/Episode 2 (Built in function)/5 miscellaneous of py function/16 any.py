#20. any()
#Basic Usage: Returns True if any element of an iterable is true.
values = [False, False, True, False]
print("Any value is true:", any(values))

#Advanced Usage: Checking if any number in a list is divisible by 5.
numbers = [7, 12, 15, 20]
print("Any number is divisible by 5:", any(x % 5 == 0 for x in numbers))
