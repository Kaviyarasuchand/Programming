# Function with default arguments
def greet_user(name, message="Welcome to Python"):
    print(f"Hello, {name}! {message}")

# Call the function with only one argument
greet_user("Yogi")  # Output: Hello, Bob! Welcome to Python

# Call the function with both arguments
greet_user("Jai", "Goodbye!")  # Output: Hello, Alice! Goodbye!
