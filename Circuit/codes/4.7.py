import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import subprocess
import shlex

def u(n):
    if n<0:
        return 0
    else :
        return 1

def y_cont(t):
    if t < 0: 
        return 0
    else:
        return 2/3 * (1 - np.exp(-1.5e6 * t))

def y_disc(n):
    if n < 0:
        return 0
    else:
        return 2/3 * (1 - (1 - 7.5e5 * 1e-7)**(n*1e7)/(1 + 7.5e5 * 1e-7)**(n*1e7))

def y(n):
    if n<0:
        return 0
    else:
        return (y(n-1)*(1-1 - 7.5e5 * 1e-7))/(1+1 - 7.5e5 * 1e-7)+(u(n)+u(n-1*0.5e6))/(1+1 - 7.5e5 * 1e-7)

yt = sp.vectorize(y_cont)
yn = sp.vectorize(y_disc)
ynn = sp.vectorize(y)


spice = np.loadtxt('4.7.dat')

T = np.linspace(0, 5e-6, 50)
plt.plot(T,yn(T),'*',label="y(n) recursion")
plt.plot(T, yt(T), label='$y(t)$')
plt.plot(spice[:,0], spice[:,1], 'o', label='ngspice')
plt.plot(T, yn(T), '.', label='y(n) inverse Z')
plt.grid()
plt.legend()
plt.savefig('../figs/4.7.png')
plt.show()
