# Prompting the user for different types of input
name = input("Enter your name: ")  # string input
age = int(input("Enter your age: "))  # integer input
height = float(input("Enter your height (in meters): "))  # float input
is_student = input("Are you a student? (True/False): ").lower()  # boolean input

# Converting string input to boolean
is_student = is_student == 'true'

# Printing the input values along with their data types
print("Name:", name, type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("Is Student:", is_student, type(is_student))
