grade = input("Enter your the number right divided by total questions: ")
try:
    grade = float(grade)
except:
    grade = 0
    print("What you talkin' bout Willis?")
    quit()
if grade >= 0.9 :
    score = "A"
elif grade >= 0.8:
    score = "B"
elif grade > 0.7:
    score = "C"
elif grade > 0.6:
    score = "D"
else :
    score = "F"
print(score)
