# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 14:57:46 2022

@author: garth
"""

target = False
actual = "false"

def truth_mapper(target, actual):
    """Define your target and actual, and map accordingly"""

    # No change
    # Stay True
    if target == True and actual == "True":
        return actual
    elif target == True and actual == "true":
        return actual
    elif target == True and actual == True:
        return actual
    # Stay False
    if target == False and actual == "False":
        return actual
    elif target == False and actual == "false":
        return actual
    elif target == False and actual == False:
        return actual

    # Change
    # Trueify
    if target == True and actual == "False":
        return "True"
    elif target == True and actual == "false":
        return "true"
    elif target == True and actual == False:
        return True
    # Falsify
    if target == False and actual == "True":
        return "False"
    elif target == False and actual == "true":
        return "false"
    elif target == False and actual == True:
        return False
    
    else: 
        return "None"
    
zzz = truth_mapper(target, actual)
