#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:11:54 2019

@author: sarahspitz
"""

## Pset 1 Part B
## Extrapolated from part 1a, lines 37 and 44-47 are new

# initialize portion down payment
portion_down_payment = .25

# initialize current savings
current_savings = 0

# initialize anual return rate
r = .04
# monthly interest increment
mii = current_savings*r/12

# request annual_salary
annual_salary = int(input("Enter your annual salary: "))
#monthly_salary = annual_salary/12
# request portion saved
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# monthly salary savings
mss = annual_salary*(portion_saved)/12

# request total cost
total_cost = int(input("Enter the cost of your dream home: "))
# the amt to save to is total cost* down payment percent
to_pay = total_cost*portion_down_payment

# request semi annual raise
semi_annual_raise = float(input("Enter the semi annual raise, as a decimal: "))

# set up while that breaks when current savings reaches total cost 
##decide whether its < or <= 
##check that float rules are okay so that it is not infinite while
num_months = 0
while (current_savings < to_pay):
    if num_months > 0 and num_months%6 == 0:
        # add raise and adjust salary if number of months is greater than zero and divisible by 6 
        # adjust how the monthly savings from salary
        mss = (annual_salary + annual_salary*semi_annual_raise)*portion_saved/12
    #regardles we shall add on another month and its savings from interest and salary because the current savings aren't sufficient
    current_savings += (current_savings*r/12) + mss
    num_months = num_months + 1
    
#print number of months to reach goal
num_months_str = str(num_months)
print("Number of months: " + num_months_str)

