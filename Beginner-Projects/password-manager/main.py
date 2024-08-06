import os
from cryptography.fernet import Fernet  # type: ignore

# Define the base directory (the directory where this script is located)
base_dir = os.path.dirname(os.path.abspath(__file__))

def write_key():
    key = Fernet.generate_key()
    key_path = os.path.join(base_dir, 'key.key')
    with open(key_path, "wb") as key_file:
        key_file.write(key)

def load_key():
    key_path = os.path.join(base_dir, 'key.key')
    with open(key_path, "rb") as file:
        key = file.read()
    return key

key = load_key()
fer = Fernet(key)

def view():
    password_path = os.path.join(base_dir, 'passwords.txt')
    with open(password_path, 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    password_path = os.path.join(base_dir, 'passwords.txt')
    with open(password_path, 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
