import googlemaps
from collections import deque

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
API_KEY = '...'
gmaps = googlemaps.Client(key=API_KEY)

# List of counties to visit (include country for accuracy)
counties = ['Nairobi, Kenya', 'Nakuru, Kenya', 'Nandi, Kenya', 'Nyeri, Kenya', 'Meru, Kenya', 'Laikipia, Kenya']

def get_distance_matrix(origins, destinations):
    """Fetches the distance matrix from Google Maps API."""
    result = gmaps.distance_matrix(origins, destinations, mode='driving')
    distance_matrix = {}
    for i, origin in enumerate(origins):
        distance_matrix[origin] = {}
        for j, destination in enumerate(destinations):
            if origin == destination:
                distance_matrix[origin][destination] = 0
            else:
                try:
                    element = result['rows'][i]['elements'][j]
                    if element['status'] == 'OK':
                        distance_matrix[origin][destination] = element['distance']['value'] / 1000  # convert meters to kilometers
                    else:
                        print(f"Error finding distance between {origin} and {destination}: {element['status']}")
                        distance_matrix[origin][destination] = float('inf')
                except KeyError as e:
                    print(f"KeyError {e} for distance between {origin} and {destination}")
                    distance_matrix[origin][destination] = float('inf')
    return distance_matrix

# Fetch live distance data
origins = counties
destinations = counties
distances = get_distance_matrix(origins, destinations)

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
optimal_route, min_distance = bfs_shortest_route('Nairobi, Kenya', counties, distances)

# Print the optimal route and distance
if optimal_route:
    print("The optimal route is:")
    for county in optimal_route:
        print(f"- {county}")
    
    print(f"\nTotal distance: {min_distance} km\n")    
    
    # Create a Google Maps URL for the route
    base_url = "https://www.google.com/maps/dir/"
    route_str = "/".join([county.split(',')[0] for county in optimal_route])
    maps_url = base_url + route_str
    print("Google Maps URL:", maps_url)
else:
    print("No optimal route found. Check API availability and input data.")
