# graph_project/algorithms/bfs.py
from collections import deque

def bfs(graph, start_vertex):
    """
    Performs a Breadth-First Search on the graph starting from start_vertex.

    Args:
        graph (Graph): An instance of the Graph class.
        start_vertex: The vertex to start the BFS from.

    Returns:
        A list of vertices in the order they were visited.
        Returns an empty list if the start_vertex is not in the graph.
    """
    if start_vertex not in graph.get_all_vertices():
        return []

    visited = set()
    queue = deque([start_vertex])
    order_visited = []

    visited.add(start_vertex)

    while queue:
        current_vertex = queue.popleft()
        order_visited.append(current_vertex)

        # Neighbors are tuples (neighbor, weight)
        for neighbor, weight in graph.get_neighbors(current_vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return order_visited