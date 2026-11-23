def find_eulerian_path(graph: dict[str, list[str]]) -> list[str]:
    """
    Finds an Eulerian path in a De Brujin multigraph using DFS with backtracking.
    
    Arguments:
    ----------
        graph: `dict[, str, list[str]]`. The adjacency list of the De Brujin graph we are interested in finding a path through.

    Returns:
    --------
        result: `list[str]`

    * **Algorithm**: Starting from a node, we follow an unused edge to a neighboring node. We continute traversing the graph
    unitl every edge has been visited. If we reach a dead end prematurely, we backtrack and try another
    route.\n

    * **TRADEOFFS**: This naive approach, while simple to understand, is extremely inefficient and has, in the worst-case, O(N!) 
    runtime complexity since so many edge orderings are explored. As this is a toy example, it does not matter here, but in a 
    production implementation, we may look into implementing [Hierholzer's algorithm]("https://en.wikipedia.org/wiki/Eulerian_path#Hierholzer's_algorithm")
    """

    #define total number of edges to track
    total_edges = sum(len(neighbors) for neighbors in graph.values())

    def depth_first_search(current_edge, path, used_edges):
        """
        Recursive DFS used to build the Eulerian path.
        """

        #base case - check if all edges have been traversed
        if len(used_edges) == total_edges:
            return path.copy()

        #explore each outgoing edge on the graph
        for i, neighbor in enumerate(graph[current_edge]):

            #We identify each edge by source node and it's associated index
            #This is important in De Brujin multigraphs since two identical k-mers can generate
            #two distinct edges.
            edge = (current_edge, i)

            if edge in used_edges:      #pass over edges we have already traversed
                continue

            used_edges.add(edge)
            path.append(neighbor)

            #recursive call with updated parameters
            result = depth_first_search(neighbor, path, used_edges)

            if result is not None:
                return result

            #backtracking if path does not work
            path.pop()
            used_edges.remove(edge)

        return None

    #trying each node that has outgoing edges as a starting point
    for start in graph:
        if graph[start]:
            result = depth_first_search(start, [start], set())

            if result is not None:
                return result
    
    return []