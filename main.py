# .\env\Scripts\activate to activate virtual environment
# pip freeze > requirements.txt You can export a list of all installed packages
# pip install -r requirements.txt to install from a requirements file
# pip list to list all packages

import numpy as np

# The hogkin-huxley neuronal model allows one to simulate a neuron through an approximation of voltage gated dynamics
# It is one of the most computationally equivalent biological models of the neuron, which comes as at a computational cost 

class Neuron():
    def __init__(self, g_Leak, g_Na, g_K, v_Na, v_K, v_Leak, C_m, Vm):
        self.g_Leak = g_Leak
        self.g_Na = g_Na
        self.g_K = g_K
        self.v_Na = v_Na
        self.v_K = v_K
        self.v_Leak = v_Leak
        self.C_m = C_m

        self.Vm = Vm

        alpha_m = (.1 * (Vm + 40)) / (1 - np.exp(-.1 * (Vm + 40)))
        beta_m = 4 * np.exp(-.0556 * (Vm + 65))
        alpha_h = .07 * np.exp(-.05 * (Vm + 65))
        beta_h = 1 / (1 + np.exp(-.1 * (Vm + 35)))
        alpha_n = 0.01 * (Vm + 55) / (1 - np.exp(-(Vm + 55) / 10))
        beta_n = .125 * np.exp(-.0125 * (Vm + 65))
    
    def __str__(self):
        return (f"Neuron: g_Leak={self.g_Leak}, g_Na={self.g_Na}, g_K={self.g_K}, "
                f"v_Na={self.v_Na}, v_K={self.v_K}, v_Leak={self.v_Leak}, C_m={self.C_m}")

    


# Created class scaffolding for later implementation

Neuron = Neuron(g_Leak= 0.3, g_Na = 120, g_K = 36, v_Na = 45, v_K = -82, v_Leak = -60, C_m = 1)

print(Neuron)