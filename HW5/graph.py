
vertexDict = {}
pathList = []
cutList = []

def dfs(graph, root):
    visited = [False] * len(graph)
    for v in range(0, len(visited)):
        vertexDict[v] = []
    path = []
    # put root vertex in stack
    stack = [root]
    # set root vertex to visited
    visited[stack[0]] = True

    vertex = stack.pop(len(stack) - 1)
    # print("vertex: {}".format(vertex))
    # print("vertex2:", graph[2])
    path.append(vertex)
    while True:
        # iterate over vertexes
        for neighbor in range(0, len(visited)):
            # check route to vertex
            # print("vertex: {}, neighbor: {}, visited[neighbor]: {}".format(vertex, neighbor, visited[neighbor]))
            if graph[vertex][neighbor] == 1 and visited[neighbor] == False:
                # visit vertex
                visited[neighbor] = True

                # push the vertex to stack
                # print("Pushing ", neighbor, " to the stack.")
                stack.append(neighbor)
                vertexDict[vertex].append(neighbor)
            # print("Current Path: {}".format(path))
        if len(stack) == 0:
            break
        else:
            #print()
            vertex = stack.pop(len(stack) - 1)
            # print("vertex:", vertex)
            path.append(vertex)
            #print("Current Path: {}".format(path))
    # print(visited)
    #print("Current Path: {}".format(path))
    # print("bfsVD: {}".format(vertexDict))
    return vertexDict

# doesn't work if the graph is linear
def bruteForce(graph):
    initCutList(graph)
    for v in range(0, len(graph)):
        tempDict = dfs(graph, v)
        # print("td: {}".format(tempDict))
        for key, value in tempDict.items():
            if len(value) < 2 and key in cutList:
                cutList.remove(key)
        # print("bfPL: {}".format(pathList))
    print("Cut Vertices: {}".format(cutList))

def initCutList(g):
    for v in range(0, len(g)):
        cutList.append(v)
    # print("iCL: {}".format(cutList))

def rdfs(graph, root):
    return