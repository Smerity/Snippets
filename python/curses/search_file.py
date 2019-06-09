import curses
from curses import wrapper

import sys

def fetch(data, seq, max_results=10):
    results = []
    new_start = None
    while len(results) < max_results:
        match = data.find(seq, new_start)
        if match == -1:
            break
        results.append(match)
        new_start = results[-1] + 1
    return results

def normalize(text):
    text = text.replace('\\\\n', '\\\u240d').replace('\\\\r', '\\\u240a').replace('\n', '\u2424').replace('\\\\"', '\\"').replace("\'", "'")
    return text

def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.curs_set(0)

    fn = sys.argv[1]
    data = open(fn).read()

    query = ''
    while True:
        cmd = stdscr.getkey()
        if cmd == '\n':
            query = ''
            stdscr.clear()
            #curses.beep()
        elif cmd == 'KEY_BACKSPACE':
            query = query[:-1]
        else:
            query += cmd
        ###
        stdscr.clear()
        ###
        stdscr.addstr(0, 0, f'Querying {fn}: {repr(query)}')
        results = fetch(data, query)
        window = 40
        for idx, result in enumerate(results):
            low, high = max(result - window, 0), min(len(data), result + len(query) + window)
            prefix = data[low:result]
            mid = query
            suffix = data[result + len(query):high]
            s = normalize(prefix + mid + suffix)
            #s = len(s)
            stdscr.addstr(idx + 1, 0, '- ' + repr(s))
        ###
        stdscr.refresh()

wrapper(main)
