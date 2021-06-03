from mygraphtools import Graph


g = Graph(directed=True, weighted=True, connected=True)

g.setEdge(1, 2, 10)
g.setEdge(1, 3, 30)
g.setEdge(3, 4, 213)
g.setEdge(3, 211, 1.1)

print(g.getEdgesSortedByCost())