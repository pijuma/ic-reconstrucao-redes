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

"""
Gera um grafo simples (sem laço/multiaresta)
com sequencia de grau igual a dada
- Usa Havel-Hakimi para construir um grafo simples 
- aleatoriza as arestas mantendo o grau 
"""
def model_configuration_network(N, grau, nswap_fac=10, max_tries_fac=100, seed=None):

  G = nx.configuration_model(grau)

  G = nx.Graph(G)
  G.remove_edges_from(nx.selfloop_edges(G))

  return G 

  """
  deg_seq = list(int(d) for d in grau)

  if any(d < 0 for d in grau):
    print("grau negativo")
    return -1 
  
  N = len(grau)

  if any(d >= N for d in grau):
    print("Acima de N")
    return -1 
  
  #the quantity of stubs has to be even so we can pair the nodes
  if (grau.sum()%2):
    print("Soma impar")
    return -1
  
  if not nx.is_graphical(deg_seq, method="eg"):
    print("Sequência não é gráfica")
    return -1 
  
  G = nx.havel_hakimi_graph(deg_seq)

  M = G.number_of_edges()

  if M == 0: 
    return G 
  
  nswap = int(nswap_fac*M)
  max_tries = int(max_tries_fac*nswap)

  nx.double_edge_swap(G, nswap=nswap, max_tries=max_tries, seed=seed)

  return G
  """

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

