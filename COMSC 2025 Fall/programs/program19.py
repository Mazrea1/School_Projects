salePrices = []
quantity = []
totals = []
total = 0
for i in range(0,5,1):
    salePrices.append(float(input("Sale price: ")))
    quantity.append(int(input("Quantity: ")))
for i in range(0,5,1):
    totals.append(salePrices[i] * quantity[i])
for i in range(0,5,1):
    total += totals[i]
print(f"Your grand total is: ${total}")