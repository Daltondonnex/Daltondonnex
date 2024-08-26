# Distance matrix between the counties
from collections import deque


distances = {
    'Nairobi': {'Nakuru': 161, 'Nandi': 313, 'Nyeri': 151, 'Meru': 228, 'Laikipia': 264},
    'Nakuru': {'Nairobi': 161, 'Nandi': 156, 'Nyeri': 167, 'Meru': 256, 'Laikipia': 214},
    'Nandi': {'Nairobi': 313, 'Nakuru': 156, 'Nyeri': 329, 'Meru': 409, 'Laikipia': 367},
    'Nyeri': {'Nairobi': 151, 'Nakuru': 167, 'Nandi': 329, 'Meru': 137, 'Laikipia': 126},
    'Meru': {'Nairobi': 228, 'Nakuru': 256, 'Nandi': 409, 'Nyeri': 137, 'Laikipia': 143},
    'Laikipia': {'Nairobi': 264, 'Nakuru': 214, 'Nandi': 367, 'Nyeri': 126, 'Meru': 143}
}

# List of counties to visit
counties = ['Nairobi', 'Nakuru', 'Nandi', 'Nyeri', 'Meru', 'Laikipia']

# Helper function to calculate the total distance of a given route
def calculate_route_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i+1]]
    return total_distance

# BFS algorithm to find the shortest route
def bfs_shortest_route(start, counties, distances):
    queue = deque([(start, [start], 0)])  # (current_node, path, distance)
    min_distance = float('inf')
    optimal_route = None
    all_counties_set = set(counties)
    
    while queue:
        current_node, path, current_distance = queue.popleft()
        
        # If all counties are visited, check the return to the start
        if set(path) == all_counties_set:
            total_distance = current_distance + distances[current_node][start]
            if total_distance < min_distance:
                min_distance = total_distance
                optimal_route = path + [start]
            continue
        
        # Visit the neighbors
        for neighbor in distances[current_node]:
            if neighbor not in path:
                new_distance = current_distance + distances[current_node][neighbor]
                queue.append((neighbor, path + [neighbor], new_distance))
    
    return optimal_route, min_distance

# Finding the optimal route using BFS
optimal_route, min_distance = bfs_shortest_route('Nairobi', counties, distances)

print(f"The optimal route is: {optimal_route} with a total distance of {min_distance}")
