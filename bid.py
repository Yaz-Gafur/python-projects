import art  # Importing the 'art' module, which likely contains the logo for the auction program
print(art.logo)  # Printing the auction logo from the 'art' module

# Function to find the highest bidder from the bidding dictionary
def find_highest_bidder(bidding_dic):
    winner = ""  # Initialize an empty string for the winner's name
    highest_bid = 0  # Initialize the highest bid amount as 0

    max(bidding_dic)  # This line does nothing and can be removed as it's not used in the logic

    # Loop through all bidders and their bids in the bidding dictionary
    for bidder in bidding_dic:
        bid_amount = bidding_dic[bidder]  # Get the bid amount for the current bidder
        # If the current bid is higher than the current highest bid, update highest bid and winner
        if bid_amount > highest_bid:
            highest_bid = bid_amount  # Update the highest bid amount
            winner = bidder  # Update the winner's name

    # Print the winner and their bid amount
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids = {}  # Initialize an empty dictionary to store bidder names and their corresponding bid amounts
continue_bidding = True  # Initialize a flag to control the bidding loop

# While loop to allow multiple bidders to place their bids
while continue_bidding:
    name = input("What is your name?:")  # Ask the bidder for their name
    price = int(input("What is your bid?: $"))  # Ask the bidder for their bid amount and convert it to an integer
    bids[name] = price  # Store the name and bid amount in the 'bids' dictionary

    # Ask if there are any other bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    
    # If no more bidders, stop the loop and find the highest bidder
    if should_continue == "no":
        continue_bidding = False  # Set flag to False to stop the bidding loop
        find_highest_bidder(bids)  # Call the function to find and print the highest bidder
    
    # If there are more bidders, clear the screen to hide previous bids (simulated by printing new lines)
    elif should_continue == "yes":
        print("\n" * 20)  # Print 20 new lines to simulate clearing the screen
