# Discount Calculator

A simple command-line tool written in Python to calculate the final price of an item after applying a discount.

## Description

This script provides an interactive menu that allows users to input an item's original price and a discount percentage. It then calculates and displays the final price. The script includes specific logic to only apply discounts that are 20% or higher.

## Features

-   Interactive command-line interface (CLI).
-   Calculates the final price after a specified discount.
-   Applies discounts only if the percentage is 20% or greater (up to 100%).
-   Handles non-numeric input gracefully.

## How to Use

### Prerequisites

-   Python 3.x

### Running the Script

1.  Save the code as `Discount_calculator.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using the following command:

    ```bash
    python Discount_calculator.py
    ```

5.  Follow the on-screen prompts:
    -   Choose option `1` to start a calculation.
    -   Enter the original price of the item.
    -   Enter the discount percentage.
    -   The final price will be displayed.
    -   Choose option `2` to quit the program.

## Example Interaction

```
Welcome to the Discount Calculator!

Please choose an option:
1. Calculate Discount
2. Quit
Enter your choice (1 or 2): 1
Enter the retail price of the item: 150
Enter the discount percentage of the item: 25
The final price after applying the discount is: 112.5
```