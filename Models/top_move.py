import globals

def top_move():

    print("Action: Moving Up...", end="\n")

    arr = globals.arr
    undo_arr = globals.undo_arr
    redo_arr = globals.redo_arr

    moved = False

    ROWS = 3
    COLS = 4

    for col in range(COLS):
        next_row = ROWS
        current_row = ROWS - 1
        for _ in range(ROWS):
            if arr[next_row][col] != 0 and arr[next_row][col] == arr[current_row][col]:
                undo_arr[:] = arr
                redo_arr[:] = 0
                value = arr[next_row][col] + arr[current_row][col]
                arr[current_row][col] = value
                arr[next_row][col] = 0

                globals.undo_score = globals.score
                globals.redo_score = 0

                globals.score += value
                moved = True
            else:
                if arr[next_row][col] != 0 and arr[current_row][col] == 0:
                    undo_arr[:] = arr
                    redo_arr[:] = 0
                    arr[current_row][col] = arr[next_row][col]
                    arr[next_row][col] = 0
                    moved = True
            next_row -= 1
            current_row -= 1

    return moved