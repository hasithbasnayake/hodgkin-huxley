import numpy as np

class Neuron():
    def __init__(self, g_Leak, g_Na, g_K, v_Na, v_K, v_Leak, C_m, Vm):
        self.g_Leak = g_Leak
        self.g_Na = g_Na
        self.g_K = g_K
        self.v_Na = v_Na
        self.v_K = v_K
        self.v_Leak = v_Leak
        self.C_m = C_m
    
    def __str__(self):
        return (f"Neuron: g_Leak={self.g_Leak}, g_Na={self.g_Na}, g_K={self.g_K}, "
                f"v_Na={self.v_Na}, v_K={self.v_K}, v_Leak={self.v_Leak}, C_m={self.C_m}")

def alpha_m(Vm):
    (.1 * (Vm + 40)) / (1 - np.exp(-.1 * (Vm + 40)))

def beta_m(Vm):
    4 * np.exp(-.0556 * (Vm + 65))

def alpha_h(Vm):
    .07 * np.exp(-.05 * (Vm + 65))

def beta_h(Vm):
    1 / (1 + np.exp(-.1 * (Vm + 35)))

def alpha_n(Vm):
    0.01 * (Vm + 55) / (1 - np.exp(-(Vm + 55) / 10))

def beta_n(Vm):
    .125 * np.exp(-.0125 * (Vm + 65))

def I_K(Vm, n, g_K, v_K):
    return g_K * n**4 * (Vm - v_K)

def I_Na(Vm, m, h, g_Na, v_Na):
    return m**3 * h * g_Na * (Vm - v_Na)

def I_Leak(Vm, g_Leak, v_Leak):
    return g_Leak * (Vm - v_Leak)
