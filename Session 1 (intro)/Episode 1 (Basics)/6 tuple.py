#1. Creating a Tuple:
my_tuple = (1, 2, 3, 4, 5)

#2. Accessing Elements:
print(my_tuple[0])  # Output: 1

#3. Slicing Tuples:
sliced_tuple = my_tuple[1:3]  # Returns elements from index 1 to 2

#4. Length of Tuple:
length = len(my_tuple)

#5. Iterating Over a Tuple:
for item in my_tuple:
    print(item)

#6. Tuple Packing and Unpacking:
tuple_packing = 1, 2, 3
a, b, c = tuple_packing  # Tuple unpacking

#7. Checking if an Item Exists:
if 3 in my_tuple:
    print("3 exists in the tuple")

#8. Counting Occurrences:
count = my_tuple.count(3)  # Returns the number of occurrences of 3 in the tuple

#9. Finding Index:
index = my_tuple.index(3)  # Returns the index of the first occurrence of 3

#10. Converting Tuple to List:
tuple_to_list = list(my_tuple)

#11. Converting List to Tuple:
list_to_tuple = tuple([1, 2, 3, 4, 5])

#12. Concatenating Tuples:
concatenated_tuple = my_tuple + (6, 7, 8)

#13. Repeating Tuples:
repeated_tuple = my_tuple * 2

#14. Nested Tuples:
nested_tuple = ((1, 2), (3, 4), (5, 6))

#15. Tuple Membership Test:
if (1, 2) in nested_tuple:
    print("(1, 2) exists in the nested tuple")