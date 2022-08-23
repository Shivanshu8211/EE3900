import numpy as np
import matplotlib.pyplot as plt

def H(z):
	num = np.polyval([1,0,1],z**(-1))
	den = np.polyval([0.5,1],z**(-1))
	H = num/den
	return H
		

omega = np.linspace(int(-3*np.pi),int(3*np.pi),int(1e2))

plt.plot(omega, abs(H(np.exp(1j*omega))))
plt.title('Filter Frequency Response')
plt.xlabel('$\omega$')
plt.ylabel('$|H(e^{\jmath\omega})| $')
plt.grid()

plt.savefig('../figs/dtft.pdf')
plt.savefig('../figs/dtft.eps')
plt.show()





