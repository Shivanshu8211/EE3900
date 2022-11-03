import numpy as np
import matplotlib.pyplot as plt

def H(s):
    return 5e5/(s+1.5e6)

S= np.linspace(-3e6,3e6,50)

plt.plot(S,H(S))
plt.grid()
plt.savefig("../figs/Hs.png")
plt.show()
