import curses
from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    lines = ['']
    while True:
        cmd = stdscr.getkey()
        if cmd == '\n':
            lines.append('')
            #curses.beep()
        else:
            lines[-1] += cmd
        for idx, line in enumerate(lines):
            args = (curses.A_BOLD,) if idx == len(lines) - 1 else ()
            stdscr.addstr(idx, 0, repr(line), *args)

wrapper(main)
