Position = input("Welcome, Please enter your position: ")
State = input("Please enter your state: ")

if Position == "Manager" and State in ("NY", "NJ", "PA"):
    print("Red Attire")
elif Position == "Manager" and State in ("TX", "LA", "AK"):
    print("Green Attire")
elif Position == "Manager":
    print("White Attire")
elif Position == "Director" and State in ("NY", "NJ", "PA"):
    print("Blue Attire")
elif Position == "Director" and State in ("TX", "LA", "AK"):
    print("Purple Attire")
elif Position == "Director":
    print("Orange Attire")
elif Position == "VP" and State in ("NY", "NJ", "PA"):
    print("Grey Attire")
elif Position == "VP" and State in ("TX", "LA", "AK"):
    print("Black Attire")
elif Position == "VP":
    print("Pink Attire")