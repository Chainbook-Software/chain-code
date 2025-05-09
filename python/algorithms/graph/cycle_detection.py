# graph_project/algorithms/cycle_detection.py

def _is_cyclic_util_directed(graph, vertex, visited, recursion_stack):
    visited.add(vertex)
    recursion_stack.add(vertex)

    for neighbor, weight in graph.get_neighbors(vertex):
        if neighbor not in visited:
            if _is_cyclic_util_directed(graph, neighbor, visited, recursion_stack):
                return True
        elif neighbor in recursion_stack: # Found a back edge
            return True
    
    recursion_stack.remove(vertex) # Backtrack
    return False

def has_cycle_directed(graph):
    """
    Checks if a directed graph has a cycle using DFS.

    Args:
        graph (Graph): A directed Graph instance.

    Returns:
        bool: True if the graph contains a cycle, False otherwise.
    """
    if not graph._directed:
        # print("Warning: This cycle detection is for directed graphs. For undirected, use has_cycle_undirected.")
        # Or raise error: raise TypeError("Use has_cycle_undirected for undirected graphs.")
        # For now, let's proceed but note it's primarily for directed.
        pass

    visited = set()
    recursion_stack = set()
    for vertex in graph.get_all_vertices():
        if vertex not in visited:
            if _is_cyclic_util_directed(graph, vertex, visited, recursion_stack):
                return True
    return False


def _is_cyclic_util_undirected(graph, vertex, visited, parent):
    visited.add(vertex)

    for neighbor, weight in graph.get_neighbors(vertex):
        if neighbor not in visited:
            if _is_cyclic_util_undirected(graph, neighbor, visited, vertex):
                return True
        elif neighbor != parent: # Visited and not parent means a back edge
            return True
    return False

def has_cycle_undirected(graph):
    """
    Checks if an undirected graph has a cycle using DFS.

    Args:
        graph (Graph): An undirected Graph instance.

    Returns:
        bool: True if the graph contains a cycle, False otherwise.
    """
    if graph._directed:
        raise TypeError("Use has_cycle_directed for directed graphs.")

    visited = set()
    for vertex in graph.get_all_vertices():
        if vertex not in visited:
            # For undirected graphs, parent is initially None or a marker
            if _is_cyclic_util_undirected(graph, vertex, visited, None):
                return True
    return False

def has_cycle(graph):
    """
    Generic cycle detection. Calls the appropriate specific function.
    """
    if graph._directed:
        return has_cycle_directed(graph)
    else:
        return has_cycle_undirected(graph)