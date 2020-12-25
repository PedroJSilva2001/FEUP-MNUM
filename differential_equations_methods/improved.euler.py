# An improvement can be done to this method by using Lagrange's theorem: deltay = f'avg * deltax and the use of the previous point
# (xn-1, yn-1). We can calculate the next point pn+1 by pn+1 = yn-1 + 2*y'n * dxn and then the derivative at that point is p'n+1 = f(xn+1, pn+1)
# so the increment in y will be dxn = p'n+1 + y'n /2 * dxn and then we apply the same reccurence formula. 
# The improved version requires two points to start the method by using the normal method or by using Taylor series expansion more precise.
# The Euler method now becomes third order (ε = 5/12 *h^3 * y'''(ξ) if y''' preserves its sign inside the step) so ε = 8 ε' = 64 ε'', 
# Qc = (S' - S)/(S''-S') ~ 8 and ε'' ~ (S''-S')/7



# improved version of Euler method
def improved_euler(x0,y0,x1,y1, xf, n, f):
    xprev = x0
    yprev = y0
    x = x1
    y = y1
    h = (xf-x0)/n
    
    for i in range(n):
        ydern = f(x,y)
        p = yprev + 2*ydern*h
        pder = f(x+h, p)
        dyn = (pder + ydern)/2.0 * h 
        xprev = x
        yprev = y
        y = y + dyn
        x = x + h
        print(i, x, y, (x**2)/2.0)


improved_euler(0,0,0.5, 0, 5,10, lambda x, y: x)
