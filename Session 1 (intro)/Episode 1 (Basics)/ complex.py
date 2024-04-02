z = 3 + 4j

# Real and imaginary parts
print(z.real)  # Output: 3.0
print(z.imag)  # Output: 4.0

# Conjugate
print(z.conjugate())  # Output: (3-4j)

# Absolute value
print(abs(z))  # Output: 5.0

# Phase angle (in radians)
import cmath
print(cmath.phase(z))  # Output: 0.9272952180016122

# Arithmetic operations
w = 1 + 2j
print(z + w)  # Output: (4+6j)
print(z - w)  # Output: (2+2j)
print(z * w)  # Output: (-5+10j)
print(z / w)  # Output: (2+0j)
