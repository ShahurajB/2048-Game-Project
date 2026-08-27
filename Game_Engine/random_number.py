import random
import configs.globals as globals
from log.log_system import logger

ROWS = 4
COLS = 4
def generate_random_number():
    logger.info("In generate_random_number function")

    empty_cells = []

    for row in range(ROWS):
        for col in range(COLS):
            if globals.arr[row][col] == 0:
                empty_cells.append((row, col))

    if not empty_cells:
        return False
    
    row, col = random.choice(empty_cells)

    num = random.choice([2, 4])
    globals.arr[row][col] = num

    return True


def check_game_over():
    logger.info("In check_game_over function")
    arr = globals.arr

    for row in range(ROWS):
        for col in range(COLS):
            if arr[row][col] == 2048:
                return True

    return False

def is_array_full():
    logger.info("In is_array_full function")
    
    arr = globals.arr

    for row in range(ROWS):
        for col in range(COLS):
            if arr[row][col] == 0:   # found empty space
                return False

    return True  # no empty space → array is full
