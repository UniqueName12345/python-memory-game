# account cli screen
import base64
# make root_password_encoded a global variable
root_password_encoded = base64.b64encode(b"root")
# make root_password_decoded a secret variable
root_password_decoded = base64.b64decode(root_password_encoded)

# give users a choice between:
# 1. create a new account
# 2. login to an existing account
# 3. exit
def main_menu():
    print("\nWelcome to the account system!")
    print("1. Create a new account")
    print("2. Login to an existing account")
    print("3. Exit")
    choice = input("\nPlease choose an option: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        login()
    elif choice == "3":
        exit()
    else:
        print("\nInvalid option. Please try again.")
        main_menu()

def create_account():
    print("\nPlease enter your details below:")
    username = input("Username: ")
    password = input("Password: ")
    password_confirm = input("Confirm password: ")
    if password == password_confirm:
        import os
        # write the normal username to "accounts.txt"
        with open("accounts.txt", "a") as file:
            file.write(username + "\n")
        # encrypt the password and write it to "accounts.txt"
        encrypted_password = base64.b64encode(password.encode())
        with open("accounts.txt", "a") as file:
            file.write(encrypted_password.decode() + "\n")
        print("\nAccount created successfully.")
        login()
    else:
        print("\nPasswords do not match. Please try again.")
        create_account()

def login():
    print("\nPlease enter your username and password below:")
    username = input("Username: ")
    password = input("Password: ")
    # read the username and password from "accounts.txt"
    with open("accounts.txt", "r") as file:
        lines = file.readlines()
    # check if the username is in the list of usernames
    if username in lines:
        # check if the password is the same as the password in "accounts.txt"
        if password == lines[lines.index(username) + 1].strip():
            print("\nLogin successful.")
            main_menu()
        else:
            print("\nIncorrect password. Please try again.")
            login()
    else:
        print("\nUsername not found. Please try again.")
        login()
# make a random number
import random
random_number = random.randint(1, 10)


# ask the user to guess a number
guess = int(input("Guess a number between 1 and 10: "))

# compare the user's guess to the random number
if guess == random_number:
    print("You got it!")
else:
    print("Nope. The number I was thinking of was {}".format(random_number))

