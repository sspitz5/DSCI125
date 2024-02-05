#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:11:57 2019

@author: sarahspitz
"""

# Pset 1 Part C

#set semi annual raise, annual return rate, down payment portion, and cost, find correct portion of salary to save
semi_annual_raise = .07
r = .04
portion_down_payment = .25
total_cost = 1000000
to_pay = total_cost*portion_down_payment
# want to achieve in 36 months
# be within 100 dollars of down payment
num_months = 36
err = 100

# enter starting annual salary
annual_salary = int(input("Enter the starting salary: "))

# initialize number of steps for binary search
num_steps = 0

#guess somewhere in between .0000 and 1.000
#but search for an integer between 0 and 10,000 
hi = 10000
lo = 0
#portion saved is savings rate out of salary we are guessing
portion_saved = hi
current_savings = 0

#first check that you can in fact reach the goal in 36 months (check endpoint)
for month in range(0, num_months -1):
        if month > 0 and month%6 == 0:
        # add raise and adjust salary if number of months is greater than zero and divisible by 6 
        # adjust how the monthly savings from salary
            mss = (annual_salary + annual_salary*semi_annual_raise)*(portion_saved*10**-4)/12
            #regardles we shall add on another month and its savings from interest and salary because the current savings aren't sufficient
        current_savings += (current_savings*r/12) + mss
if current_savings < to_pay:
    print ("It is not possible to pay the down payment in 36 months, 3 years.")
else:
    steps = 0
    #while the amount saved within 36 mo is not within 100 
    while abs(current_savings - to_pay) > 100:
        #set up everything for next iteration of while loop
        current_savings = 0
        mss = 0
        #next guess is halfway in search
        portion_saved = (hi + lo)/2
        #increment steps for binary search, at the top is first one to go through
        steps = steps + 1
        #find the sum (current savings) after you've saved for 36 months
        for month in range(0, num_months -1):
            if month > 0 and month%6 == 0:
                # add raise and adjust salary if number of months is greater than zero and divisible by 6 
                # adjust how the monthly savings from salary
                # declare annual salary increase with raise
                new_monthly_sal = (annual_salary + annual_salary*semi_annual_raise)/12
                mss = new_monthly_sal * (portion_saved*10**-4)
            #regardles we shall add on another month and its savings from interest and salary because the current savings aren't sufficient
            current_savings = current_savings + (current_savings*r/12.0) + mss
        #before comparing current savings to portion to pay, scale it down by 100 because portion saved is saled up by 100
        #current_savings = current_savin
        #if the sum after you've saved for 36 months is greater than the to pay, then see if you can lower the savings rate and make hi the current guess
        if current_savings > to_pay:
            hi = portion_saved
        else:
            #otherwise search above (need a higher savings rate) and lower bound made equal to current guess
            lo = portion_saved
    portion_saved_str = str(float(portion_saved)*(10**-4))
    print ("Best savings rate: " + portion_saved_str)
    print ("Steps in bisection search: " + str(steps))
    


#use bisection search
