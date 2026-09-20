from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.number_of_vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.topologicalSortUtil(neighbor, visited, stack)
        stack.insert(0, v)

    def topologicalSort(self):
        visited = []
        stack = []
        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)

        # Print the resulting sorted order
        print("Topological Sort Order:", stack)

g = Graph(8)


g.addEdge("A", "C")
g.addEdge("C", "E")
g.addEdge("B", "D")
g.addEdge("B", "E")
g.addEdge("D", "F")
g.addEdge("E", "F")
g.addEdge("F", "G")

# Run Topological Sort
g.topologicalSort()