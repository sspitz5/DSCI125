#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:10:54 2019

@author: sarahspitz
"""

#Pset 1 Part A

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
# set up while that breaks when current savings reaches total cost 
##decide whether its < or <= 
##check that float rules are okay so that it is not infinite while
num_months = 0
while (current_savings < to_pay):
    current_savings += (current_savings*r/12) + mss
    num_months = num_months + 1
    
#print number of months to reach goal
num_months_str = str(num_months)
print("Number of months: " + num_months_str)

## Tests 1 and 2 work
    