import osmnx as ox # type: ignore
ox.config(use_cache=True, log_console=True, max_query_area_size=50 * 1000 * 50 * 1000)  # Increase the max query area size

import networkx as nx # type: ignore
import matplotlib.pyplot as plt # type: ignore
from itertools import permutations

# List of counties including Nairobi as the final destination
counties = {
    'Nyeri': (0.4167, 36.9500),
    'Nakuru': (0.2833, 36.0667),
    'Laikipia': (0.3600, 37.0333),
    'Nandi': (0.1750, 35.1260),
    'Meru': (0.0463, 37.6525),
    'Nairobi': (-1.286389, 36.817223)
}

def get_distance_matrix(counties):
    distances = {}
    for origin in counties:
        for destination in counties:
            if origin != destination:
                orig_coords = counties[origin]
                dest_coords = counties[destination]
                G = ox.graph_from_point(orig_coords, dist=50000, network_type='drive')
                orig_node = ox.distance.nearest_nodes(G, orig_coords[1], orig_coords[0])
                dest_node = ox.distance.nearest_nodes(G, dest_coords[1], dest_coords[0])
                distance = nx.shortest_path_length(G, orig_node, dest_node, weight='length') / 1000  # convert meters to kilometers
                distances[(origin, destination)] = distance
    return distances

distances = get_distance_matrix(counties)

def calculate_total_distance(permutation, distances):
    total_distance = 0
    for i in range(len(permutation) - 1):
        total_distance += distances.get((permutation[i], permutation[i + 1]), distances.get((permutation[i + 1], permutation[i])))
    return total_distance

def find_optimal_path(counties, distances):
    shortest_path = None
    min_distance = float('inf')
    for permutation in permutations(list(counties.keys())[:-1]):  # Exclude Nairobi from permutations
        current_distance = calculate_total_distance(permutation + ('Nairobi',), distances)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_path = permutation + ('Nairobi',)
    return shortest_path, min_distance

optimal_path, min_distance = find_optimal_path(counties, distances)
print(f"Optimal Path: {' -> '.join(optimal_path)}")
print(f"Minimum Distance: {min_distance} km")

def visualize_path(optimal_path, distances):
    G = nx.Graph()

    # Add nodes
    for county in counties:
        G.add_node(county)

    # Add edges with distances
    for (county1, county2), distance in distances.items():
        G.add_edge(county1, county2, weight=distance)

    pos = nx.spring_layout(G)

    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=15, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    path_edges = [(optimal_path[i], optimal_path[i + 1]) for i in range(len(optimal_path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

    plt.title(f"Optimal Path: {' -> '.join(optimal_path)} (Total Distance: {min_distance} km)")
    plt.show()

visualize_path(optimal_path, distances)
