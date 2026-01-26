import globals


def left_move():
    print("Action: Turning Left...", end="\n")
    moved = False
    arr = globals.arr

    R0WS = 4
    COLS = 4

    for row in range(R0WS):

        right = COLS - 1
        left = COLS -2

        for _ in range(COLS - 1):
            if arr[row][left] != 0  and arr[row][left] == arr[row][right]:
                value = arr[row][left] + arr[row][right]
                arr[row][left] = value
                globals.score += value
                arr[row][right] = 0
                moved = True
            else:
                if arr[row][right] != 0 and arr[row][left] == 0:
                    arr[row][left] = arr[row][right]
                    arr[row][right] = 0
                    moved = True

            right -= 1
            left -= 1

    return moved

