userQuit = False
while userQuit == False:
    userNum = int(input("Input a number: "))
    if userNum % 5 == 0:
        print(f"The number is divisible by 5 and the answer is {userNum / 5}")
    else:
        print("This number is not divisible by 5")
    userChoice = input("Do you want to quit? (y/n): ")
    if userChoice == "y":
        userQuit = True
        print("Goodbye!")
    else:
        userQuit = False
