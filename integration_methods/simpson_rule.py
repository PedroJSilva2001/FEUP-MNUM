# The Simpson rule is a 4º order method used to approximate a definite integral of a function f in an interval [a,b] numerically.
# Unlike what happened with the trapezoidal rule where we had substituted the arc of the curve in two consecutive points 
# for its secant, in this rule we substitute it for the parabola defined by a trio of consecutive points. 
# The formula for S is S = h/3 * [y0 + 4*y1 + 2*y2 ... + 2*y2n-2 +4*y2n-1 + y2n] = h/3 * [y0 + y2n + 4*sum{i=1->2n-1, i+=2}(yi) + 2*sum{i=2->2n-2, i+=2}(yi)] 
# This is a fourth order method because for a given amplitude of the interval, the error is proportional to the inverse fourth power of the 
# number of intervals or the step of integration.
# For a given number of steps of integration and under the assumption that the upper bound of the fourth derivative is fix, the error is 
# proportional to the fifth power of the amplitude of the interval.
# The formula for the error ε is ε = -(xn -x0)^5 / 90n^4 * f''''(ξ)
# Basing it on the error formula, ε ~ 16 ε' ~ 256 ε'' so Qc = (S' - S)/(S''-S') ~ 16. If this ratio is aproximately 16, it
# means that the steps of integration are within the domain of validity for the error formula by Lagrange's remainder and that S''-S' can be used as 
# an estimate of ε'' and estimate if S'' is withing the desired precision : ε'' ~ (S''-S')/15 



def simpson_rule(a, b, n, f):
    h = float((b-a)/n)
    integral = f(a) + f(b)
    for i in range(1, n, 2):
        integral += 4*f(a+i*h)
        if i != n-1:
            integral += + 2*f(a+(i+1)*h)
    #for i in range(2,n,2):
    #    integral += 2*f(a+i*h)
    return integral * h/3


print(simpson_rule(0, 10, 1000, lambda x: x**4))


