class UndirectedGraph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = [[0] * num_nodes for i in range(num_nodes)]

    def add_edge(self, u, v):
        if 0 <= u < self.num_nodes and 0 <= v < self.num_nodes:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
    
    def node_exists(self, u):
        return 0 <= u < self.num_nodes

    def edge_exists(self, u, v):
        if self.node_exists(u) and self.node_exists(v):
            return self.adj_matrix[u][v] == 1
        return False
    
    def get_neighbors(self, u):
        neighbors = []
        if self.node_exists(u):
            for v in range(self.num_nodes):
                if self.adj_matrix[u][v] == 1:
                    neighbors.append(v)
        return neighbors 

    def get_edge_density(self):
        num_edges = 0
        for u in range(self.num_nodes):
            for v in range(u + 1, self.num_nodes):
                if self.adj_matrix[u][v] == 1:
                    num_edges += 1
        total_possible_edges = (self.num_nodes * (self.num_nodes - 1)) / 2
        if total_possible_edges == 0:
            return 0
        edge_density =  num_edges / total_possible_edges
        return round(edge_density, 2)
        
    
    def is_complete(self):
        for u in range(self.num_nodes):
            for v in range(u + 1, self.num_nodes):
                if self.adj_matrix[u][v] == 0:
                    return False
        return True

graph = UndirectedGraph(4) # creates graph with 4 nodes
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,2)
graph.add_edge(2,3)

print(graph.node_exists(1)) # expected output: True
print(graph.node_exists(10)) # expected output: False

print(graph.edge_exists(1,2)) # expected output: True
print(graph.edge_exists(1,3)) # expected output: False

print(graph.get_neighbors(1)) # expected output: [0,2]

print(graph.get_edge_density()) # expected output: 0.67

print(graph.is_complete()) # expected output: False
