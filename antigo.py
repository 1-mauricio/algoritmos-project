import sys

class Grafo:
    def __init__(self, vertices, arestas):
        self.V = vertices
        self.A = arestas

    def vizinhos(self, node):
        "Returns the neighbors of a node."
        conexoes = []
        for out_node in self.V:
            if self.A[node].get(out_node, False) != False:
                conexoes.append(out_node)
        return conexoes

    def dijkstra_algorithm(self, start):
        nao_visitados = list(self.V)
    
        # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
        menor_caminho = {}
    
        # We'll use this dict to save the shortest known path to a node found so far
        previous_nodes = {}
    
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
        max_value = sys.maxsize

        for node in nao_visitados:
            menor_caminho[node] = max_value
        # However, we initialize the starting node's value with 0   
        menor_caminho[start] = 0
        
        # The algorithm executes until we visit all nodes
        while nao_visitados:
            # The code block below finds the node with the lowest score
            current_min_node = None
            for node in nao_visitados: # Iterate over the nodes
                if current_min_node == None:
                    current_min_node = node
                elif menor_caminho[node] < menor_caminho[current_min_node]:
                    current_min_node = node
                    
            # The code block below retrieves the current node's neighbors and updates their distances
            vizinhos = self.vizinhos(current_min_node)
            for vizinho in vizinhos:
                valor_tentado = menor_caminho[current_min_node] + self.A[current_min_node][vizinho]
                if valor_tentado < menor_caminho[vizinho]:
                    
                    menor_caminho[vizinho] = valor_tentado
                    # We also update the best path to the current node
                    previous_nodes[vizinho] = current_min_node
    
            # After visiting its neighbors, we mark the node as "visited"
            nao_visitados.remove(current_min_node)
    
        return menor_caminho

if __name__ == '__main__':
    vertices = []
    nome = {}
    grafo = {}
    big = 0

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

            if int(value[1]) > big:
                big = int(value[1])

            grafo[int(source[1])][int(target[1])] = int(value[1])
            grafo[int(target[1])][int(source[1])] = int(value[1])

    g = Grafo(vertices, grafo)
    # peso 1 - 31

    print("="*30)
    print("DE ENCONTRO A JEAN VALJEAN")
    print("="*30)

    s = int(input("\nEscolha seu personagem partida: "))
    while s >= 0:
        t = int(input("Escolha seu personagem destino: "))
        menor_caminho = g.dijkstra_algorithm(s)
        print(f"{nome[s]} --> {nome[t]} = {menor_caminho[t]}")
        s = int(input("\nEscolha seu personagem source: "))
