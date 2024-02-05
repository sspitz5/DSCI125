#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:36:23 2019

@author: sarahspitz
"""

import numpy

## Pset 0
# get x and y from the user
x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
# create string variable that's x to the y
xToY = str(x**y)
# print x**y and the value, can use comma and have space inserted(strings)
print ("x**y =", xToY)
# create var that is log base 2 of x using numpy or matplotlib pkgs
# and print the value of log(x)
#   but it prints log(x) = 1.0 and the asn has just 1
#   cast into an integer to not have the extra .0
lx = int(numpy.log2(x))
print ("log(x) = ",lx)

