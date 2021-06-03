class UnionFind():
    def __init__(self, vertices):
        self.boss = [x for x in range(vertices)]
        self.size = [1 for x in range(vertices)]

    def find(self, vertex):
        copyV = vertex
        while copyV != self.boss[copyV]:
            copyV = self.boss[copyV]
        return copyV

    def union(self, vertexV, vertexW):
        if self.size[vertexV] < self.size[vertexW]:
            self.boss[vertexV] = vertexW
            self.size[vertexW] += self.size[vertexV]
        else:
            self.boss[vertexW] = vertexV
            self.size[vertexV] += self.size[vertexW]