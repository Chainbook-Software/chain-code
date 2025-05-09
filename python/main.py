# main.py
# Adjust imports based on the new directory structure

# Assuming graph_definition.py is inside datastructures/graph/
from datastructures.graph.graph import Graph

# Assuming algorithm files are inside algorithms/graph/
from algorithms.graph.bfs import bfs
from algorithms.graph.dfs import dfs, dfs_recursive
from algorithms.graph.dijkstra import dijkstra, get_shortest_path
from algorithms.graph.bellman_ford import bellman_ford
from algorithms.graph.cycle_detection import has_cycle # Assuming has_cycle is the generic one
from algorithms.graph.connected_components import get_connected_components
from algorithms.graph.graph_coloring import graph_coloring, print_coloring
from algorithms.graph.graph_homomorphism import is_homomorphism, print_homomorphism_result

if __name__ == "__main__":
    # --- Undirected Graph Example ---
    print("--- Undirected Graph Example ---")
    g_undirected = Graph() # From datastructures.graph.graph_definition
    g_undirected.add_vertex("A")
    g_undirected.add_vertex("B")
    g_undirected.add_edge("A", "B", 5) # A --5-- B
    g_undirected.add_edge("A", "C", 2) # A --2-- C
    g_undirected.add_edge("B", "C", 1) # B --1-- C
    g_undirected.add_edge("B", "D", 3) # B --3-- D
    g_undirected.add_edge("C", "D", 7) # C --7-- D
    g_undirected.add_edge("E", "F", 1) # E --1-- F (separate component)
    g_undirected.add_vertex("G")       # Isolated vertex

    print(g_undirected)

    print("\nBFS from A:", bfs(g_undirected, "A"))
    print("DFS (iterative) from A:", dfs(g_undirected, "A"))
    print("DFS (recursive) from A:", dfs_recursive(g_undirected, "A"))

    # Graph Coloring
    print("\nGraph Coloring:")
    color_assignment = graph_coloring(g_undirected)
    print_coloring(color_assignment)

    #Homomorphims
     # Graph Homomorphism Example
    print("\nGraph Homomorphism Test:")
    g2 = Graph()
    g2.add_edge("X", "Y", 1)
    g2.add_edge("Y", "Z", 1)
    g2.add_edge("X", "Z", 1)

    # Example vertex mapping from g_undirected to g2
    mapping = {"A": "X", "B": "Y", "C": "Z", "D": "X", "E": "Y", "F": "Z"}
    homomorphism_result = is_homomorphism(g_undirected, g2, mapping)
    print_homomorphism_result(homomorphism_result)

    distances_d, predecessors_d = dijkstra(g_undirected, "A")
    if distances_d:
        print("\nDijkstra from A:")
        for vertex, dist in distances_d.items():
            print(f"  Distance to {vertex}: {dist}")
            path = get_shortest_path(predecessors_d, "A", vertex)
            print(f"  Path: {' -> '.join(path) if path else 'N/A'}")
    
    print("\nHas cycle (undirected):", has_cycle(g_undirected))

    print("\nConnected Components (undirected):")
    components = get_connected_components(g_undirected)
    for i, comp in enumerate(components):
        print(f"  Component {i+1}: {sorted(list(comp))}")

    # --- Directed Graph Example ---
    print("\n\n--- Directed Graph Example ---")
    g_directed = Graph(directed=True)
    g_directed.add_edge("X", "Y", 3) # X --3--> Y
    g_directed.add_edge("Y", "Z", 4) # Y --4--> Z
    g_directed.add_edge("X", "Z", 10) # X --10--> Z
    g_directed.add_edge("Z", "X", 2) # Z --2--> X (creates a cycle)
    g_directed.add_edge("W", "X", 1) # W --1--> X

    print(g_directed)

    print("\nBFS from X (directed):", bfs(g_directed, "X"))
    print("DFS from X (directed):", dfs(g_directed, "X"))

    distances_d_dir, predecessors_d_dir = dijkstra(g_directed, "W")
    if distances_d_dir:
        print("\nDijkstra from W (directed):")
        for vertex, dist in distances_d_dir.items():
            print(f"  Distance to {vertex}: {dist}")
            path = get_shortest_path(predecessors_d_dir, "W", vertex)
            print(f"  Path: {' -> '.join(path) if path else 'N/A'}")

    print("\nHas cycle (directed):", has_cycle(g_directed))

    # Bellman-Ford Example
    print("\n\n--- Bellman-Ford Example (Directed Graph with Negative Weights) ---")
    g_bf = Graph(directed=True)
    g_bf.add_edge("S", "A", 4)
    g_bf.add_edge("S", "E", -2)
    g_bf.add_edge("A", "C", -3)
    g_bf.add_edge("C", "D", 1)
    g_bf.add_edge("D", "B", -1)
    g_bf.add_edge("B", "A", 1)
    g_bf.add_edge("E", "D", 2)
    g_bf.add_vertex("F")

    print(g_bf)
    try:
        distances_bf, predecessors_bf = bellman_ford(g_bf, "S")
        if distances_bf:
            print("\nBellman-Ford from S:")
            for vertex, dist in distances_bf.items():
                print(f"  Distance to {vertex}: {dist}")
                path_bf = get_shortest_path(predecessors_bf, "S", vertex)
                print(f"  Path: {' -> '.join(path_bf) if path_bf else 'N/A or unreachable'}")
    except ValueError as e:
        print(f"Bellman-Ford Error: {e}")

    # Bellman-Ford with Negative Cycle
    print("\n\n--- Bellman-Ford Example (Negative Cycle) ---")
    g_neg_cycle = Graph(directed=True)
    g_neg_cycle.add_edge("A", "B", 1)
    g_neg_cycle.add_edge("B", "C", 2)
    g_neg_cycle.add_edge("C", "A", -4)
    g_neg_cycle.add_edge("C", "D", 1)

    print(g_neg_cycle)
    try:
        bellman_ford(g_neg_cycle, "A")
    except ValueError as e:
        print(f"Bellman-Ford correctly detected error: {e}")

    print("\nBFS for non-existent vertex:", bfs(g_undirected, "Z_NOT_EXIST"))
    print("DFS for non-existent vertex:", dfs(g_undirected, "Z_NOT_EXIST"))