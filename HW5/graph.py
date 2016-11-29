

def dfs(graph, root):
    visited = [False] * len(graph)

    # put root vertex in stack
    stack = [root]
    # set root vertex to visited
    visited[stack[0]] = True

    vertex = stack.pop(len(stack) - 1)
    print("vertex: {}".format(vertex))
    # print("vertex2:", graph[2])

    while True:
        # iterate over vertexes
        for neighbor in range(0, len(visited)):
            # check route to vertex
            print("vertex: {}, neighbor: {}, visited[neighbor]: {}".format(vertex, neighbor, visited[neighbor]))
            if graph[vertex][neighbor] == 1 and visited[neighbor] == False:
                # visit vertex
                visited[neighbor] = True

                # push the vertex to stack
                print("Pushing ", neighbor, " to the stack.")
                stack.append(neighbor)
        if len(stack) == 0:
            break
        else:
            print()
            vertex = stack.pop(len(stack) - 1)
            print("vertex:", vertex)
    print(visited)