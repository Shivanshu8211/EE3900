import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
A=12
f=50
l = np.linspace(-50,50,1000)
def y(t):
    return A*abs(math.sin(2*3.14*f*t))
y_t = scipy.vectorize(y)
plt.plot(l,y_t(l),'k',label = "graph of x(t)")
plt.xlabel("$t-->$")
plt.ylabel("$x(t)-->$")
plt.grid()
plt.savefig("../figs/1.1.png")
plt.show()