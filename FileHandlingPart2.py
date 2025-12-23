filename = "student_file.txt"

while True:
    print("\n--- File Operations Menu ---")
    print("1. Write to file")
    print("2. Read file")
    print("3. Append to file")
    print("4. Count number of lines")
    print("5. Count number of words")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        data = input("Enter text to write to the file: ")
        with open(filename, 'w') as file:
            file.write(data)
        print("Data written successfully.")

    elif choice == '2':
        try:
            with open(filename, 'r') as file:
                print("\nFile contents:")
                print(file.read())
        except FileNotFoundError:
            print("File does not exist.")

    elif choice == '3':
        data = input("Enter text to append to the file: ")
        with open(filename, 'a') as file:
            file.write("\n" + data)
        print("Data appended successfully.")

    elif choice == '4':
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                print("Number of lines:", len(lines))
        except FileNotFoundError:
            print("File does not exist.")

    elif choice == '5':
        try:
            with open(filename, 'r') as file:
                words = file.read().split()
                print("Number of words:", len(words))
        except FileNotFoundError:
            print("File does not exist.")

    elif choice == '6':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please select from 1 to 6.")
