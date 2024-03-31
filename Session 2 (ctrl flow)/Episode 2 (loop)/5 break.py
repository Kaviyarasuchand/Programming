# Using the break statement to exit a loop early

# Example 1: Using break in a while loop
count = 1
while True:
    print(count)
    count += 1
    if count > 5:
        break

# Example 2: Using break in a for loop
for i in range(1, 11):
    print(i)
    if i == 5:
        break
