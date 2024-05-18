"""
Algoritmo de Tarjan (AP)

"""
from sys import stdin

def ap(graph):
    visited = {i : False for i in graph}
    low = {i : -1 for i in graph}
    p = {i : -1 for i in graph}
    apNodes = set()
    for i in graph:
        low[i] = visited[i] = p[i] = -1
    t = 0
    for i in graph:
        if visited[i] == -1:
            apAux(i, graph, visited, low, p, apNodes, t)
    return apNodes
            

def apAux(v, G, visited, low, p, apNodes, t):
    num = 0
    t += 1
    visited[v] = low[v] = t

    for w in G[v]:
        if visited[w] == -1:
            num += 1
            p[w] = v
            apAux(w, G, visited, low, p, apNodes, t)
            low[v] = min(low[v], low[w])

            #verificar si es un punto de articulacion
            if p[v] != -1 and low[w] >= visited[v]:
                apNodes.add(v)
                
        elif w != p[v]:
            low[v] = min(low[v], visited[w])

    if p[v] == -1 and num > 1:
        apNodes.add(v)
    

def inDegreAP(artiPoints, graph):
    ans = {i : 0 for i in artiPoints}
    for v in graph:
        for u in graph[v]:
            if u in artiPoints:
                ans[u] += 1
    return ans



def main():
    G = {}
    undirectedG = {}
    key = stdin.readline().strip()
    while key != "":
        lst = key.split()
        adj = lst[1:]
        u = lst[0]
        G[u] = adj
        for v in adj:
            if v not in undirectedG:
                undirectedG[v] = []
            if u not in undirectedG:
                undirectedG[u] = []
            undirectedG[v].append(u)
            undirectedG[u].append(v)
        
        key = stdin.readline().strip()

    


    apNodes = ap(undirectedG)

    if len(apNodes) == 0:
        print("No hay puntos de articulacion")
    else:
        print("Puntos de Articulacion:")
        print(*apNodes)
        inDegree = inDegreAP(apNodes, undirectedG)
        print("Seguidores")
        inDegree = dict(sorted(inDegree.items(), key=lambda item: item[1], reverse=True))
        for i in inDegree:
            print("Influencer %s, tiene %d seguidores" % (str(i), inDegree[i]))

main()