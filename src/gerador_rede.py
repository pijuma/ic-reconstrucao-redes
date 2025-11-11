import networkx as nx
import random 

"""
generates a graph using configuration model (canonic)
without selfloops and with all edges being different
as input: number of nodes and the expected values for the degree of each node
as output: a network with the given distribution of degree following the configuration model
"""
def valid(i, j, past):
  if i == j:
    return 0
  if (i, j) in past:
    return 0
  return 1


def model_configuration_network(N, grau):

  G = nx.Graph()

  for i in range(N):
    G.add_node(i)

  edges_add = {}
  sum = 0

  for i in grau:
    sum += i
  #the quantity of stubs has to be even so we can pair the nodes
  #a quantidade de stubs deve ser par para possibilitar o pareamento
  if (sum & 1):
    return -1

  while sum != 0:

    i = j = 0
    #talvez seja melhor criar uma lista com todos graus ao invés de fazer assim
    while (valid(i, j, edges_add) == 0 or grau[i] == 0 or grau[j] == 0):
      i = random.randint(0, N-1)
      j = random.randint(0, N-1)
      grau[i]-=1
      grau[j]-=1

    G.add_edge(i, j)
    #bidirecional graph
    edges_add[(i, j)] = edges_add[(j, i)] = 1
    sum -= 2

  return G

"""
Para o modelo de Chung-Lu:
https://github.com/ftudisco/scalefreechunglu/blob/master/python/fastchunglu.py 
"""

from networkx import Graph
from scipy.sparse import csr_matrix
import numpy as np

def make_nx_graph(w):
  n = np.size(w)
  print("nos ", n)
  s = np.sum(w)
  m = ( np.dot(w,w)/s )**2 + s
  m = int(m/2)
  wsum = np.cumsum(w)
  wsum = np.insert(wsum,0,0)
  wsum = wsum / wsum[-1]
  I = np.digitize(np.random.rand(m,1), wsum) - 1
  J = np.digitize(np.random.rand(m,1), wsum) - 1
  I = I.reshape(m,).astype(int)
  J = J.reshape(m,).astype(int)

  # converte para lista de tuplas puras de inteiros Python
  edges = [(int(i), int(j)) for i, j in zip(I, J)]

  G = Graph()
  G.add_nodes_from(range(n))
  G.add_edges_from(edges)
  return G

