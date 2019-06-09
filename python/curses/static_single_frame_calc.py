from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    for v in range(1, 11):
        stdscr.addstr(v, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
