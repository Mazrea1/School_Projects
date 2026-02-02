addItem = True
total = 0
while addItem == True:  
    item = float(input("Enter the cost of the item to your shopping list: "))
    if item == 0:
        print(f"Your total is ${total}. Goodbye!")
        break
    else:
        total += item
        print(f"${item} has been added to your shopping list.")