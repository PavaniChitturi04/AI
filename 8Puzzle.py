from collections import deque

# Define the goal state
goal_state = ((1, 2, 3), (8, 0, 4), (7, 6, 5))

# Define possible moves
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = None, None
   
    for row_idx, row in enumerate(state):
        if 0 in row:
            empty_row, empty_col = row_idx, row.index(0)
            break
           
    for move in moves:
        new_row, new_col = empty_row + move[0], empty_col + move[1]
       
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            neighbor = [list(row) for row in state]
            neighbor[empty_row][empty_col], neighbor[new_row][new_col] = neighbor[new_row][new_col], neighbor[empty_row][empty_col]
            neighbors.append(tuple(map(tuple, neighbor)))
   
    return neighbors

def bfs(start):
    queue = deque([(start, [])])
    visited = set()
   
    while queue:
        state, path = queue.popleft()
       
        if state == goal_state:
            return path
       
        visited.add(state)
       
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
   
    return None

def main():
    print("Enter the initial state:")
    initial_state = []
    for _ in range(3):
        row = tuple(map(int, input().split()))
        initial_state.append(row)
   
    solution_path = bfs(tuple(initial_state))
   
    if solution_path:
        print("Solution steps:")
        for step in solution_path:
            for row in step:
                print(row)
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()