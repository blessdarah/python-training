"""
program: program to get the name of a users
author: Bless Darah
reviewed by: Benoit
"""

first_name = "Bless"
last_name = "Darah"

# comment (ignored)
fullname = first_name + " " + str(100)

print("First name:", first_name)
print("Last name:", last_name)

# Show the users full name
print("Full name:", fullname)


# Numbers
num1 = 45
num2 = 8
print("sum: ", num1 + num2)
print("prod: ", num1 * num2)
print("div: ", num1 / num2)
print("modulus: ", num1 % num2)
print("quotient: ", num1 // num2)
print("diff: ", num1 - num2)
print("exponent: ", num1 ** num2)

# comparison
print("equal: ", num1 == num2)
print("is greater? ", num1 > num2)
print("is less? ", num1 < num2)
print("is less or equal? ", num1 <= num2)
print("is less or equal? ", num1 != num2)


# Get user input
n1 = input("Enter a number: ")
n1 = int(n1) # typecasting converting var of type a to var of type b

n2 = int(input("Enter a second number: "))
name = str(input("Enter your name: "))
