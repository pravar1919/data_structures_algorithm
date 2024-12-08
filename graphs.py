class Graph:
    """
    'A': []
    'B': []
    'C': []
    """
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for i in self.adj_list[vertex]:
                self.adj_list[i].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    
    def add_edges(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v2 in self.adj_list and v1 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_edges('A', 'B')
g.add_edges('A', 'C')
g.add_edges('A', 'D')
g.add_edges('B', 'D')
g.add_edges('C', 'D')

g.remove_vertex('D')
g.print_graph()