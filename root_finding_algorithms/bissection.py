# Bissection is a bracketing method used to find the root of a real-valued function by applying Bolzano's theorem which states that if we
# have a real-valued function continuous at the inteval [a,b] then if f(a) and f(b) have oposite signs, the function must at 
# some point cross the x-axis.
# The method consists of bissecting the interval [a,b], calculating the middle point c (c = a+b/2) and choosing the interval with the change in sign of the function
# Each iteration reduces the length of the interval by half
# If an interval which posesses more than one root is given, the algorithm will only find one of them but it will not denounce the others
# As it is a bracketing method, bissection always converges to a value if the function is continuous in the interval and if f(a) and f(b) have oppositve signs
# It is a method of relative slow convergence because it does not use the values f(a) and f(b), only its signs
# the number of iterations n needed to converge to a root to within a certain tolerance ε (error guaranteed to be at most ε) is bounded by
# n <= log2(|b-a| / ε) and n <= nm + log2(b-a)

import math
import pandas as pnd


def f(x):
    return math.sin(x) +x**5-0.2*x+1

def g(x):
    return x**2-2

def h(x):
    return x**3-5*x

def bissection_absolute_precision(a, b, f, tolerance):
    cols = {"a":[], "b":[], "c":[], "f(a)":[], "f(b)":[], "f(c)":[], "|b-a|":[]}
    while True:
        c = (a+b)/2.0
        cols["a"].append(a)
        cols["b"].append(b)
        cols["c"].append(c)
        cols["f(a)"].append(f(a))
        cols["f(b)"].append(f(b))
        cols["f(c)"].append(f(c))
        cols["|b-a|"].append(abs(b-a))
        if abs(a-b) > tolerance:
            break
        if f(a)*f(c) < 0:
            b = c
        elif f(a)*f(c)>0:
            a = c

    data = pnd.DataFrame(cols, columns=["a", "b", "c" ,"f(a)", "f(b)", "f(c)", "|b-a|"])
    print("\n",data) 
    return c 

def bissection_iterations(a, b, f, iterations):
    c = 0
    for i in range(iterations):
        c = (a+b)/2.0
        if f(a)*f(c) < 0:
            b = c
        elif f(a)*f(c)>0:
            a = c
    return c

#in the stop criteria, you can divide by either a, b or c. It is not important
#which one you choose, as long as the concept of it being a relative precision criteria
#stays intact (which it keeps for all three options)
def bissection_relative_precision(a, b, f, tolerance):
    c = 0
    while abs((a-b)/a) > tolerance:
        c = (a+b)/2.0  
        if f(a)*f(c) < 0:
            b = c
        elif f(a)*f(c)>0:
            a = c      
    return c

def bissection_function_annulment1(a, b, f, tolerance):
    c = 0
    while abs(f(a) - f(b)) > tolerance:
        c = (a+b)/2.0  
        if f(a)*f(c) < 0:
            b = c
        elif f(a)*f(c)>0:
            a = c
    return c

def bissection_function_annulment2(a, b, f, tolerance):
    c = 0
    while abs(f(c)) > tolerance:
        c = (a+b)/2.0          
        if f(a)*f(c) < 0:
            b = c
        elif f(a)*f(c)>0:
            a = c
    return c

print(bissection_absolute_precision(-1, 0, f, 1e-8))
print(bissection_iterations(-1, 0, f, 6))
print(bissection_relative_precision(-1, 0, f, 1e-8))
print(bissection_function_annulment1(-1, 0, f, 1e-8))
print(bissection_function_annulment2(-1, 0, f, 1e-8))
