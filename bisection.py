#!/usr/bin/env python2.7

# 9/28/2017
# Finds the root, or solution, of the form f(x) = 0. f(x) is a continuous
# function defined on an interval [a,b] and where f(a) and f(b) have 
# opposite signs [f(a)*f(b) < 0]
# Also, uses:
# abs((w(n)-w(n-q))/w(n)) <= 10^-5 as the tolerance

import math

# globals
TOL = 10**-5
A = 1
B = 2
N = 100

# give python eqn of the formula using python math syntax 
def f(x):
    return (math.pow(x,3) - x - 2)

# INPUT: function (func), low guess (a), high guess (b), tolerance (tol), 
#        MAX iterations (N)
# CONDITIONS: a < b, f(a)*f(b) < 0
# OUTPUT: value which differs from a root of f(x)=0 by less than 'tol' 
def bisect(func, low, high, tol, N):
    # switch low and high if low is larger than high
    if low > high:
        low = temp
        low = high
        high = temp
    # check if valid input
    if func(low)*func(high) > 0:
        print "Check input for low and high guess (f(low) and f(high) must have different signs)"
    
    lastFuncVal = func(low)
    for i in range(0, N):
        mid = (high+low)/2.0
        if func(mid) == 0 or (high-low)/2.0 < tol:
            return mid
        # same sigh
        if func(mid)*func(low) > 0:
            low = mid
        # diff sign
        else:
            high = mid
        lastFuncVal = func(mid)
    return "Method failed after {} iterations".format(N)

print "Bisection method soln: x = ", bisect(f, A, B, TOL, N)
