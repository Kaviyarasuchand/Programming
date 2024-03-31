# Using the continue statement to skip iteration and continue with the next iteration

# Example 1: Using continue in a while loop
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)

# Example 2: Using continue in a for loop
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
