"""
program: Program to grade a score from 1 - 20
author: Bless Darah
"""

# Ask for a score between 1 and 20
score = 0
try:
    score = int(input("Enter a score between 1 - 20: "))
except Exception:
    print("Provide a number only: default of 0 selected")

# Ask for user's name
username = ""
try:
    username = str(input("Enter your username: "))
except Exception:
    print("Error occured")
# print user's name and the score

print("Hello ", username)
print("You have entered the number: ", score)

