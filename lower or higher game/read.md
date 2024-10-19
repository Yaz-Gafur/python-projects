"""
Number Guessing Game Documentation
----------------------------------

This Python program is a "Guess Who Has More Followers" game where the user is presented with two people from a dataset 
of social media influencers. The user must guess which person has more followers by typing 'A' or 'B'. If the guess is 
correct, the user scores a point and the game continues with two new people. If the guess is wrong, the game ends, 
and the final score is displayed.

Functions:
----------
1. get_random_comparison() -> dict:
   - Randomly selects a person from the dataset and returns their dictionary.
   - This function ensures we always get a new random person for comparison.

2. check_guess(guess: str, random_dic1: dict, random_dic2: dict) -> bool:
   - Compares the follower count of two random people (Person A and Person B) based on the user's guess.
   - Parameters:
     - `guess`: User's guess ('a' or 'b'), indicating which person they think has more followers.
     - `random_dic1`: Dictionary representing Person A.
     - `random_dic2`: Dictionary representing Person B.
   - Returns:
     - `True`: If the user guessed correctly (i.e., selected the person with more followers).
     - `False`: If the user guessed incorrectly or input an invalid value.

3. game():
   - Main function to run the game. It displays comparisons, takes the user's input, and keeps track of the score.
   - The game continues until the user makes an incorrect guess.
   - A loop inside the game selects random people and checks their follower count against the user's guess using 
     the `check_guess()` function.
   - At the end of the game, it displays the final score.
   - No parameters.
   - No return value.

How the Game Works:
-------------------
1. The game starts by randomly selecting two people (Person A and Person B) from a predefined dataset (game_data.data).
2. The user is shown details of both people (name, description, and country) and asked to guess which one has more 
   followers.
3. The user inputs 'A' or 'B' to make their guess.
4. If the user guesses correctly, the score is incremented by 1, and the game continues with a new pair of people.
5. If the user guesses incorrectly, the game ends, and the final score is displayed.

Dependencies:
-------------
- `random`: This module is used to randomly select a person from the dataset.
- `game_data`: The dataset (imported from an external file/module) containing information about various people, 
  including their name, description, country, and follower count. The dataset is expected to be a list of dictionaries.

Game Flow:
----------
1. The `game()` function is called to start the game.
2. Two random people are selected using `get_random_comparison()`.
3. The user is prompted to make a guess based on the follower count.
4. The `check_guess()` function verifies if the guess is correct or not.
5. If the guess is correct, the score increases, and the game continues. If incorrect, the game ends.

Example Output:
---------------
Welcome to the Number Guessing Game!
Compare A: Alice, a musician, from USA.
Compare B: Bob, an actor, from UK.
Who has more followers? Type 'A' or 'B': a
You're right! Current score: 1

Compare A: Alice, a musician, from USA.
Compare B: Charlie, an athlete, from Canada.
Who has more followers? Type 'A' or 'B': b
You lose! Final score: 1

"""

