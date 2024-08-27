class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for nei in self.adj_list[vertex]:
                print(nei)
                self.adj_list[nei].remove(vertex)
            self.adj_list.pop(vertex)

    def printGraph(self):
        for items in self.adj_list.items():
            print(items)

if __name__ == '__main__':
    adj_list = Graph()
    adj_list.add_vertex('A')
    adj_list.add_vertex('B')
    adj_list.add_vertex('C')

    adj_list.add_edge('B', 'C')
    adj_list.printGraph()

    # adj_list.remove_edge('B', 'C')
    # adj_list.printGraph()

    adj_list.remove_vertex('B')
    adj_list.printGraph()
