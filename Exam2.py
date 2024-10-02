class UndirectedGraph:
    def __init__(self, num_nodes):
        # Initialize an adjacency matrix with num_nodes nodes, all initialized to 0
        self.num_nodes = num_nodes
        self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]
        
    def add_edge(self, u, v):
        # Add an edge between node u and v (both directions)
        if 0 <= u < self.num_nodes and 0 <= v < self.num_nodes:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def node_exists(self, u):
        # Check if the node exists in the graph
        return 0 <= u < self.num_nodes

    def edge_exists(self, u, v):
        # Check if an edge exists between node u and v
        if self.node_exists(u) and self.node_exists(v):
            return self.adj_matrix[u][v] == 1
        return False
    
    def get_neighbors(self, u):
        # Get a list of neighboring nodes of u
        neighbors = []
        if self.node_exists(u):
            for v in range(self.num_nodes):
                if self.adj_matrix[u][v] == 1:
                    neighbors.append(v)
        return neighbors
    
    def get_edge_density(self):
        # Calculate the number of edges in the graph
        num_edges = 0
        for u in range(self.num_nodes):
            for v in range(u + 1, self.num_nodes):
                if self.adj_matrix[u][v] == 1:
                    num_edges += 1
                    
        # Calculate the total possible number of edges in the graph
        total_possible_edges = (self.num_nodes * (self.num_nodes - 1)) / 2
        
        # Calculate and return the edge density
        if total_possible_edges == 0:
            return 0.0
        
        return num_edges / total_possible_edges
    
    def is_complete(self):
        # Check if the graph is complete
        # A complete graph means that all possible edges exist in the graph
        for u in range(self.num_nodes):
            for v in range(self.num_nodes):
                if u != v and self.adj_matrix[u][v] == 0:
                    return False
        return True

# Example usage
graph = UndirectedGraph(5)  # Create a graph with 5 nodes

# Add edges
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 0)

# Check if node exists
print(graph.node_exists(2))  # True
print(graph.node_exists(5))  # False

# Check if edge exists
print(graph.edge_exists(0, 1))  # True
print(graph.edge_exists(0, 2))  # False

# Get neighbors
print(graph.get_neighbors(0))  # [1, 4]

# Get edge density
print(graph.get_edge_density())  # Edge density calculation

# Check if graph is complete
print(graph.is_complete())  # False
