

import numpy as np
import scipy
import matplotlib.pyplot as plt
def h(n):
    if n ==0:
        return 1.0
    elif n == 1:
        return -h(0)/2.0
    elif n == 2:
        return -h(0)/2.0 + 1
    else :
        return -h(n-1)/2.0
vec_hn = scipy.vectorize(h)
n = np.arange(12)
plt.stem(n,vec_hn(n))
plt.xlabel("$n$")
plt.ylabel("$h(n)$")
plt.title("Impulse Reponse Definition")
plt.grid()
plt.savefig("../figs/hndef.png")
plt.show()
