import numpy as np
import matplotlib.pyplot as plt

y = np.loadtxt("./home/shivanshu/Programs/Digital signal processing/Codes/xnyn.dat",dtype = "double")
x = np.array([1,2,3,4,2,1])


plt.subplot(211)
plt.stem(np.arange(len(x)),x)
plt.xlabel("n")
plt.ylabel("$x(n)$")
plt.grid()

plt.subplot(212)
plt.stem(np.arange(len(y)),y)
plt.xlabel("n")
plt.ylabel("$y(n)$")
plt.grid()

plt.savefig("Assignment 1/Figs/xnyn2.png")
plt.show()