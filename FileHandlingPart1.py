filename = "student_file.txt"

try:
    file = open(filename, 'r')

    print("\n--- Reading entire file using read() ---")
    file.seek(0)
    print(file.read())

    print("\n--- Reading file line by line using readline() ---")
    file.seek(0)
    while True:
        line = file.readline()
        if not line:
            break
        print(line, end='')

    print("\n\n--- Reading file using readlines() ---")
    file.seek(0)
    lines = file.readlines()
    for line in lines:
        print(line, end='')

    print("\n\n--- Reading file using for loop ---")
    file.seek(0)
    for line in file:
        print(line, end='')

    file.close()

except FileNotFoundError:
    print("File does not exist. Please create the file first.")
