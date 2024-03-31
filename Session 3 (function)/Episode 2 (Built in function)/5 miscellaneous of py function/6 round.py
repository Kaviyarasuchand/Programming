#5. round()

#Basic Usage: Rounds a number to a specified number of decimal places.
num = 3.14159
print("Rounded value:", round(num, 2))

#Advanced Usage: Rounding numbers in a list to two decimal places.
nums = [3.14159, 2.71828, 1.61803]
rounded_nums = [round(x, 2) for x in nums]
print("Rounded numbers:", rounded_nums)
