# The Euler method is used to approximate the solution y(x) of an ordinary differential equation of first order: 
#  y' = dy/dx = f(x,y).
# It involves the increment of y by using y'n which is the slope of the curve at the point (xn, yn) and dxn, the 
# increment in x: dyn = y'n * dxn = f(xn, yn)*dxn. So we can obtain the next point by the recurrence formulas: 
# yn+1 = yn + dyn && xn+1 = xn + dxn
# Since it is a first order method ε ~ 2 ε' ~ 4 ε'' so Qc = (S' - S)/(S''-S') ~ 2 and ε'' ~ S''-S'
# The method can have truncature issues and doesn't have high precision since it is of first order and because of the acumulation of 
# delays in intervals where the sign of the curvature is the same. This happens because at each step we use the a derivative value that
# is only valid for its initial extreme since dxn is not really an infinitesimal

 
def euler(x0, y0, xf, n, f):
    x = x0
    y = y0
    h = (xf-x0)/n
    
    for i in range(n):

        y = y + h * f(x, y)
        x = x + h
        print(i, x, y, (x**2)/2.0)


euler(0,0, 5,10, lambda x, y: x)