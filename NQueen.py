def is_safe(board, row, col):
    # Check if a queen can be placed at board[row][col] without attacking others

    # Check the left side of this row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    def solve_util(col):
        if col >= n:
            return True

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve_util(col + 1):
                    return True
                board[i][col] = 0

        return False

    if not solve_util(0):
        print("Solution does not exist")
        return False

    for row in board:
        print(" ".join(map(str, row)))
    return True

def main():
    try:
        n = int(input("Enter the board size (N): "))
        if n <= 0:
            print("Please enter a positive integer for N.")
            return
        solve_n_queens(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer for N.")

if __name__ == "__main__":
    main()