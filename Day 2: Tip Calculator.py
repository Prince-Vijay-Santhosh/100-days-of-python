print("Tip Calculator\n")
bill_amount = float(input("Enter the total bill amount ₹:"))
tip_amount = int(
    input("Enter the percentage tip you would like to give (10, 12 or 15):"))
people_num = int(input("Enter the number of people to split the bill:"))
tip_per = tip_amount / 100
tot_tip_amo = bill_amount * tip_per
tot_bill = bill_amount + tot_tip_amo
tip = (bill_amount / people_num) * tip_per
bill_by_per = tot_bill / people_num
tip_final = round(bill_by_per, 2)
print(f"Each person should pay : {tip_final} ")
