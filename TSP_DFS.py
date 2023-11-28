#tsp_dfs
import itertools

def euclidean_distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

def total_distance(path, cities):
    distance = 0
    for i in range(len(path) - 1):
        distance += euclidean_distance(cities[path[i]], cities[path[i+1]])
    distance += euclidean_distance(cities[path[-1]], cities[path[0]])
    return distance

def traveling_salesman_bruteforce(cities):
    num_cities = len(cities)
    min_distance = float('inf')
    best_path = []

    for path in itertools.permutations(range(num_cities)):
        distance = total_distance(path, cities)
        if distance < min_distance:
            min_distance = distance
            best_path = path

    return best_path, min_distance

if __name__ == "__main__":
    num_cities = int(input("Enter the number of cities: "))
    cities = []
    for i in range(num_cities):
        x, y = map(int, input(f"Enter coordinates for city {i+1} (x y): ").split())
        cities.append((x, y))
    
    best_path, min_distance = traveling_salesman_bruteforce(cities)
    print("Best Path:", best_path)
    print("Minimum Distance:", min_distance)