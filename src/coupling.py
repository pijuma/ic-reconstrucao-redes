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
#parameters for each oscillator
alfa = 0.15
b = 0.2
c = 10
w0 = 1 + 0.015
#tem os valores iniciais do 1o e 2o acoplador já
X0 = np.random.uniform(-1, 1, size=(5, 3))
delta = 0.02 
w = w0 + delta*np.random.uniform(-1, 1, 5)

dt = 0.01
t0, tf = 0.0, 200.0
T = np.arange(t0, tf, dt)
K = 0.05 

"""
Função que descreve o acoplamento de dois osciladores
argumentos passados são:

X: (N, 3) - x, y, z pra cada nó 
neig -> neighrnors, neig[i] = vizinhos do nó i 
w -> vetor -> frequencia natural dos osciladores 
alfa, b, c -> parametros do modelo 
K -> força do acoplamento entre os osciladores

retorna (N, 3) - 3 edos (x, y, z) pra cada nó
"""
def rossler_rede(t, X, neig, K, w, alfa, b, c):

  N = X.shape[0] #tamanho da rede 
  dx = np.zeros_like(X) 
  
  for i in range(N):
    xi, yi, zi = X[i] 

    coup = 0.0 

    for j in neig[i]:
      coup += K*(X[j, 0] - xi) 
    
    dx[i, 0] = -w[i]*yi - zi 
    dx[i, 1] = w[i]*xi + alfa*yi 
    dx[i, 2] = b + zi*(xi-c)

  return dx
"""
f -> função = rossler, lorrenz... 
t -> tempo que irei avaliar 
X -> valores iniciais 
dt -> tamanho do passo 
*args -> genérico para qualquer modelo, passo parametros
"""

def runge_kutta(f, t, X0, dt, *args):

  X = X0.copy() #atual 
  traj = [X.copy()]

  for i in range(len(t)-1):
    
    f1 = f(t[i], X, *args)
    f2 = f(t[i]+(dt/2), X + (dt/2)*f1, *args)
    f3 = f(t[i]+(dt/2), X + (dt/2)*f2, *args)
    f4 = f(t[i]+dt, X + dt*f3, *args)

    X = X + (dt/6)*(f1 + 2*f2 + 2*f3 + f4)
    traj.append(X.copy())

  return np.array(traj) #(T, N, 3) -> pra cada periodo no tempo, cada nó, cada coordenada

"""
rede aleatória para testar
"""
N = 5 
p = 0.5 

G = nx.erdos_renyi_graph(N, p)
neig = [list(G.neighbors(i)) for i in range(N)]
print(neig)

traj = runge_kutta(
    rossler_rede,
    t,
    X0,
    dt,
    neig,
    K,
    w,
    alfa,
    b,
    c
)

x_signals = traj[:, :, 0]# (T, N)

x0 = x_signals[:, 0]# sinal do nó 0
x1 = x_signals[:, 1]# sinal do nó 1

plt.figure(figsize=(4,4))
i = 0  # nó
plt.plot(traj[:, i, 0], traj[:, i, 1], lw=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Retrato de fase – nó {i}')
plt.tight_layout()
plt.show()
