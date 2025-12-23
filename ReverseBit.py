# Input number
num = int(input("Enter a number: "))

# Convert number to binary (without 0b prefix)
binary = bin(num)[2:]

# Reverse the binary bits
reversed_binary = binary[::-1]

# Convert reversed binary back to decimal
new_number = int(reversed_binary, 2)

# Output results
print("Original binary:", binary)
print("Reversed binary:", reversed_binary)
print("New number after reversing bits:", new_number)
