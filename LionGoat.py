from collections import deque

class State:
    def __init__(self, lion, goat, grass, farmer, parent=None):
        self.lion = lion
        self.goat = goat
        self.grass = grass
        self.farmer = farmer
        self.parent = parent

    def __eq__(self, other):
        return (self.lion, self.goat, self.grass, self.farmer) == (other.lion, other.goat, other.grass, other.farmer)

    def __hash__(self):
        return hash((self.lion, self.goat, self.grass, self.farmer))

    def is_valid(self):
        if (self.goat == self.lion and self.farmer != self.goat) or \
           (self.goat == self.grass and self.farmer != self.goat):
            return False
        return True

    def is_final(self):
        return self.lion == 'right' and self.goat == 'right' and self.grass == 'right' and self.farmer == 'right'

    def __repr__(self):
        return f"Lion: {self.lion}, Goat: {self.goat}, Grass: {self.grass}, Farmer: {self.farmer}"

def generate_moves():
    return ['Lion', 'Goat', 'Grass', 'Farmer']

def apply_move(state, move):
    new_state = State(state.lion, state.goat, state.grass, state.farmer)
    if move == 'Lion':
        new_state.lion = 'right' if state.lion == 'left' else 'left'
        new_state.farmer = 'right' if state.farmer == 'left' else 'left'
    elif move == 'Goat':
        new_state.goat = 'right' if state.goat == 'left' else 'left'
        new_state.farmer = 'right' if state.farmer == 'left' else 'left'
    elif move == 'Grass':
        new_state.grass = 'right' if state.grass == 'left' else 'left'
        new_state.farmer = 'right' if state.farmer == 'left' else 'left'
    elif move == 'Farmer':
        new_state.farmer = 'right' if state.farmer == 'left' else 'left'
    return new_state

def solve_game():
    initial_state = State('left', 'left', 'left', 'left')
    visited_states = set()
    queue = deque([initial_state])

    while queue:
        current_state = queue.popleft()
        if current_state.is_final():
            solution = []
            while current_state:
                solution.insert(0, current_state)
                current_state = current_state.parent
            return solution
        visited_states.add(current_state)

        for move in generate_moves():
            new_state = apply_move(current_state, move)
            if new_state.is_valid() and new_state not in visited_states:
                new_state.parent = current_state
                queue.append(new_state)

    return None

solution = solve_game()

if solution:
    for index, state in enumerate(solution):
        print("Step {}: Lion: {}, Goat: {}, Grass: {}, Farmer: {}".format(
            index + 1, state.lion, state.goat, state.grass, state.farmer))
else:
    print("No solution found.")
