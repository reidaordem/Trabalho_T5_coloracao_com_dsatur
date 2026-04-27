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
    ordem_de_coloracao = [] 

    while descolorido:

        u = max(descolorido, key=lambda v: (len(cor_vizinhos[v]), degree[v]))
        ordem_de_coloracao.append(u)
        cores_vizinhas = {cores[v] for v in graph.adj[u] if cores[v] != -1}
        menor_cor = 0

        while menor_cor in cores_vizinhas:
            menor_cor += 1 

        cores[u] = menor_cor
        descolorido.remove(u)

        for vizinhos in graph.adj[u]:
            if cores[vizinhos] == -1:
                cor_vizinhos[vizinhos].add(menor_cor)

    cores_vizinhos_final = []
    for u in range(vertices):
        cores_dos_vizinhos = {cores[v] for v in graph.adj[u] if cores[v] != -1}
        cores_vizinhos_final.append(cores_dos_vizinhos)

    # Teste de validação
    valido = True
    for u in range(graph.V):
        for v in graph.adj[u]:
            if cores[u] == cores[v]:
                print(f"Erro: {ESTADOS[u]} e {ESTADOS[v]} têm a mesma cor!")
                valido = False
    if valido:
        print("Sucesso: A coloração é válida!",end="\n")

    tiposcores = set(cores)

    print("Ordem de coloração:", [ESTADOS[i] for i in ordem_de_coloracao])

    print("cores usadas: ",tiposcores,end="\n")

    print("quantidade de cores: ",len(tiposcores),end="\n" )

    print("Cores dos vizinhos :", cores_vizinhos_final,end="\n")
    
    for i in range(len(cores)):
        print(f"Estado: {ESTADOS[i]} -> Cor: {cores[i]}")
