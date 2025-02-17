#!/usr/bin/env python2.7

# Will Fritz
# 9/28/2017
# Finds the root of equation in the form of x = f(x) or g(x) = x - f(x) by using the fixed point method
import math

# function to test using python syntax in form g(x) = x - f(x)
def f(x):
    return x - math.tan(x)
    
def fixedPoint(func,  approx, tol):
