import numpy as np
import matplotlib.pyplot as plt

K = 1
τ = 1
t = np.linspace(0, 5, 100)
y = K - K * np.exp(-t / τ)
plt.plot(t, y)
plt.plot(t, np.ones_like(t), "r--")
plt.show()
