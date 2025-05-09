# graph_project/graph_definition.py

class Graph:
    """
    A graph data structure implemented using an adjacency list.
    Supports both directed and undirected graphs, and weighted edges.
    """

    def __init__(self, directed=False):
        """
        Initializes the graph.

        Args:
            directed (bool): If True, the graph is directed.
                             If False (default), the graph is undirected.
        """
        self._graph = {}  # Vertex: [(neighbor, weight), ...]
        self._directed = directed

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph if it doesn't already exist.

        Args:
            vertex: The vertex to be added.
        """
        if vertex not in self._graph:
            self._graph[vertex] = []

    def add_edge(self, vertex1, vertex2, weight=1):
        """
        Adds an edge between vertex1 and vertex2.
        If the vertices do not exist, they are added.

        Args:
            vertex1: The first vertex.
            vertex2: The second vertex.
            weight (int/float): The weight of the edge (default is 1).
        """
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Add edge from vertex1 to vertex2
        # Avoid adding duplicate edges; you might want to update weight if it exists
        # For this implementation, we simply add if not present by neighbor name
        v1_neighbors = [n for n, w in self._graph[vertex1]]
        if vertex2 not in v1_neighbors:
            self._graph[vertex1].append((vertex2, weight))
        # else:
        #     print(f"Edge from {vertex1} to {vertex2} already exists or use update_edge_weight.")


        if not self._directed:
            # If undirected, add an edge back from vertex2 to vertex1
            v2_neighbors = [n for n, w in self._graph[vertex2]]
            if vertex1 not in v2_neighbors:
                self._graph[vertex2].append((vertex1, weight))
            # else:
            #     print(f"Edge from {vertex2} to {vertex1} already exists or use update_edge_weight.")


    def get_neighbors(self, vertex):
        """
        Gets the neighbors of a given vertex along with edge weights.

        Args:
            vertex: The vertex whose neighbors are to be retrieved.

        Returns:
            A list of (neighbor, weight) tuples, or an empty list if the
            vertex is not in the graph or has no neighbors.
        """
        return self._graph.get(vertex, [])

    def get_all_vertices(self):
        """
        Returns a list of all vertices in the graph.
        """
        return list(self._graph.keys())

    def get_all_edges(self):
        """
        Returns a list of all edges in the graph.
        Each edge is represented as a tuple (vertex1, vertex2, weight).
        For undirected graphs, edges are listed once based on internal representation.
        """
        edges = []
        visited_undirected_edges = set() # To avoid duplicate edges in undirected graph output

        for vertex, neighbors in self._graph.items():
            for neighbor, weight in neighbors:
                if self._directed:
                    edges.append((vertex, neighbor, weight))
                else:
                    # For undirected, add edge only if not already added in reverse
                    if (neighbor, vertex) not in visited_undirected_edges:
                        edges.append((vertex, neighbor, weight))
                        visited_undirected_edges.add((vertex, neighbor))
        return edges


    def __str__(self):
        """
        String representation of the graph.
        """
        output = f"{'Directed' if self._directed else 'Undirected'} Graph:\n"
        if not self._graph:
            return output + " (empty)"
        for vertex, neighbors in self._graph.items():
            if neighbors:
                neighbor_str = ", ".join([f"{n}({w})" for n, w in neighbors])
            else:
                neighbor_str = "(no outgoing edges)"
            output += f"  {vertex}: {neighbor_str}\n"
        return output