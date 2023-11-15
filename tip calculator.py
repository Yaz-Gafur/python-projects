print("Welcome to tip calculator!")
total_bill = input("Waht was the total bill?")
tip = input("What percentage tip would you like to to give? 10, 12, or 15?")
number_of_people = input("How many people to split the bill?")

total_bill_with_tip = float(total_bill) + (float(total_bill) / 100) * float(tip)
total_bill_with_tip_per_person = float(total_bill_with_tip)  / int(number_of_people)

print(f"Each person should pay ${total_bill_with_tip_per_person:.2f}")
