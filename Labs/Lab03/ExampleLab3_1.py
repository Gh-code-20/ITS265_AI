#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:19:38 2021

@author: sharylriley
"""

#example args and kwargs
#*args and ** kwargs used in function
# definitions to pass an unspecified number if 
# arguements to a functions - do not need to know how many
# many arguements will be passed to your function.

# args used to pass non-keyboarded variable lenght arguement list 
# to a function. 
# kwargs used to pass keyworded variable length of arguements to a function. 
# It is used if you want to handle named arguements. 

def test_var_args(f_arg, *argv):
   
    print("First regualr arg: " ", f_arg")
    for arg in argv:
         print("Another arg through argv: " , arg)
    
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

def test_var_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

#Test first function shown above using argv
test_var_args('First Regular Arg', 'Cleaning Robot', 'Assembly Robot', 'Bi-Pedal Robot')

print("")

greet_me(Name="Hello we are testing kwards!")
print("")

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_var_kwargs(**kwargs)
