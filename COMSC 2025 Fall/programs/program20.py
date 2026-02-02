mySales = open("mysales.txt", "w")
flag = "y"
while flag == "y":
    saleprice = float(input("Enter Sales Price of this Item: "))
    mySales.write(str(saleprice) +'\n')
    flag = input("continue (y/n)? ")
mySales.close()
print("Thanks, All are written in file called mysales.txt ")