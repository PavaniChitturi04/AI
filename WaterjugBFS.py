#write a python program for water jug  problem using breadth first search
from collections import deque

class State:
    def __init__(self, x, y):
        self.x = x  # Current water amount in jug X
        self.y = y  # Current water amount in jug Y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

def water_jug_bfs(jug_x_capacity, jug_y_capacity, target_amount):
    visited = set()
    queue = deque([(State(0, 0), [])])  # Initialize queue with initial state and empty path

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue

        visited.add(current_state)

        if current_state.x == target_amount:
            path.append(current_state)
            return path

        # Fill jug X
        if current_state.x < jug_x_capacity:
            new_x = jug_x_capacity
            new_y = current_state.y
            if State(new_x, new_y) not in visited:
                queue.append((State(new_x, new_y), path + [current_state]))

        # Fill jug Y
        if current_state.y < jug_y_capacity:
            new_x = current_state.x
            new_y = jug_y_capacity
            if State(new_x, new_y) not in visited:
                queue.append((State(new_x, new_y), path + [current_state]))

        # Empty jug X
        if current_state.x > 0:
            new_x = 0
            new_y = current_state.y
            if State(new_x, new_y) not in visited:
                queue.append((State(new_x, new_y), path + [current_state]))

        # Empty jug Y
        if current_state.y > 0:
            new_x = current_state.x
            new_y = 0
            if State(new_x, new_y) not in visited:
                queue.append((State(new_x, new_y), path + [current_state]))

        # Pour from X to Y
        if current_state.x > 0 and current_state.y < jug_y_capacity:
            pour_amount = min(current_state.x, jug_y_capacity - current_state.y)
            new_x = current_state.x - pour_amount
            new_y = current_state.y + pour_amount
            if State(new_x, new_y) not in visited:
                queue.append((State(new_x, new_y), path + [current_state]))

        # Pour from Y to X
        if current_state.y > 0 and current_state.x < jug_x_capacity:
            pour_amount = min(current_state.y, jug_x_capacity - current_state.x)
            new_x = current_state.x + pour_amount
            new_y = current_state.y - pour_amount
            if State(new_x, new_y) not in visited:
                queue.append((State(new_x, new_y), path + [current_state]))

    return None

def get_user_input():
    jug_x_capacity = int(input("Enter the capacity of jug X: "))
    jug_y_capacity = int(input("Enter the capacity of jug Y: "))
    target_amount = int(input("Enter the target amount for jug X: "))
    return jug_x_capacity, jug_y_capacity, target_amount

def main():
    jug_x_capacity, jug_y_capacity, target_amount = get_user_input()

    solution = water_jug_bfs(jug_x_capacity, jug_y_capacity, target_amount)

    if solution:
        print("Solution Found:")
        for step, state in enumerate(solution):
            print(f"Step {step + 1}: {state}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
