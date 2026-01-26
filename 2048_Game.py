
import keyboard
from Models import *
import globals


def print_array():
    print(f'Your Score: {globals.score}', end="\n")

    print("+----+----+----+----+")
    for row in globals.arr:
        for cell in row:
            if cell == 0:
                print("|    ", end="")
            else:
                print(f"| {cell:<3}", end="")
        print("|")
        print("+----+----+----+----+")

def display_and_random_num_gen():
    flag = generate_random_number()
    if flag:
        print_array()
        return True
    else:
        print("Game is Over , No space left")
        return False

def main():

    print("System Ready. Use arrow keys to trigger actions (Esc to quit).", end="\n")

    first = generate_random_number()
    second = generate_random_number()

    if first and second:
        print_array()
    else:
        print("Game is Over , No space left")
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

            if event.name == 'esc':
                print("Exiting...")
                break

            elif event.name in move_map:
                moved = move_map[event.name]()
                # print(f"return value :{moved}")

                if check_game_over():
                    print("Congratulations.. You Won the game!!!")
                    print_array()
                    break

                if moved:
                    if not display_and_random_num_gen():
                        break
                else:
                    print_array()
                    if is_array_full():
                        print("Game is Over , Array is full, No space left")
                        exit()

if __name__ == "__main__":
    main()