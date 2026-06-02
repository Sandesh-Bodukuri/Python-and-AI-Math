total_bill= float(input("Enter the total restaurant bill amount:"))
n = int(input("Enter number of persons splitting the bill:"))
tip =  float(input("Enter the tip percentage you want to give:"))

tip_amount = total_bill * (tip / 100)
grand_total = total_bill + tip_amount
amount_per_person = grand_total / n
print(f"The amount to be paid by each person : {amount_per_person:.2f}")

