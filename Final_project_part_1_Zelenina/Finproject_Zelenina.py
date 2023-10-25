from random import randrange

def make_list_of_free_fields(board):
    free_fields = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not (board[i][j] == "O" or board[i][j] == "X"):
                free_fields.append((i, j))
    return free_fields

def victory_for(board, sign):
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True

    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    for i in range(len(board)):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True

    for j in range(len(board[0])):
        if board[0][j] == sign and board[1][j] == sign and board[2][j] == sign:
            return True

    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    field = free_fields[randrange(len(free_fields))]
    board[field[0]][field[1]] = 'X'

def enter_move(board):
    while True:
        move = int(input("Enter your move: "))

        row = (move - 1) // 3
        column = (move - 1) % 3

        if move < 1 or move > 9:
            continue
        elif board[row][column] == "O" or board[row][column] == "X":
            continue
        else:
            break
    board[row][column] = "O"

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


board = [[1, 2, 3],
         [4, 'X', 6],
         [7, 8, 9]]

GameOver = False

display_board(board)

while not GameOver:
    if len(make_list_of_free_fields(board)) == 0:
        print("Tie")
        GameOver = True
    else:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("You won")
            GameOver = True

    if not GameOver and not len(make_list_of_free_fields(board)) == 0:
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("You lose")
            GameOver = True