#import pandas as pnd
from pandas import DataFrame
def runge_kutta2_higher_order(x0, y0, z0, xf, n, f, g):
    sister_cols = []
    data = []
    for j in range(3):
        h = (xf - x0)/n
        x = x0
        y = y0
        z = z0
        cols = {"x":[x0], "y":[y0],  "z":[z0]}
        for i in range(n):
            d1 = h * f(x, y, z)
            l1 = h * g(x, y, z)
            y_copy = y
            y = y + h * f(x + h/2.0, y + d1/2.0, z + l1/2.0)
            z = z + h * g(x + h/2.0, y_copy + d1/2.0, z + l1/2.0)
            x = x + h
            cols["x"].append(x)
            cols["y"].append(y)
            cols["z"].append(z)
        sister_cols.append(cols)
        data.append(DataFrame(cols, columns=["x", "y", "z"]))
        n = n*2
    #print("\n",data)
    return sister_cols, data

def runge_kutta4_higher_order(x0, y0, z0, xf,  n, f, g):
    sister_cols = []
    data = []
    for j in range(3):
        h = (xf - x0)/n
        x = x0
        y = y0
        z = z0
        cols = {"x":[x0], "y":[y0],  "z":[z0]}
        for i in range(n):
            d1 = h * f(x, y, z)
            l1 = h * g(x, y, z)

            d2 = h * f(x + h/2.0, y + d1/2.0, z + l1/2.0)
            l2 = h * g(x + h/2.0, y + d1/2.0, z + l1/2.0)


            d3 = h * f(x + h/2.0, y + d2/2.0, z + l2/2.0)
            l3 = h * g(x + h/2.0, y + d2/2.0, z + l2/2.0)

            d4 = h * f(x + h, y + d3, z + l3)
            l4 = h * g(x + h, y + d3, z + l3)

            y = y + d1/6.0 + d2/3.0 + d3/3.0 + d4/6.0
            z = z + l1/6.0 + l2/3.0 + l3/3.0 + l4/6.0
            x = x + h
            cols["x"].append(x)
            cols["y"].append(y)
            cols["z"].append(z)
        sister_cols.append(cols)
        data.append(DataFrame(cols, columns=["x", "y", "z"]))
        n = n*2
    #print("\n",data)
    return sister_cols, data

def euler_higher_order(x0, y0, z0, xf, n, f, g):
    sister_cols = []
    data = []
    for j in range(3):
        h = (xf-x0)/n
        x = x0
        y = y0
        z = z0
        cols = {"x":[x0], "y":[y0],  "z":[z0]}
        for i in range(n):
            y_copy = y
            y = y + h * f(x, y, z0)
            z = z + h * g(x, y_copy, z)
            x = x + h
            cols["x"].append(x)
            cols["y"].append(y)
            cols["z"].append(z)
        n = n*2
        sister_cols.append(cols)
        data.append(DataFrame(cols, columns=["x", "y", "z"]))
    #print("\n",data)
    return sister_cols, data


def modified_euler_higher_order(x0, y0, z0, x1, y1, z1, xf, n, f, g):
    sister_cols = []
    data = []
    for j in range(3):
        h = (xf-x0)/n
        if j == 0:
            x = x1
            y = y1
            z = z1
        else:
            x = x1 /(2*j)
            y = 0
            z = 0
        y = y1
        z = z1
        xprev = x0
        yprev = y0
        zprev = z0
        cols = {"x":[x0, x1], "y":[y0,y1],  "z":[z0, z1]}
        for i in range(n-1):
            ydern = f(x,y,z)
            zdern = g(x,y,z)

            py = yprev + 2*ydern*h
            pz = zprev + 2*zdern*h

            pyder = f(x + h, py, pz)
            pzder = g(x + h, py, pz)

            xprev = x
            yprev = y
            zprev = z

            y = y + h* (pyder + ydern)/2.0
            z = z + h* (pzder + zdern)/2.0
            x = x + h
            cols["x"].append(x)
            cols["y"].append(y)
            cols["z"].append(z)
        sister_cols.append(cols)
        data.append(DataFrame(cols, columns=["x", "y", "z"]))
        n = n*2
    #print("\n",data)
    return sister_cols, data
