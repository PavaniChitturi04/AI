board = {str(i): ' ' for i in range(1, 10)}
def print_board(board):
    print('|' + board['1'] + '|' + board['2'] + '|' + board['3']+ '|' )
    print('--+--+-')
    print('|' + board['4'] + '|' + board['5'] + '|' + board['6']+ '|' )
    print('--+--+-')
    print('|' + board['7'] + '|' + board['8'] + '|' + board['9']+ '|' )



def game():
    turn, count = 'X', 0
    while count < 9:
        print_board(board)
        move = input(f"It's your turn, {turn}. Move to which place? ")
        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("That place is already filled.")
            continue 
        for a, b, c in [(7, 8, 9), (4, 5, 6), (1, 2, 3), (1, 4, 7), (2, 5, 8), (3, 6, 9), (7, 5, 3), (1, 5, 9)]:
            if board[str(a)] == board[str(b)] == board[str(c)] != ' ':
                print_board(board)
                print(f"\nGame Over. The player {turn} won the game!")
                return
        turn = 'O' if turn == 'X' else 'X'
    print("\nGame Over. It's a Tie!!")



if __name__ == "__main__":
    game()