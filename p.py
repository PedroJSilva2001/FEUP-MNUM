def aurea_min(x1, x2, f, tolerance):
    B = (5**0.5 - 1.0)/2.0  #golden ratio
    A = B**2
    x3 = x1 + A * (x2-x1)
    x4 = x1 + B * (x2-x1)
    while abs(x1 - x2) > tolerance:
        if f(x3) < f(x4):
            x2 = x4
            x4 = x3
            x3 = x1 + A*(x2-x1)
        else:
            x1 = x3
            x3 = x4
            x4 = x1 + B*(x2-x1)
    return [x1,x2,x3, x4] 
