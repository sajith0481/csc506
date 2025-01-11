import networkx as nx
import matplotlib.pyplot as plt
import time

# Function to generate a weighted graph
def generate_graph(num_nodes, density=0.5, allow_negative_weights=False):
    G = nx.gnp_random_graph(num_nodes, density, directed=True)
    for (u, v) in G.edges():
        weight = round((10 * density) * (1 if not allow_negative_weights else (-1)**(u + v)), 2)
        G[u][v]['weight'] = weight
    return G

# Dijkstra's Algorithm Implementation
def dijkstra_shortest_path(graph, source):
    return nx.single_source_dijkstra_path_length(graph, source, weight='weight')

# Bellman-Ford Algorithm Implementation
def bellman_ford_shortest_path(graph, source):
    try:
        length = nx.single_source_bellman_ford_path_length(graph, source, weight='weight')
        return length
    except nx.NetworkXUnbounded:
        print("Graph contains a negative weight cycle.")
        return {}

# Function to visualize the graph
def visualize_graph(graph, shortest_path=None):
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color='lightblue')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    if shortest_path:
        nx.draw_networkx_edges(
            graph, pos,
            edgelist=shortest_path,
            edge_color='red',
            width=2
        )
    plt.show()

# Main testing block
if __name__ == "__main__":
    # Parameters
    num_nodes = 6
    density = 0.6
    start_node = 0

    # Generate graph without negative weights for Dijkstra's algorithm
    test_graph_no_negatives = generate_graph(num_nodes, density=density, allow_negative_weights=False)

    # Generate graph with negative weights for Bellman-Ford algorithm
    test_graph_with_negatives = generate_graph(num_nodes, density=density, allow_negative_weights=True)

    # Visualize the graph without negative weights for Dijkstra
    print("Graph for Dijkstra's Algorithm:")
    visualize_graph(test_graph_no_negatives)

    # Test Dijkstra's Algorithm
    print("\nDijkstra's Algorithm Results:")
    try:
        dijkstra_result = dijkstra_shortest_path(test_graph_no_negatives, start_node)
        print("Shortest Paths:", dijkstra_result)
    except ValueError as e:
        print(f"Dijkstra's algorithm failed: {e}")

    # Visualize the graph with negative weights for Bellman-Ford
    print("\nGraph for Bellman-Ford Algorithm:")
    visualize_graph(test_graph_with_negatives)

    # Test Bellman-Ford Algorithm
    print("\nBellman-Ford Algorithm Results:")
    try:
        bellman_ford_result = bellman_ford_shortest_path(test_graph_with_negatives, start_node)
        print("Shortest Paths:", bellman_ford_result)
    except ValueError as e:
        print(f"Bellman-Ford algorithm failed: {e}")
