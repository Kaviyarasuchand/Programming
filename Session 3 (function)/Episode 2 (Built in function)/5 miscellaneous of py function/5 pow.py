#4. pow()
base = 2
exponent = 3
print("2^3 is", pow(base, exponent))

#Advanced Usage: Calculating powers of numbers in parallel lists.
nums = [2, 3, 4]
exponents = [2, 3, 4]
powers = [pow(x, y) for x, y in zip(nums, exponents)]
print("Powers:", powers)
