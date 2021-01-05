import math as m
import pandas as pnd

def f(x):
    return (2 * x + 1) ** 2 - 5 * m.cos(10 * x)

def aurea(x1, x2, f, tolerance, minumum):
    F = f
    if not minumum:
        F = lambda x: -f
    B = (5**0.5 - 1.0)/2.0  #golden ratio
    A = B**2
    x3 = x1 + A * (x2-x1)
    x4 = x1 + B * (x2-x1)
    while abs(x1 - x2) > tolerance:
        if F(x3) < F(x4):
            x2 = x4
            x4 = x3
            x3 = x1 + A*(x2-x1)
        else:
            x1 = x3
            x3 = x4
            x4 = x1 + B*(x2-x1)
    return [x1,x2,x3,x4] 


def aurea2(x1, x2,f, tolerance):
    B = (5**0.5 - 1.0)/2.0  #golden ratio
    A = B**2
    x3 = 0
    x4 = 0
    while abs(x1 - x2) > tolerance:
        x3 = A*(x2-x1)+x1
        x4 = B*(x2-x1)+x1
        if f(x3) < f(x4):
            x1 = x3
        else:
            x2 = x4
    return [x1,x2,x3, x4] 

print(aurea(-0.779, -0.471, f, 1e-3, True ))

