print("Welcome to the tip calculator!")
print()
#Main Program
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
#Converts tip to percentage
tip_as_percent = tip / 100
#Calculates tip
total_tip_amount = bill * tip_as_percent
#Calculates total bill with tip
total_bill = bill + total_tip_amount
#Calculates bill per person
bill_per_person = total_bill / people
#Rounds the final amount and prints it
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")