# Using the pass statement to do nothing and continue with the next iteration

# Example 1: Using pass in a while loop
count = 0
while count < 5:
    count += 1
    if count == 3:
        pass
    print(count)

# Example 2: Using pass in a for loop
for i in range(1, 6):
    if i == 3:
        pass
    else:
        print(i)
