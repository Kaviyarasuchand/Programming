#10. enumerate()
#Basic Usage: Returns an enumerate object that yields pairs of indexes and elements.
colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(index, color)

#Advanced Usage: Using enumerate to create a dictionary with index as keys.
colors = ['red', 'green', 'blue']
color_dict = {index: color for index, color in enumerate(colors)}
print("Color dictionary:", color_dict)