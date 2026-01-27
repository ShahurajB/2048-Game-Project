import globals

def right_move():
    print("Action: Turning Right...", end="\n")

    moved = False
    arr = globals.arr
    undo_arr = globals.undo_arr
    redo_arr = globals.redo_arr

    ROWS = 4
    COLS = 3

    for row in range(ROWS):
        for col in range(COLS):
            if arr[row][col] != 0 and arr[row][col] == arr[row][col + 1]:
                undo_arr[:] = arr
                redo_arr[:] = 0
                value = arr[row][col] + arr[row][col + 1]
                arr[row][col + 1] = value

                globals.undo_score = globals.score
                globals.redo_score = 0

                globals.score += value
                arr[row][col] = 0
                moved = True
            else:
                if arr[row][col] != 0 and arr[row][col + 1] == 0:
                    undo_arr[:] = arr
                    redo_arr[:] = 0
                    arr[row][col+1] = arr[row][col]
                    arr[row][col] = 0
                    moved = True

    return moved