from data import nodes, edges

def dijkstra(nodes, edges, source):
    nonVisited = []
    distances = {}
    for n in nodes:
        if n == source:
            distances[n] = 0
        else:
            distances[n] = 1e9

        nonVisited.append(n)

    while len(nonVisited):
        # choose a node that has smallest distances for examination
        chosenNode = nonVisited[0]
        chosenDistance = distances[chosenNode]
        chosenIndex = 0
        for i, n in enumerate(nonVisited):
            if distances[n] < chosenDistance:
                chosenDistance = distances[n]
                chosenNode = n
                chosenIndex = i

        # remove that node from the non-visited
        nonVisited = nonVisited[:chosenIndex] + nonVisited[chosenIndex + 1:]
        for neighbors in edges[chosenNode]:
            if neighbors[0] in nonVisited:
                distances[neighbors[0]] = min(distances[neighbors[0]], distances[chosenNode] + neighbors[1])
            
    return distances
dists = {}
for n in nodes:
    dists[n] = dijkstra(nodes, edges, n)

# print(dists)
print(dists['b']['c'])