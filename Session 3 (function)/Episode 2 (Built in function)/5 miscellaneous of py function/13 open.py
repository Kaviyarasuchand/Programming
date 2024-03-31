#13. open()
#Basic Usage: Opens a file and returns a file object.
with open('example.txt', 'r') as file:
    contents = file.read()
    print("File contents:", contents)

#Advanced Usage: Writing data to a file.
data = "Hello, world!"
with open('output.txt', 'w') as file:
    file.write(data)
print("Data written to file.")