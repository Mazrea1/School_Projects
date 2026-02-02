salary = int(input("Enter your salary: "))

def calculateBonus(salary):
    x = salary * 0.1
    return int(x)
def totalSalary(salary):
    total = salary + calculateBonus(salary)
    return total

print(f"Congrats ! You recieved a bonus of {calculateBonus(salary)} dollars.")
print(f"Your total salary for this year is {totalSalary(salary)} dollars.\nThank You !")