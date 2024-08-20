from cryptography.fernet import Fernet # type: ignore


##### Macintosh #####
#'/Users/malpal101/Plethora-of-Python/Beginner-Projects/5-Python-Projects-For-Beginners/Password-Manager/key.key'

##### Windows #####
#'C:\Users\User\Plethora-of-Python\Beginner-Projects\5-Python-Projects-For-Beginners\Password-Manager\key.key'

'''
# Generate a key and save it in a file
def write_key():
    key = Fernet.generate_key()
    with open('/Users/malpal101/Plethora-of-Python/Beginner-Projects/5-Python-Projects-For-Beginners/Password-Manager/key.key', "wb") as key_file:
        key_file.write(key)

write_key()
'''


def load_key():
    file = open('/Users/malpal101/Plethora-of-Python/Beginner-Projects/5-Python-Projects-For-Beginners/Password-Manager/key.key', "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)


##### Macintosh #####
#'/Users/malpal101/Plethora-of-Python/Beginner-Projects/5-Python-Projects-For-Beginners/Password-Manager/passwords.txt'

##### Windows #####
#'C:\Users\User\Plethora-of-Python\Beginner-Projects\5-Python-Projects-For-Beginners\Password-Manager\passwords.txt'


def view():
    with open('/Users/malpal101/Plethora-of-Python/Beginner-Projects/5-Python-Projects-For-Beginners/Password-Manager/passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('/Users/malpal101/Plethora-of-Python/Beginner-Projects/5-Python-Projects-For-Beginners/Password-Manager/passwords.txt', 'a') as f:
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
