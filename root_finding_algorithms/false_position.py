# False Position is a bracketing method (like the bissection method) used to find the root of a real-valued function.
# It also applies Bolzano's theorem but unlike the bissection method its formula to approximate the root c is c = (a*f(b) - b*f(a))/(f(b)-f(a))
# and the idea behin the method is while reducing the interval if an extreme value is big in absolute value while the other is small, then the root.
# is probably found near the point with the small value of the function.
# Another key difference between the both of them is that in false position either (a, f(a)) or (b, f(b)) remains static, while the other converges
# torwards the root.
# Unlike the bissection method, we can't know a priori the stopping criteria so we need to check each iteration if the termination condition is reached which
# takes a while if the values of the function at the extremes are expedit.
# The point that remains fix in place is the extreme where the sign of the function coincides with the sign of its second derivative and the successive 
# approximations are found, in relation to the root, on the side where the function has opposite sign of its second derivative
# It generally converges faster than bissection method because it uses the values f(a) and f(b) in its root approximation but its downside is that the moment
# one of the points on the extremes remains static, convergence becomes slower simply by the fact that the string becomes more and more vertical. Because of that
# we can optimize the method if each iteration we reduce by half the value of the function that we preserve.



import math
import pandas as pnd


def f(x):
    return math.sin(x) +x**5-0.2*x+1

def g(x):
    return x**2-2

def h(x):
    return x**3-5*x

def false_position_function_annulment2(a, b, f, tolerance):
    c = (a*f(b) - b*f(a))/(f(b)-f(a)) 
    cols = {"a":[a], "b":[b], "c":[c], "f(a)":[f(a)], "f(b)":[f(b)], "f(c)":[f(c)]}

    while abs(f(c)) > tolerance:
        if f(a)*f(c) < 0:
            b = c
        elif f(a)*f(c)>0:
            a = c
        c = (a*f(b) - b*f(a))/(f(b)-f(a)) 
        cols["a"].append(a)
        cols["b"].append(b)
        cols["c"].append(c)
        cols["f(a)"].append(f(a))
        cols["f(b)"].append(f(b))
        cols["f(c)"].append(f(c))

    data = pnd.DataFrame(cols, columns=["a", "b", "c" ,"f(a)", "f(b)", "f(c)"])
    print("\n",data) 
    return c 

def false_position_iterations(a, b, f, iterations):
    c = 0
    for i in range(iterations):
        c = (a*f(b) - b*f(a))/(f(b)-f(a)) 
        if f(a)*f(c) < 0:
            b = c
        elif f(a)*f(c)>0:
            a = c
    return c 

def false_position_absolute_precision(a, b, f, tolerance):
    c = (a*f(b) - b*f(a))/(f(b)-f(a))
    c_prev = a 
    while abs(c-c_prev) > tolerance:
        if f(a)*f(c) < 0:
            b = c
        elif f(a)*f(c)>0:
            a = c
        c_prev = c
        c = (a*f(b) - b*f(a))/(f(b)-f(a)) 
    return c 

def false_position_relative_precision(a,b,f,tolerance):
    c = (a*f(b) - b*f(a))/(f(b)-f(a))
    c_prev = a 
    while abs((c-c_prev)/c) > tolerance:
        if f(a)*f(c) < 0:
            b = c
        elif f(a)*f(c)>0:
            a = c
        c_prev = c
        c = (a*f(b) - b*f(a))/(f(b)-f(a)) 
    return c 

def false_position_function_annulment1(a,b,f,tolerance):
    c = (a*f(b) - b*f(a))/(f(b)-f(a))
    c_prev = a
    while abs(f(c)-f(c_prev)) > tolerance:
        if f(a)*f(c) < 0:
            b = c
        elif f(a)*f(c)>0:
            a = c
        c_prev = c
        c = (a*f(b) - b*f(a))/(f(b)-f(a)) 
    return c 
       
print(false_position_function_annulment2(-1, 0, f, 1e-8))
print(false_position_iterations(-1, 0, f, 12))
print(false_position_absolute_precision(-1, 0, f, 1e-8))
print(false_position_relative_precision(-1, 0, f, 1e-8))
print(false_position_function_annulment1(-1, 0, f, 1e-8))

