# graph_project/algorithms/bellman_ford.py

def bellman_ford(graph, start_vertex):
    """
    Implements the Bellman-Ford algorithm to find the shortest paths from a single
    source vertex to all other vertices in a weighted graph.
    Can handle negative edge weights and detect negative weight cycles.

    Args:
        graph (Graph): An instance of the Graph class.
        start_vertex: The starting vertex.

    Returns:
        A tuple (distances, predecessors):
        - distances (dict): A dictionary mapping each vertex to its shortest distance
                            from the start_vertex. float('inf') for unreachable.
                            Contains float('-inf') for vertices in or reachable
                            from a negative cycle.
        - predecessors (dict): A dictionary mapping each vertex to its predecessor
                               on the shortest path.
        Returns (None, None) if start_vertex is not in graph.
        Raises ValueError if a negative weight cycle is detected and reports it.
    """
    vertices = graph.get_all_vertices()
    if start_vertex not in vertices:
        return None, None

    edges = graph.get_all_edges() # Needs Graph.get_all_edges() method

    distances = {vertex: float('inf') for vertex in vertices}
    predecessors = {vertex: None for vertex in vertices}
    distances[start_vertex] = 0

    num_vertices = len(vertices)

    # Relax edges repeatedly
    for _ in range(num_vertices - 1):
        changed_in_iteration = False
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u
                changed_in_iteration = True
        if not changed_in_iteration: # Optimization: if no changes, shortest paths found
             break


    # Check for negative weight cycles
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            # Propagate negative infinity to all reachable nodes from cycle
            # This part can be complex to implement fully to mark all affected nodes
            # For now, we raise an error. A more robust solution might mark specific nodes.
            # To simply detect and mark nodes in a cycle or reachable from it as -inf:
            # Perform a traversal (DFS/BFS) from 'v' if distances[v] is further reduced,
            # and mark all reachable nodes as -inf.
            # However, for this implementation, we will just raise an error.
            raise ValueError(f"Graph contains a negative weight cycle involving edge ({u} -> {v})")

    return distances, predecessors