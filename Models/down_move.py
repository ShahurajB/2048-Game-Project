import globals

def down_move():
    print("Action: Moving Down...", end="\n")

    arr = globals.arr
    moved = False

    COLS = 4
    ROWS = 3

    for col in range(COLS):
        for row in range(ROWS):
            if arr[row][col] != 0  and arr[row][col] == arr[row+1][col]:
                value = arr[row][col] + arr[row+1][col]
                arr[row+1][col] = value
                arr[row][col] = 0
                globals.score += value
                moved = True
            else:
                if arr[row][col] != 0 and arr[row+1][col] == 0:
                    arr[row+1][col] = arr[row][col]
                    arr[row][col] = 0
                    moved = True

    return moved