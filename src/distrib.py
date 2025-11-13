from gerador_rede import *
import numpy as np 

def poison_graph(N):
  grau = np.random.poisson(lam=2, size=N).astype(int)
  while sum(grau) % 2 != 0:
    grau = np.random.poisson(lam=2, size=N).astype(int)
  return model_configuration_network(N, grau)

def binomial_graph(N):
  grau = np.random.binomial(n=2, p=0.5, size=N).astype(int)
  while sum(grau) % 2 != 0:
     grau = np.random.binomial(n=2, p=0.5, size=N).astype(int)
  return model_configuration_network(N, grau)

"""
alfa é o formato, c/alfa a escala e N é o número de nós
"""
def binomial_neg(alfa, c, N, k_max):
  lmbd = np.random.gamma(shape=alfa, scale=c/alfa, size=N)
  k = np.random.poisson(lam=lmbd)
  k = np.clip(k, 0, k_max)  
  #para garantir que teremos soma de grau par (possivel montar rede)
  if k.sum() % 2 == 1:
    idx = np.random.randint(0, N)
    if k[idx] < k_max:
        k[idx] += 1
    else:
        k[idx] -= 1
  return k