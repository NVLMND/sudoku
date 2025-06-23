import random
import time


board=[[0 for _ in range(9)]for _ in range(9)]


def rules():
    print("\n===================== SUDOKU RULES =====================")
    print("1. The board is a 9x9 grid, divided into 9 smaller 3x3 boxes.")
    print("2. Each row must contain the numbers 1 to 9 without repetition.")
    print("3. Each column must also contain the numbers 1 to 9 without repetition.")
    print("4. Each 3x3 box must contain the numbers 1 to 9 without repetition.")
    print("5. Empty cells are shown as 0. Your task is to fill them correctly.")
    print("6. You can only place numbers 1–9 in empty cells.")
    print("7. The puzzle is solved when the entire grid follows the rules above.")
    print("8. If you make 5 mistakes — invalid moves, wrong inputs, or rule violations — the game ends and you lose.")
    print("\n---To Play select Below---")



def playable_game(board, space=50):
    count=0
    while count<space:
        row=random.randint(0, 8)
        col=random.randint(0, 8)
        if board[row][col]!=0:
            board[row][col]=0
            count+=1


def is_valid(board, row, col, num):
    if num in board[row]:
        return False

    for i in range(9):
        if board[i][col]==num:
            return False

    start_row=(row//3)*3
    start_col=(col//3)*3

    for i in range(start_row, start_row+3):
        for j in range(start_col, start_col+3):
            if board[i][j]==num:
                return False
    return True


def check_win(board):
    for row in board:
        if 0 in row:
            return False
    return True


def solve_game(board):
    for row in range(9):
        for col in range(9):
            if board[row][col]==0:
                nums=list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if is_valid(board, row, col, num):
                        board[row][col]=num
                        if solve_game(board):
                            return True
                        board[row][col]=0
                return False
    return True     


def random_board(board):
    solve_game(board)
    playable_game(board)
    print("\nYour Sudoku Board:\n(Remember row and column numbers)")
    for i, row in enumerate(board):
        print(" ", end="")
        for num in row:
            print(num, end=" ")
        if i==4:
            print("  ←", i,"= Row Numbers")
        else:
            print("  ←", i)
    print("\n ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑\n 0 1 2 3 4 5 6 7 8 = Column Numbers\n")


def scratch_board(board):
    print("\nYour Sudoku Board:\n(Remember row and column numbers)")
    for i, row in enumerate(board):
        print(" ", end="")
        for num in row:
            print(num, end=" ")
        if i==4:
            print("  ←", i,"= Row Numbers")
        else:
            print("  ←", i)
    print("\n ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑\n 0 1 2 3 4 5 6 7 8 = Column Numbers\n")


def main_logic(board):
    mistake=0
    while mistake<=4:
        try:
            row=int(input("choose row(0-8): "))
            col=int(input("choose col(0-8): "))
            while True:
                num=int(input("choose num(1-9): "))
                print("")
                if 1<=num<=9:
                    break
                mistake+=1
                print(f"Enter number in range(1-9)---mistake count={mistake}\n")
                if mistake>4:
                    print("Too many mistakes, Game over.")
                    return
            if is_valid(board, row, col, num):
                if board[row][col]==0:
                    board[row][col]=num
                    for r in board:
                        print(" ", end="")
                        for c in r:
                            print(c, end=" ")
                        print("")
                    
                    if check_win(board):
                        print("You won!")
                        return

                else:
                    mistake+=1
                    print(f"Place is not empty---mistake count={mistake}\n")
            else:
                mistake+=1
                print(f"Number already exists---mistake count={mistake}\n")
        except ValueError:
            mistake+=1
            print(f"Put number in range(0-8)---mistake count={mistake}\n")

    print("Too many mistakes, Game over.")




rules()
while True:
    choice=input("Play a random sudoku(1)\nBuild sudoku from scratch(2)\n-----: ")
    if choice=="1" or choice=="2":
        break
    print("---Enter 1 or 2---")

if choice=="1":
    random_board(board)
elif choice=="2":
    scratch_board(board)

start_time = time.time()
main_logic(board)
end_time = time.time()

elapsed = end_time - start_time
minutes = int(elapsed // 60)
seconds = int(elapsed % 60)

print(f"\nTotal Time: {minutes}:{seconds}")








