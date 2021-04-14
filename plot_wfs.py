import os
import numpy as np
import matplotlib.pyplot as plt

waveforms = [f for f in os.listdir('.') if f.endswith(".txt")]

for wf in waveforms:

    data = np.loadtxt(wf)
    plt.figure()
    plt.plot(data)
    plt.savefig(f'{wf[:-4]}.png')
    plt.close('all')
