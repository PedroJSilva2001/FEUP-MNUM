import math as m

# Ex 1
def f(x):
    return m.sin(x)+x**5-0.2*x+1

def bissection(a,b, f, n):
    for i in range(n):
        c = (a+b)/2.0
        print(a,b)

        if f(a)*f(c) < 0:
            b = c
        elif f(a)*f(c) > 0:
            a = c
        print(i, c)
    return c
root = bissection(-1, 0, f, 6)
# b-a/2^n = epsilon
#absolute_error = (0-(-1))/2**6
a = -0.84375
b = -0.8125
absolute_error = abs(root - a)
print("absolute error:",absolute_error)
print("relative error:" ,absolute_error/abs(root) , "\n") 
print() 


# Ex 2

def f1(x,y): return x**2-y-1.2
def f2(x,y): return -x +y**2 -1.0 

def f1derx(x,y): return 2.0*x
def f1dery(x,y): return -1.0

def f2derx(x,y): return -1.0
def f2dery(x,y): return 2.0*y

def J(x,y): return f1derx(x,y)*f2dery(x,y)-f2derx(x,y)*f1dery(x,y)

def hn(x,y): return - (f1(x,y)*f2dery(x,y) - f2(x,y)*f1dery(x,y))/J(x,y)

def kn(x,y): return - (f1derx(x,y)*f2(x,y) - f2derx(x,y)*f1(x,y))/J(x,y) 

def newton(x0, y0, f1,f2,n ):
    x = x0
    y= y0
    for i in range(n):
        x_copy = x
        x = x + hn(x,y)
        y = y + kn(x_copy, y)
        print(i, x, y)
        
newton(1.00000, 1.00000, f1,f2, 2) 
print()



# Ex 3
h = 0.25
h1=0.125
h2 = 0.0625
a = 0
b = 2
k = 1.5

def F(x): return (1+ (k*m.exp(k*x))**2)
def trapezoid(a,b,h, f):
    arc = (f(a)+f(b))/2.0
    n = round((b-a)/h)       
    for i in range(1,n ):
        arc += f(a+i*h)
    return arc*h
        


def simpson(a,b,h,f):
    arc = f(a)+f(b)
    n = round((b-a)/h)
    
    for i in range(1,n, 2):
        arc += 4*f(a+i*h)
        if i != n-1:
            arc += 2*f(a+(i+1)*h)
    return arc*h/3.0

L_trap = trapezoid(a,b,h,F)
L_simp = simpson(a,b,h,F)
print("trap h :", L_trap)        
print("simp h :", L_simp)        

L1_trap = trapezoid(a,b,h1,f)
L1_simp = simpson(a,b,h1,f)
print("trap h' :",L1_trap)        
print("simp h' :", L1_simp)   
     
L2_trap = trapezoid(a,b,h2,f)
L2_simp = simpson(a,b,h2,f)
  
print("trap h'' :",L2_trap)        
print("simp h'' :", L2_simp)       
        
print("Qc trap =", (L1_trap - L_trap)/(L2_trap - L1_trap) )  
print("Qc simp =", (L1_simp - L_simp)/(L2_simp - L1_simp) ) 
print("e'' trap =", (L2_trap - L1_trap)/3.0) 
print("e'' simp =", (L2_simp - L1_simp)/15.0)
print()


# Ex 4

Ta = 59
def g(t, T): return -0.25*(T-Ta)

def euler(t0, T0, g):
    for i in range(2):
        T0 += g(t0, T0)*0.5
        t0 += 0.5
        print(i, t0, T0)

print(euler(2, 2, g))
print()
        
# Ex 5

def y(x): return -5.0*m.cos(x)+m.sin(x)+10.0

def aurea(x1, x2, x3, x4):
    b = (5**0.5 - 1)/2
    a = b**2
    for i in range(3):
        if y(x4) < y(x3):
            x1 = x3
            x3 = x1 + a*(x2-x1)
        else:
            x2 = x4
            x4 = x1 + b*(x2-x1)
        print(x1, x2, x3, x4, y(x1), y(x2), y(x3), y(x4))
aurea(2,4, 2.76393, 3.23606)
print()


# Ex 6

def z(x,y): return 3.0*x**2.0 - x*y +11.0*y + y**2.0 -8.0*x

def zderx(x,y): return 6.0*x -y -8.0

def zdery(x,y): return 2.0*y-x+11

print("Z(X0) =",z(2,2))
print("Gradient x =", zderx(2,2), "Gradient y=", zdery(2,2))
def gradient(x,y,lambdaa):
    for i in range(40):
        print(i, x, y)
        newx = x - lambdaa*zderx(x,y)
        newy = y - lambdaa*zdery(x,y)
        if abs(newx-x) <=0.001 and abs(newy-y) <=0.001:
            print( "precision", i, abs(newx-x), abs(newy-y))
            break
        print( "precision", i, abs(newx-x), abs(newy-y))
        if(z(newx, newy) < z(x,y)):
            lambdaa = lambdaa*2
            x = newx
            y = newy
        else:
            lambdaa = lambdaa/2.0

print("lambda = 1:")
gradient(2,2,1)
print("\nlambda = 0.5")
gradient(2,2,0.5)
print("\nlambda = 0.25")
gradient(2,2, 0.5)

print("Z(X1) =",z(1.0,-4.5))
print("Gradient x =", zderx(1.0,-4.5), "Gradient y=", zdery(1.0,-4.5))
# melhor lambda é 0.5 porque é o que tem os valores mais precisos
