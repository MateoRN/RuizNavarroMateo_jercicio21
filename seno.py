import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,4*np.pi,50)
y = np.cos(x)

plt.figure()
plt.plot(x,y)
plt.savefig("coseno.png")