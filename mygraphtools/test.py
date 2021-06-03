from mygraphtools import Graph


g = Graph(directed=True, weighted=True, connected=True)

g.setEdge(1, 1, 10)
print(g.edgeAlreadyExists((1, 0)))
print(g.getVertices())
print(g.getEdges())