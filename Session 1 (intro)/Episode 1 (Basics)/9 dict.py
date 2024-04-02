# Creating a dictionary
my_dict = {
    "name": "Prakash",
    "age": 30,
    "city": "New York"
}

# Accessing values using keys
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York

# Adding a new key-value pair
my_dict["gender"] = "Male"

# Modifying a value
my_dict["age"] = 32

# Removing a key-value pair
del my_dict["city"]

# Iterating over keys and values
for key, value in my_dict.items():
    print(key, ":", value)
