# Root_Finding_Techniques
Utilizing root solving techniques such as:
* Bisection Method
* Fixed-Point Method
* Newton's Method

Demonstrates numerical methods used to find solutions of nonlinear equations. Each script has a nonlinear function and error tolerance built into it, but both can be changed by the user. 

## Using the scripts

These three files are all python 2.7 scripts. Each has a shebang (```#!/usr/bin/env python2.7```) which allows them to be run from the command line. However make sure your python version is 2.7.*:
```
$ python --version
Python 2.7.9
```

### Bisection Method
Bisection Menthod is a root finding method that solves the form: f(x) = 0. 
* INPUTS: function (func), low guess (a), high guess (b), tolerance of error (tol), MAX number of iterations (N)
* CONDITIONS: f(x) must be continuous and defined on an interval [a,b], f(b)*f(b) < 0,
              a < b
* OUTPUT: Value which differs from a root of f(x) = 0 by less than tol

The current fucntion for demonstration is: f(x) = x^3 - x - 2
* Note this can be changed under:
```
def f(x):
     return (math.pow(x,3) - x - 2)
```

The current low guess, high guess, and tol for demonstration is (1, 2, 10^-5) respectively
* Note these can be changed under 
```
TOL = math.pow(10,-5)
A = 1
B = 2
```
Run from command line:
```
$ ./bisection.py
Bisection method soln: x = 1.52138519287
```
