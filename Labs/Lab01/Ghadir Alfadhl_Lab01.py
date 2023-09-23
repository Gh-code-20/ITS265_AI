# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 09:08:57 2021

@author: Ghadir Alfadhl
"""

""" 
Write a Python code to ask user to enter two values and operation 
(addition, subtraction, multiplication, division). 
Read them and show an answer.

"""

"""
Ghadir Alfadhl
ITS265
09/05/2021

"""


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("\nEnter the Operator (+,-,*,/): ", end="")

ch = input()

if ch=='+':
    print("\n" +str(num1)+ " + " +str(num2)+ " = " +str(num1+num2))
elif ch=='-':
    print("\n" +str(num1)+ " - " +str(num2)+ " = " +str(num1-num2))
elif ch=='*':
    print("\n" +str(num1)+ " * " +str(num2)+ " = " +str(num1*num2))
elif ch=='/':
    print("\n" +str(num1)+ " / " +str(num2)+ " = " +str(num1/num2))
else:
    print("\nInvalid Operator!")
