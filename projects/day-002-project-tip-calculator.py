print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
peoples = int(input("How many people to split the bill? "))
total_per_person = total_bill * (1 + tip / 100) / peoples
print(f"Each person should pay: ${total_per_person:.2f}")
