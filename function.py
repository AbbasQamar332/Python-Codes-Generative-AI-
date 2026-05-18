# A function is a block of reusable code that performs a specific task.

# Instead of writing the same code again and again, we create a function and call it whenever needed

# print("Hello Abbas")
# print("Hello Abbas")
# print("Hello Abbas")
# def a1():
#     print("Hello Abbas")

# a1()
# a1()
# a1()
# Benefit: write once → use many times.
# syntax of function
# def function_name():
#     code

# Example
# def hello():
#     print("Welcome")

# hello()
# Explanation:

# def = keyword to create function
# hello = function name
# () = parameters place
# : = start function block
# indentation matters
# 3) Function Calling

# Creating function does not run it.

# You must call it:

# def test():
#     print("Function executed")

# test()

# 4) Parameters and Arguments

# Parameters receive values.

# def F1(name):
#     print("Hello",name)
# F1("Ali")

# # Output:

# Hello Ali

# Here:

# name → parameter

# Ali → argument

# Multiple parameters
# def student(name,age):
#     print(name)
#     print(age)

# student("Ali",20)
# 5) Types of Arguments

# Python supports several argument types.

# A) Positional arguments

# Order matters.

# def info(name,age):
#     print(name,age)

# info("Ali",20)

# Wrong:

# info(20,"Ali")
# B) Keyword arguments
# def info(name,age):
#     print(name,age)

# info(age=20,name="Ali")

# Order does not matter.

# C) Default arguments
# def country(name="Pakistan"):
#     print(name)

# country()
# country("Turkey")

# Output:

# Pakistan
# Turkey
# D) Arbitrary Arguments (*args)

# Unknown number of values.

# def total(*numbers):
#     print(numbers)

# total(1,2,3,4)

# Output:

# (1,2,3,4)
# E) Keyword Arbitrary (**kwargs)
# def data(**details):
#     print(details)

# data(name="Ali",age=20)

# Output:

# {'name':'Ali','age':20}

# 6) Return Statement

# return sends value back.
# def add(a,b):
#     return a+b

# result=add(2,3)

# print(result)

# Output:

# 5

# Without return:

# def add(a,b):
#     print(a+b)

# Difference:

# print() → shows value

# return → sends value

# 7) Local Variables

# Created inside function.

# def test():
#     x=10
#     print(x)

# test()

# Outside:

# print(x)

# Error:

# NameError

# Because local variable only exists inside function.


# 8) Global Variables
# x=100

# def show():
#     print(x)

# show()

# Output:

# 100

# Using global keyword:

# x=5

# def test():
#     global x
#     x=20

# test()

# print(x)

# Output:

# 20

# 9) Recursion

# Function calling itself.

# def count(num):

#     if num==0:
#         return

#     print(num)

#     count(num-1)

# count(5)

# Output:

# 5
# 4
# 3
# 2
# 1

# Used carefully.

# 10) Lambda Function

# Small anonymous function.

# Syntax:

# lambda arguments : expression

# Example:

# square=lambda x:x*x

# print(square(5))

# Output:

# 25

# Multiple values:

# sum=lambda a,b:a+b

# print(sum(2,3))


# 11) Higher Order Functions

# Functions that take another function.

# Example:

# def square(x):
#     return x*x

# numbers=[1,2,3]

# result=map(square,numbers)

# print(list(result))

# Output:

# [1,4,9]



# def count(num):

#     if num==0:
#         return

#     print(num)

#     count(num-1)

# count(5)



def squra(x):
    return x*x

print(squra(5))