# The trapezoid rule is a 2º order method used to approximate a definite integral of a function f in an interval [a,b] numerically.
# Since a definite integral is the area under the graph between two values of x, we can approximate it by "filling" that region with 
# trapezoids, of which we can easily know the area. The more partitions we create for the area, the better the approximation.
# Let I be the integral, then I = S + ε, in which S is the estimate and ε is the error.
# The formula for S is S = h/2 * [y0 + 2*y1 + ... + 2*yn-1 + yn] = h/2 * [y0 + yn + 2*sum{i=1->N-1}(yi)] = 
# sum{i = 1-> N}( (f(x_i-1) + f(x_i))/2 * h) where h is the base of the trapezoids or the value for the step of x
# If we want to approximate well the area we must not choose the value of step but rather the number of steps or trapezoids we want to use. So 
# if n is the number of steps then h, the value of each step of x, is h = |b-a|/n. If we had chosen an h arbitraly and then calculated
# n accordingly, what would've happened is that if xn-1 + h > b (xn > b) and we would be incrementing by excess a trapezoid of area
# (xn-b) * (f(b) + f(xn))/2; if xn-1 + h < b (xn < b) we would be incrementing by defect a trapezoid of area (b-xn) * (f(xn)+ f(b))/2
# This is a second order method because for a given amplitude of the interval, the error is proportional to the inverse square of the 
# number of intervals or the step of integration.
# For a given number of steps of integration and under the assumption that the upper bound of the second derivative is fix, the error is 
# proportional to the cube of the amplitude of the interval.
# The formula for the error ε is ε = -(xn -x0)^3 / 12n^2 * f''(ξ)
# The formula for the error is not always valid and we might not even be able to find an upper bound for it so we need to find ways to 
# evaluate or keep it under check. To do this we can approximate the integral two times, one with a step value of h, and the other with a
# step value of h' = h/2. If the results don't differ significately (must be values far from the precision of the computer), then it is applicable.
# But this method isn't good because the error also depends on ξ which is uncontrollable and the formula is only valid for small values of h.
# If we approximate the integral three times: S, S', S'' with corresponding step values h, h' = h/2, h'' = h/4 we can say that I = S + ε = 
# S' + ε' = S'' + ε'' in which, basing it on the error formula, ε ~ 4 ε' ~ 16 ε'' so Qc = (S' - S)/(S''-S') ~ 4. If this ratio is aproximately 4, it
# means that the steps of integration are within the domain of validity for the error formula by Lagrange's remainder and that S''-S' can be used as 
# an estimate of ε'' and estimate if S'' is withing the desired precision : ε'' ~ (S''-S')/3 
# For a growing n, Qc is decreasing close to the theoretical value, in effect of the decreasing of the error of truncature. However it then increases 
# because of rounding errors. If this first decrease torwards the theoretical value doesn't happen, the method is not applicable with the computer we are using. 
# A defect of this method is that it produces a systematic error in intervals where the function has the same concavity.

def trapezoid_rule1(a, b, n, f):
    integral = 0
    h = float((b - a) / n)
    x = a
    for i in range(n):
        integral += (f(x) + f(x + h))/2.0 * h
        x = x + h
    return integral  

def trapezoid_rule2(a, b, n, f):
    integral = 0
    h = float((b - a) / n)
    x = a
    for i in range(n):
        integral += (f(x) + f(x + h))
        x = x + h
    return integral* h/2.0  

# best way - requires fewer evaluations of the function to calculate
def trapezoid_rule_optimized(a, b, n, f):
    h = float((b - a) / n)   
    integral = (f(a) + f(b))/2.0
    x = a
    for i in range(1, n):
        integral += f(a+i*h) 
    return integral*h

def trapezoid_rule_optimized2(a, b, n, f):
    h = float((b - a) / n)
    integral = (f(a) + f(b))/2.0
    x = a+h

    for i in range(n-1):
        integral += f(x) 
        x = x + h
    return integral*h
    
def trapezoid_rule3(a,b,n, f):
    h = float((b-a)/n)
    integral = f(a)+f(b)
    for i in range(1,n):
        integral += 2.0*f(a+i*h)
    return integral* h/2.0

print(trapezoid_rule1(0, 10, 10000, lambda x : x**4.0))
print(trapezoid_rule2(0, 10, 10000, lambda x : x**4.0))  
print(trapezoid_rule_optimized(0, 10, 10000, lambda x : x**4.0))
print(trapezoid_rule_optimized2(0, 10, 10000, lambda x : x**4.0))
print(trapezoid_rule3(0, 10, 10000, lambda x : x**4.0)) 