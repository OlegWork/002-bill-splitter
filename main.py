print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip_percent = input("How much tip would you like to give? 10, 12 or 15? ")
people_to_split = input("How many people to split the bill? ")


total_bill = float(total_bill)
tip_percent = int(tip_percent)
people_to_split = int(people_to_split)

each_share = (total_bill + (total_bill* (tip_percent/100)))/people_to_split


print(f"Each peson should pay: ${each_share:.2f}")