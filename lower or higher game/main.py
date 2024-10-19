import random       # Import the random module to help pick random items from a list
from data import info    
from art import logo, vs    # Assuming game_data contains the dataset with follower information

# Function to pick a random person from the dataset
def get_random_comparison():
    
    return random.choice(info)         # Randomly choose one item (a dictionary) from the list of data

# Main function to start and manage the game

print(logo)
def game():
    score = 0           # Initialize the score to 0 at the start of the game
    continue_playing = True         # Flag to control whether the game should keep running or stop

    while continue_playing:         # Game loop that runs as long as the player keeps guessing correctly
        random_dic1 = get_random_comparison()       # Get the first random person (A)
        random_dic2 = get_random_comparison()       # Get the second random person (B)

        # Ensure that we don’t compare the same person to themselves
        while random_dic1 == random_dic2:
            random_dic2 = get_random_comparison()       # Keep picking random B until it's different from A

        # Display the details of the two random people for comparison
        print(f"Compare A: {random_dic1['name']}, a {random_dic1['description']}, from {random_dic1['country']}.")
        print(vs)
        print(f"Compare B: {random_dic2['name']}, a {random_dic2['description']}, from {random_dic2['country']}.")

        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()          # Ask the user to guess who has more followers by typing 'A' or 'B'
        print("\n" * 20)
        print(logo)

        # Compare the user's guess with the actual follower counts
        if (guess == "a" and random_dic1["follower_count"] > random_dic2["follower_count"]) or \
           (guess == "b" and random_dic2["follower_count"] > random_dic1["follower_count"]):
            
            score += 1                      # If the user's guess is correct, increase the score and inform them
            print(f"You're right! Current score: {score}")
            
        else:
            
            print(f"You lose! Final score: {score}")            # If the user's guess is wrong, end the game and show the final score
            continue_playing = False            # Set flag to False, ending the loop and game

# Call the game function to start the game when the script is run
game()
