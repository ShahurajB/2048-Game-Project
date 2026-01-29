import globals

def down_move():
    print("Action: Moving Down...", end="\n")

    arr = globals.arr
    undo_arr = globals.undo_arr
    redo_arr = globals.redo_arr

    moved = False

    COLS = 4
    ROWS = 3

    for col in range(COLS):
        for row in range(ROWS):
            if arr[row][col] != 0  and arr[row][col] == arr[row+1][col]:

                # undo_arr[:] = arr
                # redo_arr[:] = 0

                undo_arr.append(arr.copy())
                redo_arr.clear()

                value = arr[row][col] + arr[row+1][col]
                arr[row+1][col] = value
                arr[row][col] = 0

                # globals.undo_score = globals.score
                # globals.redo_score = 0

                globals.undo_score.append(globals.score)
                globals.redo_score.clear()

                globals.score += value
                moved = True
            else:
                if arr[row][col] != 0 and arr[row+1][col] == 0:
                    # undo_arr[:] = arr
                    # redo_arr[:] = 0
                    undo_arr.append(arr.copy())
                    redo_arr.clear()
                    arr[row+1][col] = arr[row][col]
                    arr[row][col] = 0
                    moved = True

    return moved