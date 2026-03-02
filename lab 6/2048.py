import random
import os

SIZE = 4


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def create_board():
    board = [[0] * SIZE for _ in range(SIZE)]
    add_tile(board)
    add_tile(board)
    return board


def add_tile(board):
    empty = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if empty:
        r, c = random.choice(empty)
        board[r][c] = 2 if random.random() < 0.9 else 4


def print_board(board):
    clear()
    print("===== 2048 =====")
    for row in board:
        print("+----" * SIZE + "+")
        for cell in row:
            print(f"|{cell:^4}" if cell != 0 else "|    ", end="")
        print("|")
    print("+----" * SIZE + "+")
    print("W = вверх | S = вниз | A = влево | D = вправо | Q = выход")


def compress(row):
    new_row = [num for num in row if num != 0]
    new_row += [0] * (SIZE - len(new_row))
    return new_row


def merge(row):
    for i in range(SIZE - 1):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            row[i + 1] = 0
    return row


def move_left(board):
    moved = False
    new_board = []
    for row in board:
        compressed = compress(row)
        merged = merge(compressed)
        final = compress(merged)
        if final != row:
            moved = True
        new_board.append(final)
    return new_board, moved


def reverse(board):
    return [row[::-1] for row in board]


def transpose(board):
    return [list(row) for row in zip(*board)]


def move_right(board):
    reversed_board = reverse(board)
    new_board, moved = move_left(reversed_board)
    return reverse(new_board), moved


def move_up(board):
    transposed = transpose(board)
    new_board, moved = move_left(transposed)
    return transpose(new_board), moved


def move_down(board):
    transposed = transpose(board)
    new_board, moved = move_right(transposed)
    return transpose(new_board), moved


def can_move(board):
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                return True
            if c < SIZE - 1 and board[r][c] == board[r][c + 1]:
                return True
            if r < SIZE - 1 and board[r][c] == board[r + 1][c]:
                return True
    return False


def main():
    board = create_board()

    while True:
        print_board(board)
        if not can_move(board):
            print("Игра окончена!")
            break

        move = input("Ваш ход: ").lower()

        if move == "q":
            break
        elif move == "a":
            board, moved = move_left(board)
        elif move == "d":
            board, moved = move_right(board)
        elif move == "w":
            board, moved = move_up(board)
        elif move == "s":
            board, moved = move_down(board)
        else:
            continue

        if moved:
            add_tile(board)


if __name__ == "__main__":
    main()