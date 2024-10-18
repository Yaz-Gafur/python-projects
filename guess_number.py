from random import randint  # Import the 'randint' function to generate random integers.

EASY_LEVEL_TURNS = 10  # Set the number of attempts for 'easy' difficulty.
HARD_LEVEL_TURNS = 5  # Set the number of attempts for 'hard' difficulty.

# Function to check if the user's guess is too high, too low, or correct.
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:  # If the guess is greater than the actual answer.
        print("Too high.")  # Notify the user the guess is too high.
        return turns - 1  # Decrease the number of attempts and return.
    elif user_guess < actual_answer:  # If the guess is less than the actual answer.
        print("Too low.")  # Notify the user the guess is too low.
        return turns - 1  # Decrease the number of attempts and return.
    else:  # If the guess is equal to the actual answer.
        print(f"You got it. The answer was {actual_answer}")  # Notify the user of the correct guess.

# Function to set the difficulty level based on user input.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")  # Ask the user to choose difficulty.
    if level == "easy":  # If the user chooses 'easy' difficulty.
        return EASY_LEVEL_TURNS  # Return the number of turns for 'easy' difficulty.
    else:  # If the user chooses 'hard' difficulty or any other input.
        return HARD_LEVEL_TURNS  # Return the number of turns for 'hard' difficulty.

# Main game function.
def game():
    print("Welcome to the Number Guessing Game!")  # Welcome message to the user.
    print("I'm thinking of a number between 1 and 100.")  # Explain the game objective.
    answer = randint(1, 100)  # Generate a random number between 1 and 100 as the answer.
    print(f"Pssst, the correct answer is {answer}")  # (Optional) Print the answer for debugging or testing.

    turns = set_difficulty()  # Set the number of turns based on the chosen difficulty.

    guess = 0  # Initialize the user's guess to an arbitrary number (different from the answer).
    while guess != answer:  # Keep looping until the guess is equal to the answer.
        print(f"You have {turns} attempts to guess the number")  # Inform the user of the remaining attempts.
        guess = int(input("Make a guess: "))  # Ask the user for their guess and convert it to an integer.
        turns = check_answer(guess, answer, turns)  # Check the guess and update the remaining turns.
        if turns == 0:  # If the user runs out of turns.
            print("You've run out of guesses, you lose.")  # Inform the user that they've lost the game.
            return  # Exit the game.

# Start the game by calling the game() function.
game()
