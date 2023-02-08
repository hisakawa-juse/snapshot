from PIL import ImageGrab
import sys
import os
import datetime
import time

def main():
    i = 1
    interval = None
    output = None
    limit = None
    arg_len = len(sys.argv)
    while i < arg_len:
        if sys.argv[i] == '--interval' and i < arg_len - 1:
            interval = sys.argv[i + 1]
            i += 1
        elif sys.argv[i] == '--output' and i < arg_len - 1:
            output = sys.argv[i + 1]
            i += 1
        elif sys.argv[i] == '--limit' and i < arg_len - 1:
            limit = sys.argv[i + 1]
            i += 1
        i += 1

    if output is not None:
        make_folder(output)
    else:
        output = '.'

    if interval is None:
        interval = 1000
    else:
        interval = int(interval)

    if limit is not None:
        limit = int(limit)

    grab(output, interval, limit)

def grab(output, interval, limit):
    counter = 0
    while True:
        screenshot = ImageGrab.grab()
        dt = datetime.datetime.timestamp(datetime.datetime.now())
        screenshot.save(output + "/" + str(dt) + '.png')
        if limit is not None and counter >= limit:
            break
        counter += 1
        time.sleep(interval / 1000.0)

def make_folder(folder):
    os.mkdir(folder)

if __name__ == '__main__':
    main()
