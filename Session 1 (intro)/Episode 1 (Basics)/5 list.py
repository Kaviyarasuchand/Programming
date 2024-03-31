#1. Creating a List:
my_list = [1, 2, 3, 4, 5]

#2. Accessing Elements:
print(my_list[0])  # Output: 1

#3. Appending Elements:
my_list.append(6)

#4. Inserting Elements:
my_list.insert(2, 10)  # Inserts 10 at index 2

#5. Removing Elements:
my_list.remove(3)  # Removes the first occurrence of 3

#6. Popping Elements:
popped_element = my_list.pop()  # Removes and returns the last element

#7. Slicing Lists:
sliced_list = my_list[1:3]  # Returns elements from index 1 to 2

#8. Length of List:
length = len(my_list)

#9. Iterating Over a List:
for item in my_list:
    print(item)

#10. List Comprehension:
squared_list = [x**2 for x in my_list]

#11. Sorting a List:
my_list.sort()  # Sorts the list in ascending order

#12. Reversing a List:
my_list.reverse()  # Reverses the elements in the list

#13. Copying a List:
new_list = my_list.copy()

#14. Clearing a List:
my_list.clear()  # Removes all elements from the list

#15. Checking if an Item Exists:
if 10 in my_list:
    print("10 exists in the list")