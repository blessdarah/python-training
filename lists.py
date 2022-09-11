"""
    Program to manipulate and play with lists in python
    Author: Bless Darah
    Created on: 31-07-2022
"""
ls = [3, 5, 8, 11, 0, 18, 22]
ls2 = [1,5, 11, 9, 8, 21, 3]

# lambda functions
# fn name = lambda params (a, b, ...): a + b + ... + n
isEven = lambda number: number % 2 == 0

double_list = [x for x in ls if isEven(x)]

print(double_list)

greetings = lambda name = "user": print(f"Hello {name}, welcome")
sayHi = lambda name = "user", age = 10: print(f"Hello {name}, you are {age} years old today")
sayHi()
#print(ls[::-1])
#reverse = ls.reverse()
#print("reverse", ls)
#print("entire list: ", ls[0:])
#print("print in steps of 2", ls[0:5:2])
