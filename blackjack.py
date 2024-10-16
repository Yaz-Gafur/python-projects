import random  # Importing the random module to randomly deal cards
from art import logo  # Importing a 'logo' from an external 'art' module (likely for display, but unused in this code)

# Function to deal a random card from a list of possible card values
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # List of card values, 11 represents an Ace, and 10 is repeated for face cards (Jack, Queen, King)
    card = random.choice(cards)  # Randomly select a card from the list
    return card  # Return the selected card

# Function to calculate the score of a hand of cards
def calculate_score(cards):
    # Check if the hand is a Blackjack (Ace + 10) and return a score of 0 to represent it
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack represented as score 0

    # Handle the Ace (11) to convert it to 1 if the score exceeds 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)  # Remove the Ace (11)
        cards.append(1)  # Add the Ace as 1 instead
    return sum(cards)  # Return the total score of the hand

# Function to compare the user's score and the computer's score and determine the outcome
def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!"  # Both scores are equal, so it's a draw
    elif c_score == 0:
        return "Lose, opponent has Blackjack"  # Computer has a Blackjack
    elif u_score == 0:
        return "You win with a Blackjack"  # User has a Blackjack
    elif u_score > 21:
        return "You went over. You lose"  # User's score exceeds 21
    elif c_score > 21:
        return "Opponent went over. You win"  # Computer's score exceeds 21
    elif u_score > c_score:
        return "You win!"  # User's score is higher than the computer's
    else:
        return "You lose!"  # Computer's score is higher than the user's

# Main function to handle the gameplay
def play_game():
    user_cards = []  # Initialize an empty list for the user's cards
    computer_cards = []  # Initialize an empty list for the computer's cards
    computer_score = -1  # Initialize computer's score (will be updated later)
    user_score = -1  # Initialize user's score (will be updated later)
    is_game_over = False  # Flag to control the game loop

    # Deal two cards to both the user and the computer at the start
    for i in range(2):
        user_cards.append(deal_card())  # Add a card to the user's hand
        computer_cards.append(deal_card())  # Add a card to the computer's hand

    # Loop until the game is over
    while not is_game_over:
        user_score = calculate_score(user_cards)  # Calculate the user's current score
        computer_score = calculate_score(computer_cards)  # Calculate the computer's current score

        # Display the user's cards and current score, and the computer's first card
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for immediate game-ending conditions (Blackjack or user busts)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True  # End the game if Blackjack or bust
        else:
            # Ask the user if they want to draw another card or pass
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())  # Deal another card to the user
            else:
                is_game_over = True  # End the game if the user passes

    # The computer draws cards until its score is 17 or higher
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())  # Deal another card to the computer
        computer_score = calculate_score(computer_cards)  # Recalculate the computer's score

    # Display the final hands and scores
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    # Compare the final scores and print the result
    print(compare(user_score, computer_score))

# Game loop to repeatedly play Blackjack until the user decides to quit
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 20)  # Clear the screen by printing new lines
    play_game()  # Start a new game
