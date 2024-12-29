# Introduction
# The string is the combination of charecters, and To tell our system it is a string we use this inside the double quotation

# print("Hello world");
# output : Hello world
# print("Hello world")
# output : Hello world

# String concatenation
# The string is the combination of charecters, and To tell our system it is a string we use this inside the double quotation

# print("My name is sujit saran \n I am from Jajpur")
# Output
# My name is sujit saran
# I am from jajpur
# print("Hello "+" My name is sujit saran")
# Output: Hello My name is sujit saran

# Indentation Error
#     print("Hello") Throws an Error

# python input function
# we use input function to get user input
# input("What is your name?")
# Output
# What is your name? here ask your name
# print("Hello "+ input("What is your name? "))         here first input will execute and ask your name the finally print Hello <Your name>
# Output
# What is your name? here ask your name
# Hello <Your name>

# Adding and exclamation at the end of the sentence
# print("Hello "+ input("What is your name:")+ "!")      Same here first input will execute and ask your name then print Hello <Your anme is printed> then !
# Output
# What is your name?Sujit saran
# Hello Sujit saran!

# Python variables
# name=input("Enter your name:")
# print(name)
# print(type(name))
# Output
# Enter your name:Sujit
# Sujit
# <class 'str'>

# name="sumit"
# print(name)
# Output: Sumit

# Can you calculate the total number of charecters in the string
# print(len(name))
# Output : Sumit

# print(len(input("Enter your name:")))
# output; Enter your name:Sujit saran
# 11

# Can you use what you've learned about creating variables and using variales in order to take these two parts, the input() function,
# and the output() function and store them in a separate variable
# username=input("Enter the username:")
# print(username)
# print(len(username))
# Output
# Enter the username:Sujit saran
# Sujit saran
# 11

# Question
# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch
# the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise.
glass1="milk"
glass2="juice"
temp=glass1
glass1=glass2
glass2=temp
print("glass1:"+glass1)
print("glass2:"+glass2)
# output
# glass1:juice
# glass2:milk

# Variable Naming
username="sujit"
# user name="sujit"    not a valid variable
user_name="sujit"

# Band name generator project
# create a greeting for your program...., Ask the user for the city that they grew up in and store it in a variable
# Combine the name of their city and pet and show them their band name
print("Welcome To Band name generator project")
user_city=input("Enter your city:")
user_pet=input("Enter your pet:")
print("The name of your band is:"+user_city+""+user_pet)
