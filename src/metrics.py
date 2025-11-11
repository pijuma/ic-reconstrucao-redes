"""
Dada uma rede como entrada e a quantidade de nós
essa função retorna o knn para cada grau
"""

def knn_k(grafo, N):
  grau = [0 for i in range(N)]
  for i in range(N):
    grau[i] = len(list(grafo.neighbors(i)))

  knn = [0 for i in range(N)]

  #para cada nó irei calcular o knn
  for i in range(N):
    sum = 0
    for j in list(grafo.neighbors(i)):
      sum += grau[j]
    if(grau[i] > 0):
       knn[i] = sum/grau[i]

  knn_grau = [0 for i in range(N)]
  qtd = [0 for i in range(N)] #quantos nós possuem aquele grau

  for i in range(N):
    qtd[grau[i]]+=1
    knn_grau[grau[i]] += knn[i]

  for i in range(N):
    if(grau[i]>0):
       knn_grau[i] /= grau[i]

  return knn_grau