import globals

def top_move():

    print("Action: Moving Up...", end="\n")

    arr = globals.arr
    moved = False

    ROWS = 3
    COLS = 4

    for col in range(COLS):
        next_row = ROWS
        current_row = ROWS - 1
        for _ in range(ROWS):
            if arr[next_row][col] != 0 and arr[next_row][col] == arr[current_row][col]:

                value = arr[next_row][col] + arr[current_row][col]
                arr[current_row][col] = value
                arr[next_row][col] = 0
                globals.score += value
                moved = True
            else:
                if arr[next_row][col] != 0 and arr[current_row][col] == 0:
                    arr[current_row][col] = arr[next_row][col]
                    arr[next_row][col] = 0
                    moved = True
            next_row -= 1
            current_row -= 1

    return moved