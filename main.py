print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
no_of_people = int(input("How many people to split the bill with? "))
tip_percentage = int(
    input("What percentage of bill would you like to give? 10, 12 or 15? "))
total_tip = total_bill * (tip_percentage / 100)
total_bill_with_tip = total_bill + total_tip
per_person_split = total_bill_with_tip / no_of_people
while (tip_percentage != 10 and tip_percentage != 12 and tip_percentage != 15):
  print("Please enter a valid percentage.")
  tip_percentage = int(
      input("What percentage of bill would you like to give? 10, 12 or 15? "))

print(f"Each person should pay ${round(per_person_split,2)}")
