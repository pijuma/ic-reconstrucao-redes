from gerador_rede import *
from distrib import *
from aux import * 
import numpy as np 

ct = 0 

G = poison_graph(100)
graph_info(G, 1)
visualize(G, 1)

#recuperando o grau pela rede gerada e verificando o histrograma
degree_seq = (d for n, d in G.degree())

freq = {}

freq[0] = 0

for d in degree_seq:
  if d not in freq:
    freq[d] = 0
  freq[d] += 1

items = sorted(freq.items())   #(grau, freq)
xs = [k for k, v in items]
ys = [(v/G.number_of_nodes()) for k, v in items]

plt.figure(figsize=(8, 5))
plt.plot(xs, ys, 'o-')
plt.title(f'Distribuição do grau')
plt.xlabel('Degree')
plt.ylabel('Frequency')
#plt.show()
plt.savefig(f"graph{ct}.png")
ct+=1
