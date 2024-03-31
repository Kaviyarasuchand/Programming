# Printing a simple string
print("Hello, world!")

# Printing variables
name = "Alice"
age = 30
print("Name:", name)
print("Age:", age)

# Printing multiple items separated by a space (default behavior)
print("Name:", name, "Age:", age)

# Printing with formatted strings (f-strings)
print(f"Name: {name}, Age: {age}")

# Printing with format() method
print("Name: {}, Age: {}".format(name, age))

# Printing with different separators
print("Python", "is", "awesome", sep="-")
print("Python", "is", "awesome", sep="***")

# Printing with end parameter to change the end character
print("Hello,", end=" ")
print("world!")

# Printing without a newline character
print("This is on", end=" ")
print("the same line.")
