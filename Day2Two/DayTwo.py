# Data types, Numbers, Operations, Type conversion, f-Strings
# DATA TYPES
# Primitive data types
# Strings, Integers, Float, Booleans

# print("Hello"[0])
# output:H
# print(input("Enter your name:")[0])
# output: Enter your name:Sujit
# S

# print("123"+" is a string here")
# print("123"+"456")
# print(123+456)
# output
# 123 is a string here
# 123456
# 579

# Integer
# number=123+345
# print(number)
# print(1234567890)

# Float
# float=123.45
# print(float)
# print(1123.4)

# Boolean
# print(True)
# print(False)

# Type Error and Type Checking and Conversion
# print(len(12345))  TypeError : Object of the int has no len()
# num=12345
# print(len(num))       TypeError: object of the int has no len()
# print(len("Hello world"))

# How to check the datatype of a data
# by using type() function
# print(type(123))
# print(type("Sujit"))
# print(type(10>20))
# print(10>20)

# Convert A piece of data into different datatype
# num = "1123"
# print(type(num))
# int(num)
# print(type(int(num)))
# Output
# 11
# <class 'int'>
# <class 'str'>
# <class 'bool'>
# False
# <class 'str'>
# <class 'int'>

# age=25
# name="sujit"
# print("My name is ",name)
# print(name+age) Error
# print(name,age)
# Find the Error
# print("Number of letters in your name"+len(input("Enter your name:")))
# print("Number of letters in your name",len(input("Enter your name:")))
# or
# length=len(input("Enter your name:"))
# print("Number of letters in your name",length)

# output
# My name is  sujit
# sujit 25
# Enter your name:Sujit
# Number of letters in your name 5
# Enter your name:Sujit
# Number of letters in your name 5


# Mathematical Operation
# PEMDAS
# parenthesis, Exponential, Multiplication, Division, Addition, Subtraction
# (),**,*,/,+,-
# print("My age is "+str(22))
# print(12+13)
# print(30-10)
# print(30*10)
# print(30/10)
# print(30%4)
# print(type(30/4))
# print(57/4)
# print(57//4)
# print(10**2)
# print(100+50-3*20/3)

# output
# My age is 22
# 25
# 20
# 300
# 3.0
# 2
# <class 'float'>
# 14.25
# 14
# 100
# 130.0

# BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight.
# This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the person's height squared.
# Convert this sentence into code on line 6.

# height = 1.78
# weight = 63
# bmi=weight/height**2
# print(bmi)

# output
# 19.883853048857468

# Number manipulation and F strings in python
# print(round(bmi))
# 20
# round() defines if the floating value below .5 it is same number else number+1
# num=23.4
# print(round(num))    #23
# num=23.6
# print(round(num))    #24
# num=23.5
# print(round(num))    #24
# print(round(num,2))  #23.5

# Assignment operator
# score = 0
# score+=1
# print(score)
# output: 1

# f-strings
# print("The score is :"+str(score))
# print("The score is :",score)
# output
# The score is :1
# The score is : 1

# score = 20
# height = 28.4
# is_winning = True
# print(f"Your score is {score}, Your height is {height}, your winning is {is_winning}")      #your score is 20
# output: Your score is 20, Your height is 28.4, your winning is True

# result = int("5")/int(2.3)
# print(type(result))

# Calculator Project
# If the bill was $150.00 split between 5 people with 12% tip.
# Each person should pay
# (150.00/5)*1.12=33.6
# After formating the result to 2 decimal points = 33.60

print("Welcome to the tip calculator")
bill=float(input("What is the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10,12,15:"))
people=int(input("Enter the number of people:"))
bill_with_tip=tip/100*bill
print(bill_with_tip)
tip_as_percentage=tip/100
total_tip_amount=bill*tip_as_percentage
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
print(round(bill_per_person,3))
print(f"Each person should pay ${bill_per_person}")


