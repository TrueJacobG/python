import time
import random
import os
import argparse


def clear_console():
    os.system("cls") if os.name == "nt" else os.system("clear")


def print_c(message, line, position, length):
    print(line[:position] + '\033[91m' + message +
          '\033[0m' + line[position+length:])


def start():

    # defaults
    width = 100
    starting = 0
    how_many_screens = 10
    how_many_lines = 10
    message = "MESSAGE"

    parser = argparse.ArgumentParser()
    parser.add_argument("-width", type=int, default=width)
    parser.add_argument("-starting", type=int, default=starting)
    parser.add_argument("-screens", type=int, default=how_many_screens)
    parser.add_argument("-lines", type=int, default=how_many_lines)
    parser.add_argument("-message", type=str, default=message)

    args = parser.parse_args()
    print(args)

    return args.width, args.starting, args.screens, args.lines, args.message


def main():
    clear_console()

    width, starting, how_many_screens, how_many_lines, message = start()

    alf = "abcdefghijklmnoprstuwyz"

    t = 0
    while(t < how_many_screens):
        which_line = random.randint(0, how_many_lines-1)
        for x in range(how_many_lines):
            line = "".join([random.choice(alf) for _ in range(width)])
            if t >= starting and x == which_line:
                length = len(message)
                position = random.randint(0, width-length)
                print_c(message, line, position, length)
            else:
                print(line)

        time.sleep(1)
        clear_console()
        t += 1


if __name__ == "__main__":
    main()
