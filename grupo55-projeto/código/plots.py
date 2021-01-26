from numpy import arange
from matplotlib.pyplot import plot, show, scatter, xlabel, ylabel, legend, ylim



def plot_Dt(D, tf):
    instants = arange(0, tf, 0.1)
    dosages = [D(t) for t in instants]
    xlabel("tempo t (h)")
    ylabel("Dosagem D(t) (mg/h)")
    plot(instants,dosages)
    show()

def plot_concentrations_continuous(points):
    t = points["x"]
    mi = points["y"]
    mp = points["z"]
    xlabel("tempo t (h)")
    ylabel("massa m (mg)")
    plot(t, mi, label = "mi")
    plot(t, mp, label= "mp")
    legend()
    show() 

def plot_concentrations_discrete(points):
    t = points["x"]
    mi = points["y"]
    mp = points["z"]
    xlabel("tempo t (h)")
    ylabel("massa m (mg)")
    scatter(t, mi, s=5, label = "mi", c = "r")    
    scatter(t, mp, s=5, label = "mp", c = "g")
    legend()
    show()

def plot_all(points):
    t = points["x"]
    mi = points["y"]
    mp = points["z"]
    xlabel("tempo t (h)")
    ylabel("massa m (mg)")
    plot(t, mi, label = "mi")
    plot(t, mp, label = "mp")
    scatter(t, mi, s=5, label = "mi", c = "r")    
    scatter(t, mp, s=5, label = "mp", c = "g")  
    legend()
    show()

def plot_qc(qc_values):
    ylim(-20, 20)
    iter = [i for i in range(len(qc_values))]
    plot(iter, qc_values)
    scatter(iter, qc_values, s=5, c = "r")    
    ylabel("Qc")
    legend()
    show()
