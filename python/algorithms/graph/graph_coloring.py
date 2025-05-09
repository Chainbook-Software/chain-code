def graph_coloring(graph):
    """
    Implements the Greedy Graph Coloring algorithm to color the vertices of a graph.
    Ensures no two adjacent vertices have the same color.

    Args:
        graph (Graph): An instance of the Graph class.

    Returns:
        dict: A dictionary mapping each vertex to its assigned color.
    """
    vertices = graph.get_all_vertices()
    if not vertices:
        return {}

    # Dictionary to store the color assigned to each vertex
    color_assignment = {}

    # Assign the first color to the first vertex
    color_assignment[vertices[0]] = 0

    # Loop through the remaining vertices
    for vertex in vertices[1:]:
        # Get colors of adjacent vertices
        adjacent_colors = set()
        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor in color_assignment:
                adjacent_colors.add(color_assignment[neighbor])

        # Find the smallest available color
        color = 0
        while color in adjacent_colors:
            color += 1

        # Assign the chosen color to the current vertex
        color_assignment[vertex] = color

    return color_assignment


def print_coloring(color_assignment):
    """
    Prints the vertex color assignments in a readable format.

    Args:
        color_assignment (dict): Dictionary mapping vertices to their colors.
    """
    for vertex, color in color_assignment.items():
        print(f"Vertex {vertex} -> Color {color}")
