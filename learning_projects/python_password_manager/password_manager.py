from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

MASTER_PWD = input("What is the master password? ")
key = load_key() + MASTER_PWD.encode()
fer = Fernet(key)

def view():
    print("Your login credentials.")
    with open('passwords.txt', 'r') as f:
         for line in f.readlines():
            DATA = line.rstrip()
            user, passw = DATA.split("|")
            print("User:", user, "| Password:", str(fer.decrypt(passw.encode())))


def add():
    print("Please fil in the login credentials:")
    NAME = input('Username: ')
    PWD = input("Password: ")
    print("Username " + NAME + " and Password " + PWD + " added successfully!")

    with open('passwords.txt', 'a') as f:
        f.write(NAME + "|" + str(fer.encrypt(PWD.encode())) + "\n")


while True:
    MODE = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if MODE == "q":
        break
    
    elif MODE == "view":
        view()
    elif MODE == "add":
        add()
    else:
        print("Invalid mode.")
        continue 