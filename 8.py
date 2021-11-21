#9
import numpy as np
import matplotlib.pyplot as plt
r = np.linspace(0., 5., 51)
theta = np.linspace(0.,2.*np.pi,101)
xmat, ymat, psi = np.zeros((r.size, theta.size)), np.zeros((r.size, theta.size)), np.zeros((r.size, theta.size)) 
for i in range(r.size):
    for j in range(theta.size):
        xmat[i, j] = r[i] * np.cos(theta[j])
        ymat[i, j] = r[i] * np.sin(theta[j])
        psi[i, j] = r[i] * np.exp(-r[i]) * (np.cos(theta[j]))**2
plt.contour(xmat, ymat, psi)
plt.show()
