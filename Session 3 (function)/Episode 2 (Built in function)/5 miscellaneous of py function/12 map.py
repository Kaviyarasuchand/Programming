#12. map()
#Basic Usage: Applies a function to all the items in an input iterable.
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

#Advanced Usage: Mapping multiple functions to corresponding elements in iterables.
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
added_nums = list(map(lambda x, y: x + y, nums1, nums2))
print("Added numbers:", added_nums)
