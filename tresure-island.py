print("Welcome to Tresure Island.")
print("Your mission is to find the tresure.")
left_or_right = input("You are at a cross road. Where do you want to go? Type 'left' or 'right': ")
if left_or_right == "left":
    wait_or_swim = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait a boat. Type 'swim' to swim across.")
    if wait_or_swim == "wait":
        doors = input("You arrive at the island unharmed. There a house with 3 doors. one red, one yellow and one blue. Which color do you choose?")
        if doors == "yellow":
            print("You found the tresure!")
        else:
            print("Game over!")
    else:
        print("Game over!")
else:
    print("Game over!")
    
