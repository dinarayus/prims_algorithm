import heapq
mst = []
usedVertices = set()
with open("") as f:
    numVertices = int(f.readline())
    edges = [[] for _ in range(numVertices)]
    for line in f.readlines():
        edge = tuple(map(int, line.split("")))

