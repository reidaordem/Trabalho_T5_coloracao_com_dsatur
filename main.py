import os 
from dsatur import dsatur
from graph import Graph
arquivo = input("forneça o caminho do arquivo, Exemplo(sem as contra barras duplas): C:\\Users\\Usuario\\Downloads\\t5\\dados\\brasil.txt")


with open(arquivo) as f:
    V = int(f.readline())
    E = int(f.readline())
    graph = Graph(V)
    for _ in range(E):
        v,w = f.readline().split()
        graph.add_edge(v,w)



dsatur(graph)

