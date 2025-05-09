# graph_project/algorithms/dfs.py

def dfs(graph, start_vertex):
    """
    Performs a Depth-First Search on the graph starting from start_vertex.
    This is an iterative version using a stack.

    Args:
        graph (Graph): An instance of the Graph class.
        start_vertex: The vertex to start the DFS from.

    Returns:
        A list of vertices in the order they were visited (one possible DFS order).
        Returns an empty list if the start_vertex is not in the graph.
    """
    if start_vertex not in graph.get_all_vertices():
        return []

    visited = set()
    stack = [start_vertex]
    order_visited = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            order_visited.append(vertex)
            # Add neighbors to stack (in reverse order to process them "left-to-right" typically)
            # Neighbors are tuples (neighbor, weight)
            for neighbor, weight in reversed(graph.get_neighbors(vertex)):
                if neighbor not in visited:
                    stack.append(neighbor)
    return order_visited

def dfs_recursive_util(graph, vertex, visited, path):
    visited.add(vertex)
    path.append(vertex)
    for neighbor, weight in graph.get_neighbors(vertex):
        if neighbor not in visited:
            dfs_recursive_util(graph, neighbor, visited, path)

def dfs_recursive(graph, start_vertex):
    """
    Performs a Depth-First Search on the graph starting from start_vertex (recursive).

    Args:
        graph (Graph): An instance of the Graph class.
        start_vertex: The vertex to start the DFS from.

    Returns:
        A list of vertices in one possible DFS traversal order.
    """
    if start_vertex not in graph.get_all_vertices():
        return []
    
    visited = set()
    path = []
    dfs_recursive_util(graph, start_vertex, visited, path)
    return path