# Question 2) You have to given s String and you have to capitalise first two character  of the string
# Given a full name and you to capitalise the name appropriately

# Sample Input :
# John bob

# Constraint
#  0<=len(s)<=1000
# The String consists of alphanumeric  character and spaces

# Sample Output :
# JOhn BOb

def capitalize_first_second_letters(str1):
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[0].upper() + word[1].upper() + word[2:] + " "
     return result 
     
name=input("Please enter your name : ")
print("Before capitalization : ", name)
print("After capitalization :", capitalize_first_second_letters(name))
