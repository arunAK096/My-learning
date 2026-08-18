class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2):
        self.adjacency_list[v1].append(v2)
        self.adjacency_list[v2].append(v1)

    def dfs(self, start_vertex):
        visited = set()
        stack = [start_vertex]
        while len(stack) > 0:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex, end=" ")
                visited.add(current_vertex)
                for neighbor in self.adjacency_list[current_vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)

custom_graph = Graph()
custom_graph.add_vertex("A")
custom_graph.add_vertex("B")
custom_graph.add_vertex("C")
custom_graph.add_vertex("D")
custom_graph.add_vertex("E")

custom_graph.add_edge("A", "B")
custom_graph.add_edge("A", "C")
custom_graph.add_edge("B", "D")
custom_graph.add_edge("C", "E")

print("DFS Traversal:")
custom_graph.dfs("A")