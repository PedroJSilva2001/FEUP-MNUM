# To find the minima or maxima of a real valued function we can portion the function in regions where its concavity 
# is the same so that is is guaranteed that only one minimum or maximum resides in that region. If this region is [a,b] 
# we can choose an x0, a <= x0 <= b and give it a step h and evaluate if f(x + h) is moving torwards or away of the local
# extreme 


def find_minimum(x0, f, h):
    if f(x0) < f(x0 + h):
        h = -h 
    while f(x0) > f(x0+h):
        x0 +=h
    return [x0 - abs(h), x0,x0 + abs(h)]    
find_minimum(3, lambda x:x**2, 0.05)

def find_maximum(x0, f, h):
    if f(x0) > f(x0 + h):
        h = -h 
    while f(x0) < f(x0+h):
        x0 +=h
    return [x0 - abs(h), x0,x0 + abs(h)]    

print(find_maximum(3, lambda x: -x**2, 0.05))