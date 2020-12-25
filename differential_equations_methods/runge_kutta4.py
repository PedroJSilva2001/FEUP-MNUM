# The Runge-Kutta 2 is a second order method to solve numerically ODEs.
# Since it is second order ε ~ 16 ε' ~ 256 ε'' so Qc = (S' - S)/(S''-S') ~ 16 and ε'' ~ (S''-S')/15 .
# It involves calculating dyn by using 4 estimates

def runge_kutta4(x0, y0, xf, n, f):
    h = (xf-xi)/n
    x = x0
    y = y0
    for i in range(n):
        d1 = h * f(x,y)
        d2 = h * f(x + h/2.0 , y + d1/2.0)
        d3 = h * f(x + h/2.0, y + d2/2.0)
        d4 = h * f(x + h, y + d3)
        dyn = d1/6.0 + d3/3.0 + d3/3.0 + d4/6.0
        y = y + dyn
        x = x + h
        print(i, x,y)
