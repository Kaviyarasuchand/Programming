# Identity Operators

# Consider two variables 'x' and 'y' assigned with integer values.
x = 5
y = 5

# is Operator:
# The 'is' operator checks if two variables refer to the same object in memory.
# In this case, 'x' and 'y' both have the same value, but Python may optimize memory
# by storing the same integer value in the same memory location for performance reasons.
# Therefore, 'x is y' will print True, indicating that 'x' and 'y' refer to the same object.
print("is Operator:")
print("x is y:", x is y)

# is not Operator:
# The 'is not' operator checks if two variables do not refer to the same object in memory.
# Since 'x' and 'y' have the same value and Python may optimize memory by storing the
# same integer value in the same memory location, 'x is not y' will print False,
# indicating that 'x' and 'y' refer to the same object.
print("\nis not Operator:")
print("x is not y:", x is not y)
