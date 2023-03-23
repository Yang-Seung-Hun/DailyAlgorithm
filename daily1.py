from typing import List


def union(v1,v2,uf):
    fa = find(v1, uf)
    fb = find(v2, uf)
    if fa != fb:
        uf[fa] = fb


def find(v, uf):
    if v == uf[v] :
        return v
    else:
        uf[v] = find(uf[v], uf)
        return uf[v]


def makeConnected(n: int, connections: List[List[int]]) -> int:
    uf = list(range(n))

    if len(connections) < n-1:
        return -1

    for connection in connections:
        v1 = connection[0]
        v2 = connection[1]
        union(v1, v2, uf)

    groups = set()
    for i in range(n):
        group = find(i, uf)
        groups.add(group)
    return len(groups) - 1


# links = [[0,1],[0,2],[1,2]]
# num = 4

# links = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# num = 6

links = [[0,1],[0,2],[0,3],[1,2]]
num = 6

print(makeConnected(num, links))
