GPA = float(input("Enter your GPA: "))
exam = float(input("Enter your entrance exam score: "))

if GPA >= 4.0 or (GPA >= 3.5 and exam >= 80) or (GPA >= 3.0 and exam >= 90) or (GPA >= 2.5 and exam == 100):
    print("Congratualations! You got admission to our prestigious college.")
else:
    print("We are sorry. You do not meet the admission criteria.")