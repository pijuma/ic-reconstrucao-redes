from dinamica import *
from gerador_rede import *
from distrib import *
from aux import * 
import numpy as np 
import random
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import collections
from scipy.integrate import solve_ivp
from scipy.signal import hilbert

"""
Checando como varia a diferença de fase/acoplamento 
a depender da varíavel que define a força desse (C)
"""

"""
Como retorno da função temos:
o sinal, o envelope, a fase instantânea e a frequência
"""
def analytic_hilbert(x):

    x_h = hilbert(x)
    env = np.abs(x_h)
    insta_phase = np.unwrap(np.angle(x_h))

    return x_h, env, insta_phase

Y1 = runge_kutta(rossler_acoplado, dt, y0, 0, w0, w1, 0.01, t)

x_h1, env1, insta_phase1 = analytic_hilbert([y[0] for y in Y1])
x_h2, env2, insta_phase2 = analytic_hilbert([y[3] for y in Y1])

Y1 = runge_kutta(rossler_acoplado, dt, y0, 0, w0, w1, 0.027, t)

x_h1, env1, ip17 = analytic_hilbert([y[0] for y in Y1])
x_h2, env2, ip27 = analytic_hilbert([y[3] for y in Y1])

Y1 = runge_kutta(rossler_acoplado, dt, y0, 0, w0, w1, 0.035, t)

x_h1, env1, ip15 = analytic_hilbert([y[0] for y in Y1])
x_h2, env2, ip25 = analytic_hilbert([y[3] for y in Y1])

#Gráfico
p1 = [insta_phase1[i]-insta_phase2[i] for i in range(len(insta_phase1))]
p17 = [ip17[i]-ip27[i] for i in range(len(ip17))]
p15 = [ip15[i]-ip25[i] for i in range(len(ip15))]

plt.xlabel('time', fontsize=14)
plt.ylabel(r'$\phi_1 - \phi_2$', fontsize=14)
plt.xlim(0, 2010)
plt.ylim(-10, 70)
plt.grid(False)
plt.plot(t, p1, 'r', label = 'C = 0.01', lw=0.5)
plt.plot(t, p17, 'b', label = 'C=0.027', lw=0.5)
plt.plot(t, p15, 'g', label = 'C=0.035', lw=0.5)
plt.legend()
#plt.show()
plt.savefig(f"dif_phase.png")