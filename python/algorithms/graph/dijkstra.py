# graph_project/algorithms/dijkstra.py
import heapq

def dijkstra(graph, start_vertex):
    """
    Implements Dijkstra's algorithm to find the shortest paths from a single source
    to all other vertices in a weighted graph with non-negative edge weights.

    Args:
        graph (Graph): An instance of the Graph class. Edge weights must be non-negative.
        start_vertex: The starting vertex.

    Returns:
        A tuple (distances, predecessors):
        - distances (dict): A dictionary mapping each vertex to its shortest distance
                            from the start_vertex. Unreachable vertices will have float('inf').
        - predecessors (dict): A dictionary mapping each vertex to its predecessor
                               on the shortest path from the start_vertex.
        Returns (None, None) if start_vertex is not in graph.
    """
    if start_vertex not in graph.get_all_vertices():
        return None, None

    distances = {vertex: float('inf') for vertex in graph.get_all_vertices()}
    predecessors = {vertex: None for vertex in graph.get_all_vertices()}
    distances[start_vertex] = 0
    
    # Priority queue stores (distance, vertex)
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If we found a shorter path already, skip
        if current_distance > distances[current_vertex]:
            continue

        # Neighbors are (neighbor, weight)
        for neighbor, weight in graph.get_neighbors(current_vertex):
            if weight < 0:
                raise ValueError("Dijkstra's algorithm does not support negative edge weights.")
            
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances, predecessors

def get_shortest_path(predecessors, start_vertex, end_vertex):
    """
    Reconstructs the shortest path from start_vertex to end_vertex
    using the predecessors dictionary from Dijkstra's algorithm.
    """
    path = []
    current_vertex = end_vertex
    while current_vertex is not None and current_vertex in predecessors:
        path.append(current_vertex)
        if current_vertex == start_vertex:
            break
        current_vertex = predecessors[current_vertex]
    
    if not path or path[-1] != start_vertex: # Path not found or start not reached
        return [] 
    return path[::-1] # Reverse to get path from start to end