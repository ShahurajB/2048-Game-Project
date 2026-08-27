
import keyboard
from Game_Engine import *
import configs.globals as globals
from log.log_system import logger

def print_array():
    print(f'Your Score: {globals.score}', end="\n")
    logger.info(f'Your Score: {globals.score}')

    print("+----+----+----+----+")
    # logger.info("+----+----+----+----+")
    for row in globals.arr:
        for cell in row:
            if cell == 0:
                print("|    ", end="")
                # logger.info("|    ")
            else:
                print(f"| {cell:<3}", end="")
                # logger.info(f"| {cell:<3}")
        print("|")
        # logger.info("|")
        print("+----+----+----+----+")
        # logger.info("+----+----+----+----+")

def restart():
    # print("In Restart function")
    logger.info("In Restart function")

    globals.arr[:] = 0
    globals.score = 0

    flag = generate_random_number()
    if flag:
        print_array()
    else:
        # print("Game is Over , No space left")
        logger.info("Game is Over , No space left")
        exit()

def display_and_random_num_gen():
    flag = generate_random_number()
    if flag:
        print_array()
        return True
    else:
        # print("Game is Over , No space left")
        logger.info("Game is Over , No space left")
        return False

def main():

    print("System Ready. Use arrow keys to trigger actions (Esc to quit).", end="\n")
    logger.info("Executing main function.")

    first = generate_random_number()
    second = generate_random_number()

    if first and second:
        print_array()
    else:
        # print("Game is Over , No space left")
        logger.info("Game is Over , No space left")
        exit()


    while True:
        event = keyboard.read_event()

        # print(f'Event type: {event.event_type}')
        if event.event_type == keyboard.KEY_DOWN:

            move_map = {
                'up': top_move,
                'down': down_move,
                'left': left_move,
                'right': right_move
            }
            # print(f'event name :{event.name}')
            if event.name == 'esc':
                # print("Exiting...")
                logger.info("Exiting...")
                break
            elif event.name == "u":
                undo_function()
                print_array()
            elif event.name == "r":
                redo_function()
                print_array()
            elif event.name == "s":
                restart()
            elif event.name == "h":
                help_function()

            elif event.name in move_map:
                moved = move_map[event.name]()
                # print(f"return value :{moved}")

                if check_game_over():
                    # print("Congratulations.. You Won the game!!!")
                    logger.info("Congratulations.. You Won the game!!!")
                    print_array()
                    break

                if moved:
                    if not display_and_random_num_gen():
                        break
                else:
                    print_array()
                    if is_array_full():
                        # print("Game is Over , Array is full, No space left")
                        logger.info("Game is Over , Array is full, No space left")
                        exit()

if __name__ == "__main__":
    main()