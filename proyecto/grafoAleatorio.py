import random

def generateDirectedGraph(nodes, percentage):
    lines = []
    lst = []
    numerosSel = []
    with open("names.txt", 'r') as file:
        lines = file.readlines()

    randomNum = random.randint(1, 999)
    i = 0
    while i < nodes:
        if randomNum not in numerosSel:
            numerosSel.append(randomNum)
            lst.append(lines[randomNum - 1].strip())
            i += 1
        randomNum = random.randint(1, 999)

    graph = {lst[i]: [] for i in range(nodes)}
    possibleArcs = nodes * (nodes - 1)
    numArcs = int(possibleArcs * percentage / 100)
    currentArcs = 0

    while currentArcs < numArcs:
        u = random.randint(0, nodes - 1)
        v = random.randint(0, nodes - 1)
        if u != v and lst[v] not in graph[lst[u]]:
            graph[lst[u]].append(lst[v])
            currentArcs += 1
    return graph

graph = generateDirectedGraph(900,0.5)

with open("graph.txt", 'w') as file:
    for key in graph:
        s = str(key) + " "
        for name in graph[key]:
            s += name
            s += " "
        s += "\n"
        file.write(s)
