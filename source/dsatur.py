


ESTADOS = [
    "AC", "AL", "AM", "AP", "BA", "CE", "DF",
    "ES", "GO", "MA", "MG", "MS", "MT", "PA",
    "PB", "PE", "PI", "PR", "RJ", "RN", "RO",
    "RR", "RS", "SC", "SE", "SP", "TO"
]

def dsatur(graph):
    vertices = graph.V
    cores = [-1]*vertices
    cor_vizinhos = [set() for _ in range(vertices)]
    degree = list(graph.degree(v) for v in range(vertices))
    descolorido = list(range(vertices))

    while descolorido:
        u = max(descolorido, key=lambda v: (len(cor_vizinhos[v]), degree[v]))
        cores_vizinhas = {cores[v] for v in graph.adj[u] if cores[v] != -1}
        menor_cor = 0
        while menor_cor in cores_vizinhas:
            menor_cor += 1 

        cores[u] = menor_cor
        descolorido.remove(u)

        for vizinhos in graph.adj[u]:
            if cores[vizinhos] == -1:
                cor_vizinhos[vizinhos].add(menor_cor)


    tiposcores = set(cores)
    print("cores usadas: ",tiposcores)
    print("quantidade de cores: ",len(tiposcores),end="\n" )
    print(cor_vizinhos,end="\n")
    
    for i in range(len(cores)):
        print(f"Estado: {ESTADOS[i]} -> Cor: {cores[i]}")