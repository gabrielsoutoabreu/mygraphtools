'''
@author
Gabriel Vinícius Souto Abreu
'''

from UnionFind import UnionFind
from functools import reduce
from copy import deepcopy

class Graph():

    def __init__(self, directed,  weighted, connected):
        self.__weighted = weighted
        self.__directed = directed
        self.__connected = connected
        self.__edges = list()
        self.__vertices = list()
        if weighted:
            self.__mst = list()
            self.__mstcost = 0

    def getEdgesNumber(self):
        return len(self.__edges)
    def getEdges(self):
        return deepcopy(self.__edges)

    def getVerticesNumber(self):
        return len(self.__vertices)
    def getVertices(self):
        return deepcopy(self.__vertices)

    def getMst(self):
        return deepcopy(self.__mst) if self.__weighted else None


    def __vertexIsValid(self, v):
        if type(v) == int or (type(v) == str and v.isalpha()): return True
        return False

    def getEdgesSortedByCost(self):
        return sorted(self.__edges, key=lambda edge: edge[-1]) if self.__weighted else None

    def edgeAlreadyExists(self, edge):
        equals = lambda v, w: v == w
        for e in self.__edges:
            if equals(e[0], edge[0]) and equals(e[1], edge[1]): return True
            if equals(e[0], edge[1]) and equals(e[1], edge[0]) and self.__directed: return True
        return False

    def setVertex(self, vertex):
        if not self.__vertexIsValid(vertex): 
            raise TypeError('vertices must be identified by int or str')
        self.__vertices.append(vertex)
        self.__vertices = deepcopy(list(set(self.__vertices)))
        return True

    def setEdge(self, v, w, cost=None):
        '''
            set a edge tuple => (vertexV, vertexW, if weighted: cost )
            if directed: edge(vertexV, vertexW) != edge(vertexW, vertexV)
        '''
        if self.setVertex(v) and self.setVertex(w):
            if self.edgeAlreadyExists((v, w)): return
            cost = 0 if cost == None and self.__weighted else cost
            self.__edges.append( (v, w, cost) )

    # def dfs(self, vertex):
    #     if vertex in self.vertices:
    #         visited, visitedVertices = [False for x in range(len(self.vertices))], []

    #         def calc(vertex):
    #             visited[vertex] = True
    #             visitedVertices.append(vertex)
    #             for v in self.adjacentvertices(vertex):
    #                 if not visited[v]:
    #                     calc(v)
    #         calc(vertex)
    #         return visitedVertices
    #     else:
    #         return []

    # def reach(self, vertexOrigin, vertexDestiny):
    #     visited = self.dfs(vertexOrigin)
    #     return True if vertexDestiny in visited else False

    # def calculatemst(self):
    #     if not self.__weighted or self.__directed:
    #         return []
    #     else:
    #         # self.__freeMST()
    #         # UF = UnionFind(self.numvertices())
    #         # self.__sortEdgesByCost()

    #         for edge in self.edges:
    #             vertexV = UF.find(edge[0])
    #             vertexW = UF.find(edge[1])
    #             if vertexV != vertexW:
    #                 UF.union(vertexV, vertexW)
    #                 self.mst.append(edge)
    #                 self.mstcost += edge[-1]

    #     return self.mst