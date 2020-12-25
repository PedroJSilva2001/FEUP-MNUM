# The Runge-Kutta 2 is a second order method to solve numerically ODEs.
# Since it is second order ε ~ 4 ε' ~ 16 ε'' so Qc = (S' - S)/(S''-S') ~ 4 and ε'' ~ (S''-S')/3 .
# It involves calculating dyn by using an estimate y'a = f(xn + dxn/2, yn + dxn/2 * y'n). dyn = y'a*dxn

def runge_kutta2(x0, y0, xf, n, f):
    h = (xf-xi)/n
    x = x0
    y = y0
    for i in range(n):
        dyn = h * f(x + h/2.0,  y + h/2.0 * f(x,y))
        y = y + dyn
        x = x + h
        print(i, x,y)
