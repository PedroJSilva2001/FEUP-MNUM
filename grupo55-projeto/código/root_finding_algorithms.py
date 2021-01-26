from pandas import DataFrame
import math

def bissection(a, b, f, tolerance):
    c = 0
    n = 0
    cols = {"a":[], "b":[], "c":[], "f(a)":[], "f(b)":[], "f(c)":[], "|b-a|":[]}    
    while abs(f(c)) > tolerance:
        n+=1
        c = (a + b)/2.0
        fa = f(a)
        fc = f(c)
        cols["a"].append(a)
        cols["b"].append(b)
        cols["c"].append(c)
        cols["f(a)"].append(fa)
        cols["f(b)"].append(f(b))
        cols["f(c)"].append(fc)
        cols["|b-a|"].append(abs(b-a))
        if abs(fc) <= tolerance:
            break
        if fa*fc < 0:
            b = c
        elif fa*fc > 0:
            a = c        
    data = DataFrame(cols, columns=["a", "b", "c" ,"f(a)", "f(b)", "f(c)", "|b-a|"])
    #print("\n",data)
    return c, data, n

def false_position(a, b, f, tolerance):
    c = 0
    n = 0
    cols = {"a":[], "b":[], "c":[], "f(a)":[], "f(b)":[], "f(c)":[]}    

    while True:
        n += 1
        c = (a*f(b) - b*f(a))/(f(b)-f(a))
        fc = f(c)
        fa = f(a)
        cols["a"].append(a)
        cols["b"].append(b)
        cols["c"].append(c)
        cols["f(a)"].append(fa)
        cols["f(b)"].append(f(b))
        cols["f(c)"].append(fc)
        if abs(fc) <= tolerance:
            break
        if fa*fc < 0:
            b = c
        elif fa*fc > 0:
            a = c

    data = DataFrame(cols, columns=["a", "b", "c" ,"f(a)", "f(b)", "f(c)"])
    #print("\n",data) 
    return c, data, n

def newton(x0, f, fder,  tolerance):
    n = 0
    cols = {"x":[x0], "f(x)":[f(x0)]}  
    while True:
        n += 1
        x0 = x0 - f(x0)/fder(x0)
        fx0 = f(x0)
        cols["x"].append(x0)
        cols["f(x)"].append(fx0) 
        if abs(fx0) <= tolerance:
            break
    data = DataFrame(cols, columns=["x", "f(x)"])
    #print("\n",data) 
    return x0, data, n

def modified_false_position(a, b, f, tolerance):
    c = 0
    n = 0
    fc = 0
    side = 0
    cols = {"a":[], "b":[], "c":[], "f(a)":[], "f(b)":[], "f(c)":[]}    
    fa = f(a)
    fb = f(b)
    while True:
        n +=1
        c = (a*fb - b*fa)/(fb-fa)
        fc = f(c)
        cols["a"].append(a)
        cols["b"].append(b)
        cols["c"].append(c)
        cols["f(a)"].append(fa)
        cols["f(b)"].append(fb)
        cols["f(c)"].append(fc)
        if abs(fc) <= tolerance:
            break
        if fa*fc < 0:
            b = c
            fb = fc
            if side == -1:
                fa /=2
            side = -1
              
        elif fa*fc>0:
            a = c
            fa = fc
            if side == 1:
                fb /= 2
            side = 1

    data = DataFrame(cols, columns=["a", "b", "c" ,"f(a)", "f(b)", "f(c)"])
    #print("\n",data) 
    return c, data, n

def picard_peano(x0, f, g, tolerance):
    n = 0
    cols = {"x":[x0], "f(x)":[f(x0)]}
    while True:
        n +=1
        x0 = g(x0)
        fx0 = f(x0)
        cols["x"].append(x0)
        cols["f(x)"].append(fx0)        
        if abs(fx0) <= tolerance:
            break
    data = DataFrame(cols, columns=["x", "f(x)"])
    #print("\n",data)
    return x0, data, n
