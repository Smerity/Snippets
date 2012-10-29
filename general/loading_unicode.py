import random
import sys
import time

loaders = [
    u"\u25F7\u25F6\u25F5\u25F4",
    u"\u25CB\u25CC",
    u"\u25C7\u25C8\u25C9\u25CE"

]
loader = random.choice(loaders)

while 1:
    for c in loader:
        sys.stdout.write(c+"  Loading...")
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write("\r")
