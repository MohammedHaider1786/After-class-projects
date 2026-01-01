filename = "students.txt"

file = open(filename, "w")
file.write("Ali\n")
file.write("Sara\n")
file.write("Ahmed\n")
file.close()

print("File written successfully using 'w' mode.\n")

file = open(filename, "r")
content = file.read()
file.close()

print("File content using 'r' mode:")
print(content)

file = open(filename, "a")
file.write("Hussain\n")
file.close()

print("\nNew data appended using 'a' mode.\n")

file = open(filename, "r+")
print("Current file content using 'r+' mode:")
print(file.read())

file.write("Abbas\n")
file.close()

print("\nData written using 'r+' mode.")
