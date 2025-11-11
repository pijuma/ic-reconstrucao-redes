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
from metrics import * 

"""
Para o caso da exponencial
"""
N = 1000
c = 800
alfa = 1

grau = binomial_neg(alfa, c, N)
rede_exp = make_nx_graph(grau)

knn_exp = knn_k(rede_exp, N)

"""
Para o caso da variância tender ao infinito
"""
alfa = 0.1

grau = binomial_neg(alfa, c, N)
rede_var = make_nx_graph(grau)
knn_var = knn_k(rede_var, N)

"""
Para o caso da Poisson
"""
alfa = 10000

grau = binomial_neg(alfa, c, N)

rede_pois = make_nx_graph(grau)
knn_pois = knn_k(rede_pois, N)

#gráfico knn x grau
t = range(0, len(knn_var))

fig, ax = plt.subplots()

ax.set_xlabel('grau', fontsize=14)
ax.set_ylabel('knn_x', fontsize=14)
#ax.plot(t, knn_var, 'r', label = 'alfa = 0.1', lw=0.5)
ax.plot(t, knn_exp, 'g', label = 'alfa = 1', lw=0.5)
ax.plot(t, knn_pois, 'b', label = 'alfa = 1000', lw=0.5)

ax.legend()
#fig.show()

fig.savefig(f"redes.png")