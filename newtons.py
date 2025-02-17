#!/usr/bin/env python2.7

# Will Fritz
# 9/29/2017
# program to find solution to equation, namely f(x), using newton's method
# and secant method
import math
import time

def f(x):
    return math.pow((1+x),204)-440*x-1

def fprime(x):
    return 204*pow((x+1),203) - 500

def newtons(approx, tol, N):
    p0 = approx
    for i in range(0, N):
        p = p0 - (f(p0)/fprime(p0))
        if abs(p - p0) < tol:
            return p
        p0 = p
    return "The method failed after {} iterations".format(N)

def secant(p0, p1, tol, N):
    for i in range(0, N):
        p = p1 - ((f(p1)*(p1-p0))/(f(p1) - f(p0)))
        if abs(p-p1) < tol:
            return p
        p0 = p1
        p1 = p
    return "Them method failed after {} iterations">format(N)        

startTime = time.time()
output = newtons(.1, pow(10, -5), 100)
elapsedN = time.time() - startTime
startTime2 = time.time()
output1 = secant(.1,.09,pow(10,-5),100)
elapsedS = time.time() - startTime2

print "Newtons method soln: x =", output
print "Newtons time in seconds: {}".format(elapsedN)

print "Secant method soln: x =", output1
print "Secant time in seconds: {}".format(elapsedS)
