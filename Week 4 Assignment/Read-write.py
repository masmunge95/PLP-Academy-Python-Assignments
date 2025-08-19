# Function to create the original assignment file
def create_file():
    with open("Assignment.txt", "w") as file:
        file.write("Hello, PLP! This is my Week 4 Assignment")

# Function to read one file and write a modified version to another
def read_write_file(file_name):
    if file_name.lower() != "assignment.txt":
        print("Invalid file name. Please use 'Assignment.txt'.")
        return 
    try:
        # Read the file contents
        with open(file_name, "r") as file:
            content = file.read()
            print("\nOriginal content: ")
            print(content)
        # Write modified version to new file
        with open("Modified-Assignment.txt", "w") as file:
            new_content = content.replace("Hello", "Hi")
            file.write(new_content)
            print("\nModified content: ")
            print(new_content)
    except FileNotFoundError:
        print(f"{file_name} not found. Please try again.")
    finally:
        print("\nFile operation completed.\n")

# Main menu for the python file
def main():
    create_file()  # Create the initial file

    while True:
        print("Welcome to the Read-Write File Program!")
        print("1. Enter file name:")
        print("2. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_name = input("Enter the file name (including extension, e.g. Assignment.txt): ")
            read_write_file(file_name)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()