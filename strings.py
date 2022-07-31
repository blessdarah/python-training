"""
    Program to manipulate and play with python strings
    Author: Bless Darah
    Created on: 31-07-2022
"""

sentence = "This is a sentence string"

students = ['bless', 'benoit', 'james'];


print("Students:", students)
print("lenght: ", len(students[0]))

print("length of sentence is", len(sentence))


# slice list
first10chars = sentence[:10]
top3student = students[:3]
last3Students = students[-3:]
#print("first10chars: ", top3student)
#print("first10chars: ", last3Students)
#print("get all but first 3 items: ", students[3:])


#print("ends with string?", sentence.endswith('string'))
#print("starts with string?", sentence.startswith('string'))
#print("split sentence into words: ", sentence.split(" "))
#print("Last two words in a sentence: ", sentence.split(" ")[-2:])
#print("print hello 3 times", "hello "*3)


# Replacing in strings
# destructive functions and non-destructive

greetings = "Hello, my name is bless. how are you doing today?"
greetings = greetings.replace("bless", "benoit")

#print("greetings: ", greetings)


# Changing cases
name = "Bless"
first_name = "Bless"
last_name = "Darah"
full_name = first_name + " " + last_name

print("lower: ", name.lower())
print("upper: ", name.upper())
print("title: ", greetings.title())
print("capitalize: ", greetings.capitalize())
print("swap case: ", name.swapcase())
print("full_name", "_".join([first_name, last_name]) )


web_url = "http://blessdarah.com/blog/"
blog_post = ["this is the title", "this is the post content", "31-07-22"]
title = web_url + blog_post[0].replace(" ", "-")

print('url:', title)

"""Testing"""
print("name is lowercase: ", name.islower())

username = input("Enter your username in uppercase only: ")

if not username.isdigit():
    print("please provide username only in uppercase")










