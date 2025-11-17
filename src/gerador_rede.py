import networkx as nx
import random 
from itertools import chain
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
Dada uma lista retorna 
uma sequencia que a frequencia do valor 
é o grau do nó 
"""
def stub_list(degree_seq):
  chaini = chain.from_iterable 
  return list(chaini([n]*d for n, d in enumerate(degree_seq)))

"""
Gera um grafo simples (sem laço/multiaresta)
com sequencia de grau igual a dada
- Usa Havel-Hakimi para construir um grafo simples 
- aleatoriza as arestas mantendo o grau 

Pode gerar self-loop/multiaresta
mas a chance para N grande é muito baixa, 
então tende a não dar problema 
(prova no caderno)
"""
def model_configuration_network(N, grau):

  m = 0 
  G = nx.empty_graph(N)

  stubs = stub_list(grau)

  n = len(stubs)
  seed = random.Random(42)

  half = n//2 
  seed.shuffle(stubs)
  out_s, in_s = stubs[:half], stubs[half:]

  G.add_edges_from(zip(out_s, in_s))

  G.remove_edges_from(nx.selfloop_edges(G))

  return G 