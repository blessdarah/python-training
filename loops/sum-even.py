"""
Python program to get the sum of all even numbers from 1 to n
where n is an interger
Author: Bless darah
Date: 01-08-2022
"""

n = int(input("Enter a maximum number to sum to: "))

counter = 2
sum = 0
while counter <= 100:
    sum += counter
    counter += 2

print(f"Sum of all even numbers from 1 to {n} is: {sum}")


# Exerceise
"""
Write a program to get the sum of all odd numbers from 1 to n
where n is an integer and n is from a user input
"""
print("printing the sum of all odd numbers from 1 to n")

odd_sum = 0

for n in range(1, n):
    if n % 2 == 1:
        odd_sum += n

print(f"Odd sum is: {odd_sum}")


