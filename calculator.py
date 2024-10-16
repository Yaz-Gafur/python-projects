from itertools import accumulate  # Importing the 'accumulate' function from itertools (not used, can be removed)

# Defining basic arithmetic functions

def add(n1, n2):  # Function to add two numbers
    return n1 + n2

def subtract(n1, n2):  # Function to subtract the second number from the first
    return n1 - n2

def multiply(n1, n2):  # Function to multiply two numbers
    return n1 * n2

def devide(n1, n2):  # Function to divide the first number by the second
    return n1 / n2

# Dictionary to map arithmetic symbols to their corresponding function
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide,
}

# Main calculator function
def calculator():
    should_accumulate = True  # Flag to control whether to continue accumulating results

    # Prompt the user to input the first number and convert it to a float
    num1 = float(input("What is the first number?: "))

    # Loop to allow continuous calculations
    while should_accumulate:
        # Print the available operations
        for i in operations:
            print(i)

        # Ask the user to choose an operation
        choice = input("Choose an operation:")

        # Ask the user to input the second number and convert it to a float
        num2 = float(input("What is your second number?:"))

        # Perform the chosen operation by looking up the function in the operations dictionary and applying it
        answer = operations[choice](num1, num2)
        
        # Print the result of the calculation
        print(f"{num1} {choice} {num2} = {answer}")

        # Ask the user if they want to continue with the current result
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to stop the operation.")
        
        # If the user wants to continue, set the first number to the current result
        if should_continue == "y":
            num1 = answer  # Set num1 to the current answer for the next operation
        else:
            should_accumulate = False  # Set flag to False to stop the loop
            print("\n" * 20)  # Print new lines to simulate clearing the screen
            calculator()  # Restart the calculator function for a new calculation

# Start the calculator
calculator()

