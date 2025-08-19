# Week 4 Assignment: File and Exception Handling in Python

This project is a simple command-line Python script created for the PLP Academy's Week 4 assignment. It demonstrates fundamental concepts of file handling (I/O) and robust exception handling.

## Description

The script provides a menu-driven interface that performs the following operations:
1.  **Creates a file** named `Assignment.txt` with a predefined sentence.
2.  **Reads the content** from `Assignment.txt`.
3.  **Modifies the content** by replacing the word "Hello" with "Hi".
4.  **Writes the modified content** to a new file named `Modified-Assignment.txt`.

Throughout this process, the script uses `try...except` blocks to gracefully handle potential errors such as `FileNotFoundError`, `PermissionError`, and other `OSError` exceptions that might occur during file operations.

## Features

- **File Creation**: Automatically generates the initial `Assignment.txt` file.
- **File Reading**: Reads data from a specified text file.
- **Content Modification**: Performs a simple string replacement on the file's content.
- **File Writing**: Saves the modified content to a new destination file.
- **Interactive CLI**: A user-friendly command-line menu to operate the program.
- **Robust Error Handling**: Catches and reports common file-related errors without crashing.

## How to Run the Script

1.  Ensure you have Python installed on your system.
2.  Navigate to the project directory in your terminal or command prompt.
3.  Run the script using the following command:

    ```bash
    python Read-write.py
    ```

## Usage

Once the script is running, you will see a menu:

```
Welcome to the Read-Write File Program!
1. Enter file name:
2. Quit
Enter your choice:
```

1.  **To process the file**, enter `1`. The program will then ask for a filename.
    -   Enter `Assignment.txt`.
    -   The script will display the original content, the modified content, and confirm that the operation is complete.
    -   A new file, `Modified-Assignment.txt`, will be created in the same directory.
2.  **To exit the program**, enter `2`.

## Code Overview

- **`create_file()`**: Responsible for creating and writing the initial `Assignment.txt`.
- **`read_write_file(file_name)`**: The core function that handles reading the input file, modifying its content, and writing to the output file. It contains all the primary exception handling logic.
- **`main()`**: The main function that runs the program. It initializes the file, displays the menu, and handles user input in a continuous loop.
- **`if __name__ == "__main__":`**: The standard entry point that calls the `main()` function when the script is executed directly.