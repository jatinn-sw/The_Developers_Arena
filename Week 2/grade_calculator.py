marks = float(input("Enter your marks (out of 100): "))

if marks >= 90:
    print("Your grade is A")
    print("Outstanding performance!!")
elif marks >= 80:
    print("Your grade is B")
    print("Excellent job! Keep pushing!!")
elif marks >= 70:
    print("Your grade is C")
    print("Good effort! However you can do better.")
elif marks >= 60:
    print("Your grade is D")
    print("You passed, but there's more room to improve.")
else:
    print("Your grade is F")
    print("Don't give up, every failure is a step closer to success.")