import heapq
import networkx as nx
import matplotlib.pyplot as plt

class FoodDeliveryRoutePlanner:
    def __init__(self):
        self.graph = nx.DiGraph()
    
    def add_road(self, start, end, travel_time):
        """Adds a road between two locations with a given travel time."""
        self.graph.add_edge(start, end, weight=travel_time)
        self.graph.add_edge(end, start, weight=travel_time)  # Assuming two-way roads
    
    def dijkstra(self, start, target):
        """Finds the shortest path using Dijkstra's algorithm."""
        priority_queue = [(0, start)]
        shortest_paths = {node: float('inf') for node in self.graph.nodes}
        shortest_paths[start] = 0
        predecessors = {}
        
        while priority_queue:
            current_time, current_location = heapq.heappop(priority_queue)
            
            if current_location == target:
                break
            
            for neighbor in self.graph.neighbors(current_location):
                travel_time = self.graph[current_location][neighbor]['weight']
                new_time = current_time + travel_time
                
                if new_time < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = new_time
                    heapq.heappush(priority_queue, (new_time, neighbor))
                    predecessors[neighbor] = current_location
        
        path = []
        node = target
        while node in predecessors:
            path.insert(0, node)
            node = predecessors[node]
        
        if path:
            path.insert(0, start)
        
        return path, shortest_paths[target]
    
    def visualize_graph(self):
        """Displays the current road network."""
        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_size=700, node_color='lightblue')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.show()

# Example Usage
if __name__ == "__main__":
    planner = FoodDeliveryRoutePlanner()
    planner.add_road("A", "B", 5)
    planner.add_road("A", "C", 10)
    planner.add_road("B", "C", 2)
    planner.add_road("C", "D", 7)
    planner.add_road("B", "D", 8)
    
    planner.visualize_graph()
    
    start, target = "A", "D"
    path, time = planner.dijkstra(start, target)
    print(f"Shortest path from {start} to {target}: {path} with travel time: {time}")
