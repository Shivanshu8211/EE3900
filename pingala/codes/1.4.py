import numpy as np
import matplotlib.pyplot as plt

n = 100
alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2
k = np.linspace(1, n, n)
t = 10**k
a = (alpha**k - beta**k)/(alpha - beta)
b = a[2:] + a[:98]
b = np.pad(b, (1, 0), 'constant', constant_values=(1, 0))
tb = b*(1/t[:99])
eps = 1e-6
ans = 8/89
sb = np.cumsum(tb)
k1=np.linspace(1,99,99)
plt.stem(k1,sb,label='Simulation')
plt.axhline(y=8/89,color='r',label='Theoretical')
plt.legend()
plt.savefig('pingala/figs/1.4.eps')
plt.savefig('pingala/figs/1.4.pdf')
#plt.show()
if (abs(sb[-1] - ans) < eps): print("1.4 correct")
else: print("1.4 incorrect")