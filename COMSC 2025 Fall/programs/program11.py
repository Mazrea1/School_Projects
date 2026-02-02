sale = int(input("Enter the total of the items: "))

if sale >= 100:
    discount = sale * 0.2
    total = sale - discount
elif sale >= 50:
    discount = sale * 0.1
    total = sale - discount
else:
    print("No discount, have a total equal to 50 or more to get a discount")
    exit()
print(f"The grand total is ${total}")