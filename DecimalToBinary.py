# Input binary number as a string
binary_number = input("Enter a binary number: ")

if not all(bit in '01' for bit in binary_number):
    print("Please enter binary values only (0 and 1).")
else:
    decimal_number = int(binary_number, 2)

    print("Decimal equivalent:", decimal_number)
