#tsp-bfs
import heapq

def euclidean_distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

def total_distance(path, cities):
    distance = 0
    for i in range(len(path) - 1):
        distance += euclidean_distance(cities[path[i]], cities[path[i+1]])
    distance += euclidean_distance(cities[path[-1]], cities[path[0]])
    return distance

def traveling_salesman_bfs(cities):
    num_cities = len(cities)
    start_city = 0
    initial_state = (start_city, [start_city], 0)
    
    priority_queue = [initial_state]
    
    while priority_queue:
        current_city, path, current_distance = heapq.heappop(priority_queue)
        
        if len(path) == num_cities:
            return path, current_distance
        
        for next_city in range(num_cities):
            if next_city not in path:
                new_distance = current_distance + euclidean_distance(cities[current_city], cities[next_city])
                new_path = path + [next_city]
                heapq.heappush(priority_queue, (next_city, new_path, new_distance))
    
    return None, None

if __name__ == "__main__":
    num_cities = int(input("Enter the number of cities: "))
    cities = []
    for i in range(num_cities):
        x, y = map(int, input(f"Enter coordinates for city {i+1} (x y): ").split())
        cities.append((x, y))
    
    best_path, min_distance = traveling_salesman_bfs(cities)
    if best_path is not None:
        print("Best Path:", best_path)
        print("Minimum Distance:", min_distance)
    else:
        print("No solution found.")