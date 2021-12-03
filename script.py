import sys

class Grafo:
    def __init__(self, vertices, arestas):
        self.V = vertices
        self.A = arestas

    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.V:
            if self.A[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.A[node1][node2]

    def dijkstra_algorithm(self, start_node):
        unvisited_nodes = list(self.V)
    
        # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
        shortest_path = {}
    
        # We'll use this dict to save the shortest known path to a node found so far
        previous_nodes = {}
    
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
        max_value = sys.maxsize

        for node in unvisited_nodes:
            shortest_path[node] = max_value
        # However, we initialize the starting node's value with 0   
        shortest_path[start_node] = 0
        
        # The algorithm executes until we visit all nodes
        while unvisited_nodes:
            # The code block below finds the node with the lowest score
            current_min_node = None
            for node in unvisited_nodes: # Iterate over the nodes
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node
                    
            # The code block below retrieves the current node's neighbors and updates their distances
            neighbors = self.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + self.value(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    # We also update the best path to the current node
                    previous_nodes[neighbor] = current_min_node
    
            # After visiting its neighbors, we mark the node as "visited"
            unvisited_nodes.remove(current_min_node)
    
        return previous_nodes, shortest_path

if __name__ == '__main__':
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
    previous_nodes, shortest_path = g.dijkstra_algorithm(15)
    # print(nome[66])
    print(shortest_path[66])
