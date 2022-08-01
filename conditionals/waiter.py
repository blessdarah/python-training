"""
Learning about conditional in python
Author: Bless Darah
Date: 01-08-2022
"""

name = input("Enter your name: ")
age = int(input("How are old are you? "))

print(f"Hello {name}, nice to have you here.")
# below 13 kid
if age < 13:
    print("We notice you're a kid, we can't give you a drink")

if(age >= 13 and age <= 19):
    print("You're a teenager and we still can't give you a drink")

if(age >= 20):
    print("Welcome, what will you like to drink?")
    drink = input("Place your choice here: ")
    print(f"Alright {name}, the waiter will serve you with a glass of {drink}")
    print('Have a great time. Cheers!')

# 13 - 19 teenager

# 20 and above young adult
