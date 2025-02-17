#!/usr/bin/env python2.7

# Will Fritz
# 9/28/2017
# Finds the root, or solution, of the form f(x) = 0. It uses:
# abs((w(n)-w(n-q))/w(n)) <= 10^-5

import math

# give python eqn of the formula using python math syntax 
def f(x):
    return (-32.17/(2*math.pow(x,2)))*(((math.exp(x)-math.exp(-x))/2) - math.sin(x)) - 1.7

def bisect(func, low, high, tol):
    # switch low and high if low is larger than high
    if low > high:
        low = temp
        low = high
        high = temp
    # check if valid input
    if func(low)*func(high) > 0:
        print "Check input for low and high guess (f(low) and f(high) must have different signs)"
    
    lastFuncVal = func(low)
    while(True):
        mid = (high+low)/2.0
        if abs(func(mid) - lastFuncVal)/abs(func(mid)) <= tol:
            return mid
        # same sigh
        if func(mid)*func(low) > 0:
            low = mid
        # diff sign
        else:
            high = mid
        lastFuncVal = func(mid)

print bisect(f, -1, -.001, math.pow(10,-5))
