from collections import defaultdict


class Vertex:
    def __init__(self, data):
        self.index = data['index']
        self.p = data['point']


class Graph:
    def __init__(self):
        self.__vertices = []
        self.__adj_list = defaultdict(set)
        self.__edge_set = set()

    def add_edge(self, u: Vertex, v: Vertex):
        if u not in self.__vertices or v not in self.__vertices:
            print("graph.add_edge: invalid vertices given.")
            return None

        self.__adj_list[u].add(v)
        self.__adj_list[v].add(u)

    def set_edge_list(self):
        self.__edge_set = set()
        for v in self.__vertices:
            for u in self.__adj_list[v]:
                self.__edge_set.add({u, v})

    @property
    def edge_set(self):
        return self.__edge_set

    def __contains__(self, edge):
        if type(edge) is set:
            if edge in self.__edge_set:
                return True
            else:
                return False
        elif type(edge) is tuple:
            if edge[0] in self.__adj_list[edge[1]] and edge[1] in self.__adj_list[edge[0]]:
                return True
            else:
                return False
        else:
            raise TypeError
