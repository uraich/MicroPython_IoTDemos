#!/usr/bin/env python3
# using a library; matplotlib
# Uli Raich
# Demo for session1 of the workshop on IoT at the
# African Internet Summit 2019, Kampala, Uganda

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,10*np.pi,2*np.pi/200)

plt.plot(t,np.sin(t))
plt.plot(t,np.cos(t))
plt.plot(t,np.exp(-t*0.1)*np.sin(t))
plt.show()
