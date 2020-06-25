from datetime import datetime

board_hard = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

board_medium = [
    [0,0,0,3,0,4,0,0,6],
    [0,4,0,0,6,9,8,1,0],
    [0,0,0,2,7,8,5,4,0],
    [7,0,1,9,5,2,4,3,8],
    [0,2,5,6,8,3,1,7,0],
    [8,9,3,1,4,7,6,0,2],
    [0,5,4,7,3,6,0,0,0],
    [0,7,6,8,2,0,0,9,0],
    [2,0,0,4,0,1,0,0,0]
]

board_easy = [
    [5,0,0,3,1,4,9,2,6],
    [0,4,2,5,6,9,8,1,7],
    [0,0,0,2,7,8,5,4,3],
    [7,6,1,9,5,2,4,3,8],
    [4,2,5,6,8,3,1,7,9],
    [8,9,3,1,4,7,6,5,2],
    [9,5,4,7,3,6,2,8,1],
    [1,7,6,8,2,5,3,9,4],
    [2,3,8,4,9,1,7,6,0]
]


def solve(bo):

    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(abs(bo[i][j]))
            else:
                print(str(abs(bo[i][j])) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None


def valid_all(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if valid(bo, abs(bo[i][j]), (i, j)) == False or bo[i][j] == 0:
                return False
    return True

def brute_force_solve(bo):
    count = 0
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                count += 1
            else:
                bo[i][j] = -bo[i][j]

    num = int("1"*count)
    while not valid_all(bo):
        tmp = num
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] >= 0:
                    bo[i][j] = tmp % 10
                    tmp = tmp // 10
        num += 1




def main():
    algo_choice = int(input("Please Select Algorithm Brute-force(0), Backtracking(1) :"))
    level_choice = int(input("Please Select Difficulty Easy(0), Medium(1), Hard(2) :"))

    if level_choice == 0:
        board = board_easy
    elif level_choice == 1:
        board = board_medium
    else:
        board = board_hard

    print_board(board)
    start_time = datetime.now()

    if algo_choice == 0:
        brute_force_solve(board)
    else:
        solve(board)

    print("_______________________\n")
    print_board(board)
    print("\nTotal time spent {}".format(datetime.now() - start_time))


if __name__ == "__main__":
    main()
