class Grafo:
    def __init__(self, vertices, arestas):
        self.V = vertices
        self.A = arestas

    def get_shortest_path(self, menor_caminho, not_cheked):
        menor_custo = inf
        node_menor_custo = None
        for node in not_cheked:
            if menor_caminho[node] <= menor_custo:
                menor_custo = menor_caminho[node]
                node_menor_custo = node
        return node_menor_custo

    def dijkstra_algorithm(self, source, target):
        menor_caminho = {}
        vizinhos = {}
        for node in self.A:
            menor_caminho[node] = float('inf')
            vizinhos[node] = {}

        menor_caminho[source] = 0

        nao_visitados = [node for node in menor_caminho]
        node  = self.get_shortest_path(menor_caminho, nao_visitados)
        while nao_visitados:
            custo_atual = menor_caminho[node]
            custo_vizinho = self.A[node]
            for c in custo_vizinho:
                if menor_caminho[c] > custo_atual + custo_vizinho[c]:
                    menor_caminho[c] = custo_atual + custo_vizinho[c]
                    vizinhos[c] = node

            nao_visitados.pop(nao_visitados.index(node))
            node = self.get_shortest_path(menor_caminho, nao_visitados)

        if menor_caminho[target] < inf:
            caminho = [target]
            i = 0
            while source not in caminho:
                caminho.append(vizinhos[caminho[i]])
                i += 1
            caminho.reverse()
        else:
            return "Não é possível chegar ao destino"

        return caminho, menor_caminho


if __name__ == '__main__':
    inf = float('inf')
    vertices = []
    nome = {}
    grafo = {}

    data = open('data\lesmis.txt', 'r')

    for line in data:
        if 'node' in line:
            id = next(data).split()
            label = next(data).split()
            vertices.append(int(id[1]))
            nome[int(id[1])] = label[1]
            grafo[int(id[1])] = {}

        elif 'edge' in line:
            source = next(data).split()
            target = next(data).split()
            value = next(data).split()

            grafo[int(source[1])][int(target[1])] = int(value[1])
            grafo[int(target[1])][int(source[1])] = int(value[1])

    g = Grafo(vertices, grafo)

    print("="*30)
    print("DE ENCONTRO A JEAN VALJEAN")
    print("="*30)

    s = int(input("\nEscolha seu personagem partida: "))
    while s >= 0:
        t = int(input("Escolha seu personagem destino: "))
        retorno = g.dijkstra_algorithm(s,t)
        if len(retorno) == 1:
            print(retorno)
        else:
            caminho, custo_menor_caminho = retorno
            nomes = []
            for i in caminho:
                nomes.append(nome[i])

            print(f'Para chegar em {nome[t]}, {nome[s]} precisa passar por: {nomes}, e isso tem custo de {custo_menor_caminho[t]}')

        s = int(input("\nEscolha seu personagem source: "))
    