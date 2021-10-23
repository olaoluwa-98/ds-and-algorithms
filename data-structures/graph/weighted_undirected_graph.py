class WeightedUndirectedGraph:
    def __init__(self) -> None:
        self.graph = {}
    
    def add_vertex(self, vertex):
        if self.graph.get(vertex) is None:
            self.graph[vertex] = []

    def add_edge(self, v1, v2, weight):
        if self.graph.get(v1) is None or self.graph.get(v1) is None:
            return False
        # Since this code is not restricted to a directed or 
        # an undirected graph, an edge between v1 v2 does not
        # imply that an edge exists between v2 and v1
        self.graph[v1].append([v2, weight])
    
    def print_graph(self):
        for vertex in self.graph:
            for edges in self.graph[vertex]:
                print(vertex, " -> ", edges[0], " edge weight: ", edges[1])

graph = WeightedUndirectedGraph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)

# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
graph.add_edge(1, 2, 1)
graph.add_edge(1, 3, 1)
graph.add_edge(2, 3, 3)
graph.add_edge(3, 4, 4)
graph.add_edge(4, 1, 5)
graph.print_graph()

# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print ("Internal representation: ", graph.graph)