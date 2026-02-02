totalAmt = float(input("Enter the total amount: "))
boughtComp = input("Did you buy a computer? ")
if totalAmt >= 100 or boughtComp.lower() == "yes":
    discount = totalAmt * 0.25
else:
    discount = totalAmt * 0.1
print("Your grand total is: ", totalAmt - discount)