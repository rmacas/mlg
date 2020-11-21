import numpy as np
import matplotlib.pyplot as plt


a = np.loadtxt("9_103_clean.txt")
a = np.loadtxt("9_103_noise.txt")
a = np.loadtxt("9_103_noisy_6dB.txt")
a = np.loadtxt("9_103_denoised_2dB.txt")

plt.plot(a)
plt.show()
