import hashlib
import getpass

password_manager = {}

def create():
    username = input("enter your username:")
    password = getpass.getpass("enter your password:")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username]=hashed_password
    print("account created successfull!")

def login():
    username = input("enter your username:")
    password = getpass.getpass("enter your password:")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and hashed_password in password_manager[username]==hashed_password:
        print("login successfull")
    else:
        print("invalid credentials")

def main():
    while True:
        choice = input("enter 1 to create account and 2 to login and 0 to exit")
        if choice == "1":
            create()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("invalid choice.")

if __name__=="__main__":
    main()