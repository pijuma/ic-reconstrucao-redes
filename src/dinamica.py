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
Primeiro implementando um runge kutta 
padrão para uma equação de Lorenz 1963. 
Para testar o implementado no vídeo:
https://www.youtube.com/watch?v=vNoFdtcPFdk
"""

#lorenz parameters
sigma = 10
beta = 4/3
rho = 28

#rossler parameters
alfa = 0.15
b = 0.2
c = 10
omega = 1-0.015

def lorenz(t, x):
  xdot = [sigma*(x[1]-x[0]), x[0]*(rho-x[2]) - x[1], x[0]*x[1] - beta*x[2]]
  return np.array(xdot)

"""
função para calcular a integral numérica
usando método de runge-Kutta de 4a ordem
"""

def runge_kutta(f, dt, y0, t0, t):

  func = []
  x_k = y0
  func.append(x_k)

  for i in range(len(t)):
    f1 = f(t[i], x_k)
    f2 = f(t[i]+(dt/2), x_k + (dt/2)*f1)
    f3 = f(t[i]+(dt/2), x_k + (dt/2)*f2)
    f4 = f(t[i]+dt, x_k + dt*f3)
    x_k = x_k + (dt/6)*(f1 + 2*f2 + 2*f3 + f4)
    func.append(x_k)

  return func

#calling runge_kutta for lorrenz attractor
y0 = [-8, 8, 27]
dt = 0.01
T = 10
num_pto = int(T/dt)

t = np.linspace(0, T, num_pto)
Y = runge_kutta(lorenz, dt, y0, 0, t)

ax = plt.figure().add_subplot(projection='3d')
ax.plot([y[0] for y in Y], [y[1] for y in Y], [y[2] for y in Y], 'r', lw=0.5)

#for comparison with the library implementation
lorenz_sol = solve_ivp(lorenz, (0, T), y0, t_eval=t)
t = lorenz_sol.t
y = lorenz_sol.y.T
ax.plot(y[:, 0], y[:, 1], y[:, 2], 'b')
#plt.show()
plt.savefig(f"Lorrenz.png")

"""
Applying for rossler attractor
without coupling
"""

def rossler(t, x):
  dot = [-omega*x[1] - x[2], omega*x[0] + alfa*x[1], b + x[2]*(x[0]-c)]
  return np.array(dot)

#calling runge_kutta for rossler attractor
y0 = [-8, 8, 27]
dt = 0.01
T = 2000
num_pto = int(T/dt)

t = np.linspace(0, T, num_pto)
Y = runge_kutta(rossler, dt, y0, 0, t)

ax = plt.figure().add_subplot(projection='3d')
ax.plot([y[0] for y in Y], [y[1] for y in Y], [y[2] for y in Y], 'r', lw=0.5)

#fazendo com implementação da biblioteca
rossler_sol = solve_ivp(rossler, (0, T), y0, t_eval=t)
t = rossler_sol.t
y = rossler_sol.y.T
ax.plot(y[:, 0], y[:, 1], y[:, 2], 'b')
#plt.show()
plt.savefig(f"Rossler.png")

