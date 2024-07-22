class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_grahp(self):
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))

g = Graph()

g.add_edge(10, 15)
g.add_edge(10, 14)
g.add_edge(14, 20)

g.print_grahp()



