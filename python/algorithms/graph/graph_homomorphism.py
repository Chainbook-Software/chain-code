def is_homomorphism(graph1, graph2, mapping):
    """
    Checks if a given vertex mapping defines a graph homomorphism from graph1 to graph2.

    Args:
        graph1 (Graph): The source graph.
        graph2 (Graph): The target graph.
        mapping (dict): A dictionary representing the vertex mapping from graph1 to graph2.

    Returns:
        bool: True if the mapping is a homomorphism, False otherwise.
    """
    for vertex1 in graph1.get_all_vertices():
        # Ensure vertex1 is in the mapping
        if vertex1 not in mapping:
            print(f"Vertex {vertex1} not found in mapping.")
            return False

        mapped_vertex1 = mapping[vertex1]

        # Check neighbors of vertex1 in graph1
        for neighbor, _ in graph1.get_neighbors(vertex1):
            # Ensure neighbor is mapped
            if neighbor not in mapping:
                print(f"Neighbor {neighbor} not found in mapping.")
                return False

            mapped_neighbor = mapping[neighbor]

            # Check the mapped edge in graph2
            neighbors2 = [n for n, _ in graph2.get_neighbors(mapped_vertex1)]
            if mapped_neighbor not in neighbors2:
                print(f"Edge ({mapped_vertex1}, {mapped_neighbor}) not found in graph2.")
                return False

    return True


def print_homomorphism_result(result):
    """
    Prints whether the mapping defines a valid homomorphism.

    Args:
        result (bool): The result of the homomorphism check.
    """
    if result:
        print("The mapping is a valid graph homomorphism.")
    else:
        print("The mapping is NOT a valid graph homomorphism.")
