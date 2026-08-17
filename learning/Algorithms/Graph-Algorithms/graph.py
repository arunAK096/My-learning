class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            self.gdict = {}
        else:
            self.gdict = gdict

    def add_edge(self, vertex, edge):
        if vertex in self.gdict:
            self.gdict[vertex].append(edge)


custom_graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B", "E"],
    "E": ["B", "C", "D", "F"],
    "F": ["E"]
}

graph = Graph(custom_graph)

graph.add_edge("E", "C")

print("Edges connected to E:", graph.gdict["E"])
