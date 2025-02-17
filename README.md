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
Bisection Method is a root finding method that solves the form: f(x) = 0. 
* INPUTS: function (func), low guess (a), high guess (b), tolerance of error (tol), MAX number of iterations (N)
* CONDITIONS: f(x) must be continuous and defined on an interval [a,b], f(b)*f(b) < 0,
              a < b
* OUTPUT: Value which differs from a root of f(x) = 0 by less than tol

The current low guess, high guess, tol, and N for demonstration is (1, 2, 10^-5, 100) respectively
* Note these can be changed under:
```
# globals
TOL = 10**-5
A = 1
B = 2
N = 100
```

The current fucntion for demonstration is: f(x) = x^3 - x - 2
* Note this can be changed under:
```
def f(x):
     return (math.pow(x,3) - x - 2)
```

Run from command line:
```
$ ./bisection.py
Bisection method soln: x =  1.52138519287
```

### Fixed-Point Method
The Fixed-Point Iteration Method finds the root of an equation in the form: x = f(x) or g(x) = x - f(x)
* INPUTS: function (func), approximation (approx), tolerance of error (tol), MAX number of iterations (N)
* OUTPUT: Value which differs from a root of f(x) = 0 by less than tol

The current approx, tol, and N for demonstration is (4.6, 10^-4, 100) respectively
* Note these can be changed under:
```
# globals
APPROX = 4.6
TOL = 10**-4
N = 100
```

The current fucntion for demonstration is: f(x) = (1/tan(x))- (1/x) + x
* Note this can be changed under:
```
def f(x):
     return (1/math.tan(x)) - (1/x) + x
```

Run from command line:
```
$ ./fixedPoint.py
Fixed point solution: x = 4.49340945791
```
### Newton's Method
The Newton's Method finds the root of an equation:   x : f(x) = 0
* INPUTS: approximation (approx), tolerance of error (tol), MAX number of iterations (N)
* OUTPUT: THe value (guess) which differs from a root of f(x) = 0 by less than tol. Since the guess gets more accurate after every iteration, this is simply when the guess satisfies the following abs(guess - prev_guess) < tol

The current approx, tol, and N for demonstration is (4.6, 10^-4, 100) respectively
* Note these can be changed under:
```
# globals
APPROX = 0.1
TOL = 10**-5
N = 100
```

The current fucntion for demonstration is: f(x) = (1 + x)^204 - 440x - 1
* Note this can be changed under:
```
def f(x):
     return math.pow((1+x),204)-440*x-1
```

For Newton's Method we also need to know f'(x). Currently, f'(x) = 204*(1 + x)^203 - 440
* Note that this MUST be changed when f(x) is changed. Do this under:
```
def fprime(x):
     return 204*math.pow((x+1),203) - 440
```

Run from command line:
```
$ ./newtons.py
Newton's Method soln: x =  0.00681932148758
```

### Secant Method
The Newton's Method finds the root of an equation:   x : f(x) = 0. Considered an approximation of Newton's Method. It is convienienvt since you do not need f' like in Newton's Method
* INPUTS: approximation (approx), tolerance of error (tol), MAX number of iterations (N)
* OUTPUT: THe value (guess) which differs from a root of f(x) = 0 by less than tol. Since the guess gets more accurate after every iteration, this is simply when the guess satisfies the following abs(guess - prev_guess) < tol

The current approx, tol, and N for demonstration is (4.6, 10^-4, 100) respectively
* Note these can be changed under:
```
# globals
APPROX = 0.1
TOL = 10**-5
N = 100
```

The current fucntion for demonstration is: f(x) = (1 + x)^204 - 440x - 1
* Note this can be changed under:
```
def f(x):
     return math.pow((1+x),204)-440*x-1
```

Run from command line:
```
$ ./secant.py
Secant method soln: x =  0.00681932406799
```
