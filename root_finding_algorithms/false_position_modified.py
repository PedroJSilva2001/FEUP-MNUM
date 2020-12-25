# Modification of false position explained in false position file

import pandas as pnd

def modified_false_position_function_annulment(a, b, f, tolerance):
    c = 0
    fc = 0
    side = 0
    cols = {"a":[], "b":[], "c":[], "f(a)":[], "f(b)":[], "f(c)":[]}    
    fa = f(a)
    fb = f(b)
    while True:
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

    data = pnd.DataFrame(cols, columns=["a", "b", "c" ,"f(a)", "f(b)", "f(c)"])
    print("\n",data) 
    return c 
