print("Welcome to the tip calculator!")
total_bill = float(input("What is(was) your total bill? \n$"))
tip_in_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? \n%"))
number_people = int(input("How many people to split the bill?\n"))

tip_in_dollars = tip_in_percentage / 100 * total_bill
bill_with_tip = total_bill + tip_in_dollars
bill_per_person = bill_with_tip / number_people

print(f"Each person should pay: ${round(bill_per_person, 2):.2f}")