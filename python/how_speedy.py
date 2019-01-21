import time

timestamp = int(time.time())
count = 0
while True:
    now = int(time.time())
    if now - timestamp >= 1:
        print(f'For {timestamp} we looped {count} times')
        timestamp = now
        count = 0
    count += 1

