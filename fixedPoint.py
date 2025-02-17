#!/usr/bin/env python2.7

# 9/28/2017
# Finds the root of equation in the form of x = f(x) or g(x) = x - f(x) by using the fixed point method
import math

# globals
APPROX = 4.6
TOL = 10**-4
N = 100

# function to test using python syntax in form g(x) = x - f(x)
def f(x):
    return (1/math.tan(x)) - (1/x) + x
    
def fixedPoint(func,  approx, tol, n):
    for i in range(0, n):
        p = func(approx)
        if abs(p-approx) < tol:
            return p
        approx = p
    return "Method failed after {} iterations".format(n)

print "Fixed point soln: x = ", fixedPoint(f, APPROX, TOL, N) 
