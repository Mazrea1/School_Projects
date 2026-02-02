totalAmt = float(input("Enter the total amount: "))
state = input("Enter your state of residence: ")
if totalAmt >= 100 and state == 'TX':
    discount = totalAmt * 0.25
elif totalAmt >= 100 and state == "LA":
    discount = totalAmt * 0.2
else:
    discount = totalAmt * 0.1
print("Your grand total is: ", totalAmt - discount)