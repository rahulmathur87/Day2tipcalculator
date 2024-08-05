print("Welcome to the tip calculator!")
total_bill = float(input("Total Bill? $"))
tip_percentage = int(input("Tip percentage? 10,12 or 15? "))
people = int(input("How many to split the bill? "))
bill_plus_tip = total_bill + ((tip_percentage/100) * total_bill)
share = bill_plus_tip/people
final_share = "{:.2f}".format(share)
print(f"Each person's share is ${final_share}")
