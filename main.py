# .\env\Scripts\activate to activate virtual environment
# pip freeze > requirements.txt You can export a list of all installed packages
# pip install -r requirements.txt to install from a requirements file
# pip list to list all packages

import numpy as np
import matplot.pyplot as plt 

# The hogkin-huxley neuronal model allows one to simulate a neuron through an approximation of voltage gated dynamics
# It is one of the most computationally equivalent biological models of the neuron, which comes as at a computational cost 

class Neuron():
    def __init__(self, n, m, h, c_m, I_e, g_Na, g_K, g_L, V_m, E_Na, E_K, E_L):
        n = self.n
        m = self.m 
        h = self.h 
        c_m = self.c_m
        I_e = self.I_e
        g_Na = self.g_Na
        g_K = self.g_K
        g_L = self.g_L
        V_m = self.V_m
        E_Na = self.E_Na
        E_K = self.E_K
        E_L = self.E_L  
    def __str__():
    
    def runNeuron(self):

# Created class scaffolding for later implementation