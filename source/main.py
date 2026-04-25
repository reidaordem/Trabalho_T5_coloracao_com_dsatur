import sys
from dsatur import dsatur
from graph import Graph

if ( len(sys.argv) <= 1 ):
    print("informe o arquivo de entrada. Ex.: python main.py ../dados/brasil.txt")
    sys.exit(1)

arquivo = sys.argv[1]

with open(arquivo) as f:
    V = int(f.readline())
    E = int(f.readline())
    graph = Graph(V)
    for _ in range(E):
        v,w = f.readline().split()
        graph.add_edge(v,w)

dsatur(graph)

