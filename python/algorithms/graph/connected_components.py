# graph_project/algorithms/connected_components.py
from .dfs import dfs_recursive_util # Can use DFS or BFS for traversal

def get_connected_components(graph):
    """
    Finds all connected components in an undirected graph.
    Each component is a set of vertices.

    Args:
        graph (Graph): An undirected Graph instance.

    Returns:
        list: A list of sets, where each set contains the vertices
              of a connected component.
        Returns an empty list if the graph is empty.
        Raises TypeError if the graph is directed.
    """
    if graph._directed:
        raise TypeError("Connected components are typically defined for undirected graphs. "
                        "For directed graphs, consider 'strongly connected components'.")

    if not graph.get_all_vertices():
        return []

    visited = set()
    components = []

    for vertex in graph.get_all_vertices():
        if vertex not in visited:
            component = []
            # Use a traversal (like DFS) to find all reachable nodes
            # We can reuse parts of DFS or implement a simple traversal here
            
            # Simple DFS-like traversal for component finding:
            current_component_nodes = []
            # Using a utility from dfs.py (make sure dfs.py has dfs_recursive_util or adapt)
            # For simplicity, let's write a small traversal here:
            q = [vertex]
            comp_visited_locally = {vertex}
            
            while q:
                curr = q.pop(0) # BFS-like for component finding
                current_component_nodes.append(curr)
                visited.add(curr)
                for neighbor, _ in graph.get_neighbors(curr):
                    if neighbor not in comp_visited_locally:
                        comp_visited_locally.add(neighbor)
                        q.append(neighbor)
            
            components.append(set(current_component_nodes))
            
    return components