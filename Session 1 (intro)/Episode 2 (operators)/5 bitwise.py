# Bitwise Operators
x = 5  # 101
y = 3  # 011

# Bitwise AND
print("Bitwise AND (x & y):", x & y)  # Output: 1 (001)

# Bitwise OR
print("Bitwise OR (x | y):", x | y)  # Output: 7 (111)

# Bitwise XOR
print("Bitwise XOR (x ^ y):", x ^ y)  # Output: 6 (110)

# Bitwise NOT
print("Bitwise NOT (~x):", ~x)  # Output: -6

# Bitwise Left Shift
print("Bitwise Left Shift (x << 2):", x << 2)  # Output: 20 (10100)

# Bitwise Right Shift
print("Bitwise Right Shift (y >> 1):", y >> 1)  # Output: 1 (001)

# Bitwise NOT (on y to make it a negative number for demonstration)
y = -3  # -3 represented in two's complement: 11111111111111111111111111111101
print("Bitwise NOT (~y):", ~y)  # Output: 2 (00000000000000000000000000000010)
