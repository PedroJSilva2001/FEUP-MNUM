# Newton's method can also be used to approximate a solution of a system of multiple equations by using calculus.
# If we have the system f1(x,y) = 0  &&  f2(x,y) = 0 we can write it in the following way: x = xn + hn  &&  y = yn + kn
# and then we obtain f1(xn+hn, yn+kn) = 0 && f2(xn+hn, yn+kn) = 0. If the jacobian J(xn. yn) is not zero, we can write that
# hn = -(f1 * f2'y - f2 * f1'y )/ J  && kn = -(f1'x * f2 - f2'x * f1)/ J. So the recurrence formulas are 
# xn+1 = xn - (f1 * f2'y - f2 * f1'y )/(f1'x * f2'y - f2'x * f1'y) &&
# yn+1 = yn - (f1'x * f2 - f2'x * f1)/(f1'x * f2'y - f2'x * f1'y) 


def f1(x,y): return x-y**2
def f2(x,y): return y-x**2

def f1derx(x,y):
    return 1
def f1dery(x,y):
    return -2*y

def f2derx(x,y):
    return -2*x

def f2dery(x,y):
    return 1

def J(x,y):
    return f1derx(x,y) * f2dery(x,y) - f2derx(x,y) * f1dery(x,y)

def hn(x,y):
    return -(f1(x,y) * f2dery(x,y) - f2(x,y) * f1dery(x,y) )/ J(x,y)
def kn(x,y):
    return -(f1derx(x,y) * f2(x,y) - f2derx(x,y) * f1(x,y) )/J(x,y)
def newton_function_annulment(x0, y0, f1, f2, tolerance):
    x = x0
    y = y0 
    while abs(f1(x,y)) > tolerance:
        x = x0 + hn(x0,y0)
        y = y0 + kn(x0, y0)
        x0 = x
        y0 = y
    return (x, y)
print(newton_function_annulment(2, 2, f1, f2, 1e-8))