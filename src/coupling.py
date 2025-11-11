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
w1 = 1 - 0.015
#tem os valores iniciais do 1o e 2o acoplador já
y0 = [-8, 8, 27, 0, 18, 27]


dt = 0.01
T = 2000

num_pto = int(T/dt)

t = np.linspace(0, T, num_pto)

"""
Função que descreve o acoplamento de dois osciladores
argumentos passados são:
x: [x, y, z] -> define os pontos atuais
w -> omega, para permitir uma diferença de fase
x2 -> para o segundo oscilador, acoplando ele
alfa, b, c, C -> parâmetros do modelo
[x1, y1, z1, x2, y2, z2]
"""
def rossler_acoplado(t, x, w1, w2, C):
  dot = [(-w1*x[1] - x[2] + C*(x[3]-x[0])),
         w1*x[0] + alfa*x[1],
         b + x[2]*(x[0]-c),
         (-w2*x[4] - x[5] + C*(x[0]-x[3])),
         w2*x[3] + alfa*x[4],
         b + x[5]*(x[3]-c)
         ]
  return np.array(dot)

#adaptando para ter os parametros do outro oscilador
def runge_kutta(f, dt, y0, t0, w1, w2, C, t):

  func = []
  x_k = y0
  func.append(x_k)

  for i in range(len(t)-1):
    f1 = f(t[i], x_k, w1, w2, C)
    f2 = f(t[i]+(dt/2), x_k + (dt/2)*f1, w1, w2, C)
    f3 = f(t[i]+(dt/2), x_k + (dt/2)*f2, w1, w2, C)
    f4 = f(t[i]+dt, x_k + dt*f3, w1, w2, C)
    x_k = x_k + (dt/6)*(f1 + 2*f2 + 2*f3 + f4)
    func.append(x_k)

  return func

"""
Testing 
"""
Y = runge_kutta(rossler_acoplado, dt, y0, 0, w0, w1, 0.027, t)

ax = plt.figure().add_subplot(projection='3d')
ax.plot([y[0] for y in Y], [y[1] for y in Y], [y[2] for y in Y], 'r', lw=0.5)
#plt.show()
plt.savefig(f"rossler_acoplado.png")
