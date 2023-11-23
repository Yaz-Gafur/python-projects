rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if your_choice == 0:
  print(rock)
elif your_choice == 1:
  print(paper)
elif your_choice == 2:
  print(scissors)
else:
  print("Invalid choice")

print("Computer chose:")

computer_choice = random.randint(0,2)
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)
else:
  print("Invalid choice")

if your_choice == 0 and computer_choice == 2:
  print("You win!")
elif your_choice == 0 and computer_choice == 1:
  print("You losse!")
elif your_choice == 0 and computer_choice == 0:
  print("Draw!")
elif your_choice == 1 and computer_choice == 0:
  print("You win!")
elif your_choice == 1 and computer_choice == 1:
  print("Draw!")
elif your_choice == 1 and computer_choice == 2:
  print("You losse!")
elif your_choice == 2 and computer_choice == 0:
  print("You losse!")
elif your_choice == 2 and computer_choice == 1:
  print("You win!") 
else:
  print("Draw!")


