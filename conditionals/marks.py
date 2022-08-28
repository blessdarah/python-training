"""
Python program to grade student marks
Author: Bless darah
Date: 01-08-2022
"""

# 0 - 49 = F
# 50 - 69 = C
# 70 - 79 = B
# 80 - 79 = A

score = int(input("Enter the score for chemistry level 01: "))
if score < 0:
    print("You cannot have a negative value:")
    print("try again")
else:
   # number is > 0 
   if score < 50:
       print("Grade: F")
   elif score >= 50 and score < 70:
       print("Grade: C")
   elif score >= 70 and score < 80:
       print("Grade: B")
   elif score >= 80:
       print("Grade: A")
#   else:
#       print("Grade: A")

gender = input("Enter your gender m for male and f for female")

if gender == 'm':
    print("Gender: male")
elif gender == 'f':
    print("Gender: female")
else:
    print("We cannot recognize your input")



