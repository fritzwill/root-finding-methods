#!/usr/bin/env python2.7

# 9/29/2017
# program to find solution to equation, namely f(x) = 0, using newton's 
# method

import math
import time

# globals
APPROX = 0.1
TOL = 10**-5
N = 100

# functions we are using, namely f and f'
def f(x):
    return math.pow((1+x),204)-440*x-1

def fprime(x):
    return 204*math.pow((x+1),203) - 440

# Actual Newton's Method
def newtons(approx, tol, n):
    p0 = approx
    for i in range(0, n):
        p = p0 - (f(p0)/fprime(p0)) # this is the calculation of the guess
        if abs(p - p0) < tol:
            return p
        p0 = p
    return "The method failed after {} iterations".format(n)

# Call the method and print its answer
output = newtons(APPROX, TOL, N)
print "Newton's method soln: x = ", output
