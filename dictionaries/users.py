"""
Program to learn more about dictionaries
Author: Bless Darah
Date: 28/08/22
"""
# Think of dictionaries as object (key => value) pair
user = {
    "first_name": "Bless", # [firstname, bless]
    "last_name": "Darah", # [lastname, darah]
    "age": 10 # [age, 10]
}

user['address'] = 'Limbe'
user.pop('age')
del user['address']

user['street_address'] = '123 bambili road'
user.update({"address": "Bamenda", "first_name": "James"})

#loop through obj
# for key, value in user.items():
 #    print("key: ", key)
  #   print("value: ", value)

# print("obj keys", user.keys())
# print("obj values:", user.values())


# copying dict
user2 = user.copy()
user3 = dict(user)


# Functions
# not repeat yoursel
# functions have parameters (or orguments) => needs of a function (dependencies)
# return value (something or nothing)
    # nothing: printing
# def function_name(parameter1, p2, p3...):
    # execute
   # return

# Function to print a user objec on screen
def print_user(user, message = "Printing object"):
    print(message)
    for key, value in user.items():
        print(f"{key}: {value}")
    return



print_user(user3, "Printing user copy");
