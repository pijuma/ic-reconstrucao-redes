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

def gerar(alfa, c, N, kmax):
    grau = binomial_neg(alfa, c, N, kmax)
    print("grau calculado")
    rede = model_configuration_network(N, grau, seed = 42)
    print("rede gerada")
    grau_nos, knn = knn_k(rede, N)
    return rede, grau_nos, knn 

def arrumar_knn(k_nodes, knn_nodes, k_min = 0, k_max = 300, min_count=5):
    
    k_nodes = np.asarray(k_nodes, dtype=int)
    knn_nodes = np.asarray(knn_nodes, dtype=int)
    kmax = int(k_nodes.max())

    sum_knn = np.bincount(k_nodes, weights=knn_nodes, minlength=kmax+1)
    cnt = np.bincount(k_nodes, minlength=kmax+1)

    with np.errstate(invalid='ignore', divide='ignore'):
        knn_k = sum_knn / np.where(cnt == 0, np.nan, cnt)

    degrees = np.arange(kmax+1)
    mask = (degrees >= k_min) & (degrees <= k_max) & (cnt >= min_count) & np.isfinite(knn_k)
    return degrees[mask], knn_k[mask]


"""
Para o caso da exponencial
"""
N = 50000
c = 6
alfa = 1

rede_exp, k_exp, knn_exp = gerar(alfa, c, N, 300)

print("montei a exp")

"""
Para o caso da variância tender ao infinito
"""
alfa = 0.1
rede_var, k_var, knn_var = gerar(alfa, c, N, 300)
print("montei a var")
"""
Para o caso da Poisson
"""
alfa = 1000
rede_pois, k_pois, knn_pois = gerar(alfa, c, N, 300)
print("montei a pois")

#gráfico knn x grau
x_var, y_var = arrumar_knn(k_var, knn_var)
x_exp, y_exp = arrumar_knn(k_exp, knn_exp)
x_pois, y_pois = arrumar_knn(k_pois, knn_pois)

fig, ax = plt.subplots()
ax.set_xlabel('grau', fontsize=14)
ax.set_ylabel('knn_x', fontsize=14)
ax.set_xlim(0, 400)
ax.plot(x_var, y_var, 'r', label = 'alfa = 0.1', lw=0.5)
ax.plot(x_exp, y_exp, 'g', label = 'alfa = 1', lw=0.5)
ax.plot(x_pois, y_pois, 'b', label = 'alfa = 1000', lw=0.5)

ax.legend()
#fig.show()

fig.savefig(f"redes.png")