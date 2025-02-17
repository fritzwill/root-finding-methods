#!/usr/bin/env python2.7

# 9/12/2018
# finds the solution to f(x) = 0 using secant method

import math

# globals
APPROX = 0.1
TOL = 10**-5
N = 100

# function we are using
def f(x):
    return math.pow((1+x),204)-440*x-1

# Actual Secant Method
def secant(p0, p1, tol, N):
    for i in range(0, N):
        p = p1 - ((f(p1)*(p1-p0))/(f(p1) - f(p0)))
        if abs(p-p1) < tol:
            return p
        p0 = p1
        p1 = p
    return "Them method failed after {} iterations">format(N)        


print "Secant method soln: x = ", secant(.1,.09,pow(10,-5),100)
