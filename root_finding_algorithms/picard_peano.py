# Picard-Peano method is another iterative method used to solve equations numerically such as finding roots of real-valued functions.
# Suppose we have the equation f(x) = 0, if we don't know how to solve it to find the root x, we can transform it in the form x = g(x)
# so we are solving the system of equations y = x and y = g(x). Geometrically this means that each root aproximation ξ will be the 
# solution for the system.
# If we start with a guess x0 and we calculate y0 = g(x0) we are going up in the graph (or down) until we find the curve y = g(x) at
# the point (x0, y0). We then choose x1 = y0 which means we are going left in the graph(or right) until we find the curve y = x at
# the point (x1, y0) and then we go down (or up) until we find the point (x1, 0). We can repeat this ladder process until we have a good
# enough approximation.  
# The succession is xn = g(xn-1). If it is convergent, in other words if there exists a value ξ such that ξ = lim n->inf (xn), then 
# lim(xn) = lim(g(xn-1)) = g(lim(xn-1)) = g(lim(xn)) which means ξ = g(ξ). So if the limit exists for the succession, it is the root
# of the function f.
# The method doesn't always converge to a value ξ (ξ = lim n->inf (xn)). In fact, it only happens if |g´(x)| < 1.
# The recurrence formula is xn+1 = g(xn).

import math
import pandas as pnd 


def f(x):
    return x - 3.6 + math.cos(x+1.2)**3
def g(x):
    return 3.6-math.cos(x+1.2)**3

def picard_peano_function_annulment(x0, g, tolerance):
    x = x0
    while abs(f(x)) > tolerance:
        x = g(x)
    return x
    
print(picard_peano_function_annulment(0.5, g, 1e-8))