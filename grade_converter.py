# FILE NAME - grade_converter.py

##Jameisha Hardgers
#December 15, 2025 

percentage = float(input("Enter your percentage grade: "))

if percentage >= 90:
    letter_grade = "A"
elif percentage >= 80:
    letter_grade = "B"
elif percentage >= 70:
    letter_grade = "C"
elif percentage >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Your letter grade is: {letter_grade}")
