"""
Python program to learn about loops
Author: Bless darah
Date: 01-08-2022
"""
# for loop and while loop
# loop enable you to interat over an iterable

list_of_numbers = [1, 3, 5, 7, 9, 11]
odd = [2, 4, 6, 8, 10] # 5

index = 0;

# infinite loop
# exit condition for loops
# condition if true execute code inside the loop
while index < len(odd):
    print(f"value at {index}: {odd[index]}")
    index = index + 1
    

print("For loop example")
for n in list_of_numbers:
    print("number: ", n)

print("For loop example with index")
for index, n  in enumerate(list_of_numbers):
    print(f"number at {index}: {n}")




# sum 1 to 100 (first 100 numbers)
sum = 0
counter = 1

while counter <= 100:
    sum += counter # same as sum = sum + counter
    counter += 1  # same as counter = counter + 1

print("The sum from 1 to 100 is: ", sum)



