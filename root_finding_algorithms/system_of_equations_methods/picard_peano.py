# Picard-Peano method when applied to a system of equations f1(x,y) && f2(x,y) requires that we transform  it in the 
# form x = g1(x,y) && y = g2(x,y).
# The successions are xn = g1(xn-1, yn-1) && yn = g2(xn-1, yn-1).
# Like we had seen when applied to just an equation we need to check if for both successions the iteration process 
# converges to two values ξ and η, in other words if the limits ξ = lim n->inf (xn) and η = lim n->inf (yn) exist.
# As proved for one variable, if both of them exist, they are the solution to the system.
# The method only converges to the values ξ and η  if |g1'x| + |g2'x| < 1 && |g1'y| + |g2'y| < 1
# The reccurence formulas are xn+1 = g1(xn,yn) && yn+1 = g2(xn,yn)

import math as m

def f1(x, y): return 2 * x * x - x * y - 5 * x + 1

def f2(x, y): return x + 3 * m.log10(x) - y * y

def g1(x, y):  
    return m.pow((x * y + 5 * x - 1) / 2, 1 / 2)


def g2(x, y): 
    return m.pow(x + 3 * m.log(x), 1 / 2)


def picard_peano_iterations(x0, y0, f1, f2, iterations):
    x = x0
    y = y0 
    for i in range(iterations):
        xcopy = x
        x = g1(x,y)
        y = g2(xcopy, y)
    return (x, y)

def picard_peano_absolute_precision(x0, y0, f1, f2, tolerance):
    x = 1
    y = 1

    while abs(x - x0) > tolerance or abs(y-y0) > tolerance:
        x0 = x
        y0 = y
        x = g1(x0,y0)
        y = g2(x0, y0)
    return (x, y)

print(picard_peano_absolute_precision(10, 0, f1, f2, 1e-8)) 