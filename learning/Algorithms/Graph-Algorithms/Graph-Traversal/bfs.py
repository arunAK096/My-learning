from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def bfs(self, start_node):
        visited = set()
        visited.add(start_node)
        queue = deque([start_node])
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")
            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


my_graph = Graph()

for node in ["A", "B", "C", "D", "E"]:
    my_graph.add_vertex(node)

my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("B", "E")
my_graph.add_edge("C", "D")
my_graph.add_edge("D", "E")

print("BFS Traversal Order:")
my_graph.bfs("A")
