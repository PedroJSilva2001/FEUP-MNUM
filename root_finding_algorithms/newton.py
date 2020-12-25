# Newton's method is used to find the root of a real-valued function using a recurrence formula and an initial guess for the root
# The recurrence formula is xn+1 = xn - f(xn)/f'(xn)
# Newton's method may not converge to a definite value as it is prone to oscillate in sequence, for example, in functions in which the root is an 
# inflection point i.e x^3 - 5x
# Stationary points (where the derivative is zero) will lead to division by zero
# A large error in the initial estimate can contribute to non-convergence of the algorithm
# If the initial value of x is guessed poorly, another root, not the wanted one, may be obtained. So, if the root we want is on the other side of 
# the stationary point we must choose a point in which the derivative follows the gradient of the function i.e f(x)= x^2 - 2: if we do newton(x0 = -1,f) 
# we won't be getting the root x = sqrt(2) but instead x = -sqrt(2)
# It will also diverge if the derivative does not exist at the root i.e f(x) = |x|^a, 0 < a < 1/2 where it will overshoot the solution and lands on 
# the other side of the y-axis, farther than it initially was. In the limiting case a =1/2 so the iterations will alternate indefinetely between points x0 and -x0
# If the derivative is not continuous at the root, then the method will also diverge 
# This method is generally of faster convergence than bissection or regula falsi
# This method each iteration has the potencial to double the number of accurate decimal places


import math

def f(x):
    return math.sin(x) +x**5-0.2*x+1

def fder(x):
    return math.cos(x) + 5*x**4 -0.2

def g(x):
    return x**2-2

def gder(x):
    return 2*x

def h(x):
    return x**3-5*x

def hder(x):
    return 3*x**2 -5

def i(x):
    return x**(1/3)

def ider(x):
    return 1/3*x**(1/3-1)

def j(x):
    return x**(1/2)

def jder(x):
    return 1/2*x**(1/2-1)

def k(x):
    if x == 0:
        return 0
    return x+x**2*math.sin(2/x)
    
def kder(x):
    if x == 0:
        return 1
    return 1+2*x*math.sin(2/x)-2*x*math.cos(2/x)


def a(x):
    return 1- 3/(x**3)
def ader(x):
    return 3*3*x**(-3-1)

def newton1(x0, f, fder, tolerance):
    print("0", " | x0 =", x0, " | f(x0) =", f(x0))
    x = x0
    count = 0
    while abs(f(x)) > tolerance:
        x = x0 - f(x0)/fder(x0)
        x0 = x
        count +=1
        print(count, " | x"+ str(count) + " =", x, " | f(x" +  str(count) + ") =", f(x))
    return x 

def newton2(x0, f, fder, iterations):
    print("0", " | x0 =", x0, " | f(x0) =", f(x0))
    x = x0
    count = 0
    for i in range(iterations):
        x = x0 - f(x0)/fder(x0)
        x0 = x
        count +=1
        print(count, " | x"+ str(count) + " =", x, " | f(x" +str(count) + ") =", f(x))
    print()
    return x 

# converges
newton1(-1, f, fder, 1e-8)
print()
newton2(1, a, ader,5 )
input()

# converges to the negative root
# if we want the positive root we must choose not choose a negative guess
newton2(-4, g, gder, 6)

# division by zero will occur since x0 = 0 is a stationary point
newton1(0, g, gder , 1e-8)

# will oscillate around the root x0 = 0 because it is an inflection point
newton1(1, h, hder, 1e-8)

# will diverge twice as fast each iteration
newton1(1, i, ider, 1e-8)

# will oscillate between -x0 and x0
newton1(1, j, jder, 1e-8)

# will diverge almost everywhere in the neighbourhood of the root
newton1(1, k, kder, 1e-8)