"""
    Program to manipulate and play with lists in python
    Author: Bless Darah
    Created on: 31-07-2022
"""

# length 5: last element is 4, and first is at 0
# as list of lenght n has last el at n-1 and first at 0
list_of_numbers = [1, 3, 5, 7, 9, 11]
odd = [2, 4, 6, 8, 10]

# Add to a list from behind
list_of_numbers.append(43)
print("append 43: ", list_of_numbers)

# Add to a list from front
list_of_numbers.insert(0, 18)
print("insert 43 at 0: ", list_of_numbers)

# remove at element
list_of_numbers.remove(5)
print("remove 5: ", list_of_numbers)


# remove at element
list_of_numbers.clear()
print("clear: ", list_of_numbers)


# remove at element
list_of_numbers.extend(odd)
print("list: ", list_of_numbers)


# remove at element
print("count number of 2s: ", list_of_numbers.count(2))


# index or positon of an element
print("index of 4 in list: ", list_of_numbers.index(4))

# pop remove last element (stack)
print("pop value: ", list_of_numbers.pop())
print("new list after pop function: ", list_of_numbers.sort(reverse = True));

# index or positon of an element
#print("index of 4 in list: ", list_of_numbers.index(4))

