import heapq
import matplotlib.pyplot as plt
import networkx as nx

# Define the graph as an adjacency list
graph = {
    'Nairobi': {'Nyeri': 150, 'Nakuru': 160, 'Laikipia': 190, 'Nandi': 300, 'Meru': 250},
    'Nyeri': {'Nairobi': 150, 'Laikipia': 100, 'Meru': 120},
    'Nakuru': {'Nairobi': 160, 'Laikipia': 140, 'Nandi': 170},
    'Laikipia': {'Nairobi': 190, 'Nyeri': 100, 'Nakuru': 140, 'Meru': 90},
    'Nandi': {'Nairobi': 300, 'Nakuru': 170},
    'Meru': {'Nairobi': 250, 'Nyeri': 120, 'Laikipia': 90},
}

# Dijkstra's algorithm implementation
def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    shortest_path = {}
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                shortest_path[neighbor] = current_node
    
    return distances, shortest_path

# Find the shortest path from Nairobi to all other nodes
distances, shortest_path = dijkstra(graph, 'Nairobi')

# Function to reconstruct the path
def reconstruct_path(shortest_path, start, end):
    path = []
    while end:
        path.append(end)
        end = shortest_path.get(end)
    return path[::-1]

# Find the path from Nairobi to Nyeri
path = reconstruct_path(shortest_path, 'Nairobi', 'Nyeri')

# Print the path and distances
print("Shortest path from Nairobi to Nyeri:", path)
print("Distances:", distances)

# Visualization using NetworkX and Matplotlib
G = nx.Graph()

# Add nodes and edges to the graph
for node in graph:
    for neighbor, weight in graph[node].items():
        G.add_edge(node, neighbor, weight=weight)

pos = nx.spring_layout(G)  # positions for all nodes
edge_labels = {(u, v): f'{d["weight"]}' for u, v, d in G.edges(data=True)}

plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=15, font_weight='bold', edge_color='gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange')

plt.title("Shortest Path from Nairobi to Nyeri")
plt.show()
