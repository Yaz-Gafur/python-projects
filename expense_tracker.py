# Function to add an expense to the list of expenses
def add_expense(expenses, amount, category):
    # Append a dictionary containing the expense amount and category to the expenses list
    expenses.append({'amount': amount, 'category': category})

# Function to print all the expenses in the list
def print_expenses(expenses):
    # Iterate through each expense in the expenses list
    for expense in expenses:
        # Print the amount and category of the current expense
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# Function to calculate the total amount of all expenses
def total_expenses(expenses):
    # Use map to extract amounts and sum them up
    return sum(map(lambda expense: expense['amount'], expenses))

# Function to filter expenses by a specific category
def filter_expenses_by_category(expenses, category):
    # Return an iterator of expenses where the category matches the specified category
    return filter(lambda expense: expense['category'] == category, expenses)

# Main function to drive the expense tracker program
def main():
    # Initialize an empty list to store expenses
    expenses = []
    
    # Infinite loop for the main menu until the user decides to exit
    while True:
        # Print the main menu for the expense tracker
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        # Get the user's choice for the operation to perform
        choice = input('Enter your choice: ')

        # Check if the user chose to add an expense
        if choice == '1':
            # Prompt the user to input the expense amount
            amount = float(input('Enter amount: '))
            # Prompt the user to input the expense category
            category = input('Enter category: ')
            # Add the expense to the list
            add_expense(expenses, amount, category)

        # Check if the user chose to list all expenses
        elif choice == '2':
            # Print a header for the list of all expenses
            print('\nAll Expenses:')
            # Call the function to print each expense
            print_expenses(expenses)
    
        # Check if the user chose to display the total expenses
        elif choice == '3':
            # Print the total expenses calculated by the function
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        # Check if the user chose to filter expenses by category
        elif choice == '4':
            # Prompt the user to enter the category to filter by
            category = input('Enter category to filter: ')
            # Print a header showing the filtered category
            print(f'\nExpenses for {category}:')
            # Get the filtered expenses
            expenses_from_category = filter_expenses_by_category(expenses, category)
            # Print the filtered expenses
            print_expenses(expenses_from_category)
    
        # Check if the user chose to exit the program
        elif choice == '5':
            # Print a message indicating the program is exiting
            print('Exiting the program.')
            # Break the loop to end the program
            break

# Call the main function to start the program
main()
