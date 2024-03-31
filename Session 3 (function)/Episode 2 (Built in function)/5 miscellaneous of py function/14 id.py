#14. id()
#Basic Usage: Returns the identity of an object.
value = 42
print("Identity:", id(value))

#Advanced Usage: Checking the identity of objects before and after assignment.
value1 = 42
value2 = 42
print("Identity before assignment:", id(value1), id(value2))
value2 = 100
print("Identity after assignment:", id(value1), id(value2))
