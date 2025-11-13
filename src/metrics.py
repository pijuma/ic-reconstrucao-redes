
import numpy as np 
import random
import networkx as nx
import matplotlib.pyplot 
"""
Dada uma rede como entrada e a quantidade de nós
essa função retorna o knn para cada grau
"""

def knn_k(grafo, N):

  grau = [grafo.degree[i] for i in range(N)]

  kmax = max(grau)

  #mantem o grau medio dos vizinhos do nó
  knn = [0]*(N)

  #para cada nó irei calcular o knn
  for i in range(N):
    sum = 0
    #qual soma do grau dos vizinhos de i? 
    for j in list(grafo.neighbors(i)):
      sum += grau[j]
    #knn dele eh a soma/quantidade vizinhos (grau dele)
    if(grau[i] > 0):
      knn[i] = sum/grau[i]
  
  return grau, knn 

  qtd = [0]*(kmax+1)
  #qual soma dos knn de caras que tem grau i? 
  knn_grau = [0]*(kmax+1)
  
  for i in range(N):
    qtd[grau[i]]+=1
    knn_grau[grau[i]] += knn[i]

  for i in range(kmax+1):
    if(qtd[i]>0):
      knn_grau[i] /= qtd[i]

  return knn_grau