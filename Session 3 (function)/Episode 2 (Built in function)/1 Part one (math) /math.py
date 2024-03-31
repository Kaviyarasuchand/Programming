import math

# Basic Math Functions
print("Basic Math Functions:")
print("Square root of 16:", math.sqrt(16))
print("2 raised to the power of 3:", math.pow(2, 3))
print("Exponential value of 2:", math.exp(2))
print("Natural logarithm of 10:", math.log(10))
print("Ceiling of 3.14:", math.ceil(3.14))
print("Floor of 3.14:", math.floor(3.14))
print("Truncated value of 3.14:", math.trunc(3.14))
print("Factorial of 5:", math.factorial(5))

# Trigonometric Functions (Angles in radians)
print("\nTrigonometric Functions:")
angle_radians = math.radians(45)  # Convert degrees to radians
print("Sine of 45 degrees:", math.sin(angle_radians))
print("Cosine of 45 degrees:", math.cos(angle_radians))
print("Tangent of 45 degrees:", math.tan(angle_radians))
print("Arcsine of 0.7071:", math.degrees(math.asin(0.7071)))
print("Arccosine of 0.7071:", math.degrees(math.acos(0.7071)))
print("Arctangent of 1:", math.degrees(math.atan(1)))

# Constants
print("\nConstants:")
print("Value of pi:", math.pi)
print("Value of e (Euler's number):", math.e)
