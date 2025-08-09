from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Graph:
    """
    Graph implementation using adjacency list representation.
    Supports weighted and unweighted graphs.
    """
    
    def __init__(self):
        """Initialize an empty graph."""
        self.adjacency_list = defaultdict(list)
        self.vertices = set()
    
    def add_vertex(self, vertex: str) -> None:
        """Add a vertex to the graph."""
        self.vertices.add(vertex)
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, from_vertex: str, to_vertex: str, weight: float = 1.0) -> None:
        """
        Add a weighted edge from from_vertex to to_vertex.
        
        Args:
            from_vertex: Starting vertex
            to_vertex: Ending vertex
            weight: Edge weight (default: 1.0)
        """
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        
        # Add edge with weight
        self.adjacency_list[from_vertex].append((to_vertex, weight))
        
        # For undirected graph, add reverse edge
        self.adjacency_list[to_vertex].append((from_vertex, weight))
    
    def get_neighbors(self, vertex: str) -> List[Tuple[str, float]]:
        """Get all neighbors of a vertex with their edge weights."""
        return self.adjacency_list.get(vertex, [])
    
    def get_vertices(self) -> Set[str]:
        """Get all vertices in the graph."""
        return self.vertices
    
    def bfs(self, start_vertex: str) -> List[str]:
        """
        Breadth-First Search to find all reachable vertices.
        
        Args:
            start_vertex: Starting vertex for BFS
            
        Returns:
            List of vertices in BFS order
        """
        if start_vertex not in self.vertices:
            return []
        
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        result = []
        
        while queue:
            current_vertex = queue.popleft()
            result.append(current_vertex)
            
            for neighbor, _ in self.get_neighbors(current_vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start_vertex: str) -> List[str]:
        """
        Depth-First Search to explore the graph.
        
        Args:
            start_vertex: Starting vertex for DFS
            
        Returns:
            List of vertices in DFS order
        """
        if start_vertex not in self.vertices:
            return []
        
        visited = set()
        result = []
        
        def dfs_recursive(vertex: str):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor, _ in self.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start_vertex)
        return result
    
    def dijkstra(self, start_vertex: str, end_vertex: str) -> Tuple[List[str], float]:
        """
        Dijkstra's algorithm to find shortest path between two vertices.
        
        Args:
            start_vertex: Starting vertex
            end_vertex: Target vertex
            
        Returns:
            Tuple of (shortest path as list of vertices, total distance)
        """
        if start_vertex not in self.vertices or end_vertex not in self.vertices:
            return [], float('inf')
        
        # Initialize distances and previous vertices
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start_vertex] = 0
        previous = {vertex: None for vertex in self.vertices}
        
        # Priority queue: (distance, vertex)
        pq = [(0, start_vertex)]
        visited = set()
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            
            # If we reached the target, we're done
            if current_vertex == end_vertex:
                break
            
            # Check all neighbors
            for neighbor, weight in self.get_neighbors(current_vertex):
                if neighbor in visited:
                    continue
                
                new_distance = current_distance + weight
                
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (new_distance, neighbor))
        
        # Reconstruct path
        if distances[end_vertex] == float('inf'):
            return [], float('inf')
        
        path = []
        current = end_vertex
        while current is not None:
            path.append(current)
            current = previous[current]
        
        path.reverse()
        return path, distances[end_vertex]
    
    def get_all_reachable_vertices(self, start_vertex: str) -> List[str]:
        """
        Get all vertices reachable from start_vertex using BFS.
        
        Args:
            start_vertex: Starting vertex
            
        Returns:
            List of all reachable vertices
        """
        return self.bfs(start_vertex)
    
    def is_connected(self) -> bool:
        """
        Check if the graph is connected (all vertices are reachable from any vertex).
        
        Returns:
            True if graph is connected, False otherwise
        """
        if not self.vertices:
            return True
        
        start_vertex = next(iter(self.vertices))
        reachable = set(self.bfs(start_vertex))
        return len(reachable) == len(self.vertices)
    
    def get_graph_info(self) -> Dict:
        """
        Get information about the graph.
        
        Returns:
            Dictionary with graph statistics
        """
        total_edges = sum(len(neighbors) for neighbors in self.adjacency_list.values()) // 2
        
        return {
            'vertices': len(self.vertices),
            'edges': total_edges,
            'connected': self.is_connected(),
            'vertex_list': list(self.vertices)
        }
    
    def find_all_paths(self, start_vertex: str, end_vertex: str, max_paths: int = 10) -> List[Tuple[List[str], float]]:
        """
        Find all possible paths from start_vertex to end_vertex using BFS.
        
        Args:
            start_vertex: Starting vertex
            end_vertex: Ending vertex
            max_paths: Maximum number of paths to find (default: 10)
            
        Returns:
            List of tuples (path, total_distance) sorted by distance
        """
        if start_vertex not in self.vertices or end_vertex not in self.vertices:
            return []
        
        if start_vertex == end_vertex:
            return [([start_vertex], 0.0)]
        
        paths = []
        queue = deque([(start_vertex, [start_vertex], 0.0)])  # (vertex, path, distance)
        
        while queue and len(paths) < max_paths:
            current, path, distance = queue.popleft()
            
            if current == end_vertex:
                paths.append((path[:], distance))
                continue
            
            # Explore all neighbors
            for neighbor, weight in self.get_neighbors(current):
                if neighbor not in path:  # Avoid cycles
                    new_path = path + [neighbor]
                    new_distance = distance + weight
                    queue.append((neighbor, new_path, new_distance))
        
        # Sort paths by total distance
        paths.sort(key=lambda x: x[1])
        return paths
