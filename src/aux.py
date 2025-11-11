import networkx as nx
import matplotlib.pyplot as plt 

"""
retorna numero de vertices
numero de aresta
e o grafo se id = 1
"""
def graph_info(G, id):
  print("qtd Vertices:")
  print(G.number_of_nodes())
  print("qtd arestas:")
  print(G.number_of_edges())
  if(id == 1):
    print(G.edges)

def visualize(G, ct):
  plt.figure(figsize=(10, 10))
  nx.draw(G,
        node_size=400,
        node_color='skyblue',
        edge_color='gray',
        width=1.5,
        with_labels=True)
  #plt.show() -> se tiver interface 
  plt.savefig(f"visu{ct}.png")


