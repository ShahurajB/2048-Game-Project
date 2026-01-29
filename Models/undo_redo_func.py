import globals

def undo_function():
    print("Inside undo function")
    if globals.undo_arr is None:
        print("Nothing to undo")
    else:
        print("Undo arry: {globals.undo_arr}")
        # globals.redo_arr = globals.arr.copy()
        # globals.arr[:] = globals.undo_arr

        globals.redo_arr.append(globals.arr.copy())
        globals.arr = globals.undo_arr.pop()

    if globals.undo_score is None:
        print("No score to undo")
    else:
        globals.redo_score.append(globals.score)
        # globals.redo_score = globals.score
        globals.score = globals.undo_score.pop()

def redo_function():
    print("Inside Redo function")
    if globals.redo_arr is None:
        print("Nothing to redo")
    else:
        # globals.undo_arr = globals.arr.copy()
        # globals.arr[:] = globals.redo_arr

        globals.undo_arr.append(globals.arr.copy())
        globals.arr = globals.redo_arr.pop()

    if globals.redo_score is None:
        print("No score to redo")
    else:
        globals.undo_score.append(globals.score)
        # globals.undo_score = globals.score
        globals.score = globals.redo_score.pop()

def help_function():
    commands = {

        "h": "For help",
        "u": "For undo",
        "r": "For redo",
        "s": "For restart",
        "↑": "For up swipe",
        "↓": "For down swipe",
        "←": "For left swipe",
        "→": "For right swipe",
        "esc": "Exiting"
    }

    print()
    for key, action in commands.items():
        print(f"{key:<3} : {action}")
    print("\n")