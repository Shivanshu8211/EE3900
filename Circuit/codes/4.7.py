import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,1e-5,300)
y=5*(2/3)*(1-np.exp((-3/2)*1e6*x))
plt.plot(x,y)
plt.grid()
ax=plt.gca()
ax.set_xlabel('t')
ax.set_ylabel('$y(t)$')
# plt.savefig('Circuits/figs/2.7.eps')
# plt.savefig('Circuits/figs/2.7.pdf')
plt.show()