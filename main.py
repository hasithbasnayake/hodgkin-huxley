# .\env\Scripts\activate to activate virtual environment
# pip freeze > requirements.txt You can export a list of all installed packages
# pip install -r requirements.txt to install from a requirements file
# pip list to list all packages

from func import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.interpolate import interp1d

Neuron = Neuron(g_Leak= 0.3, g_Na = 120, g_K = 36, v_Na = 45, v_K = -82, v_Leak = -60, C_m = 1)

t = np.arange(0,300,1)
I_input = np.zeros(t.shape, dtype = t.dtype)
I_input[(t>50) & (t<100)] = 10
I_input[(t>150) & (t<200)] = 30

init_vals = [-65.0, 0.05, 0.32, 0.6]
I_interp = interp1d(t, I_input, fill_value='extrapolate')
C = odeint(C_dvdt, init_vals, t, args=(I_interp, Neuron.g_Na, Neuron.v_Na, Neuron.g_K, Neuron.v_K, Neuron.g_Leak, Neuron.v_Leak))

V = C[:,0]

plt.plot(t, V, 'y')
plt.show()

print(Neuron)

#Next, take advantage of Python classes and expand upon code for readability and clarity