import config
import random as rand


class User:
    def __init__(self):
        self.name = None
        self.status = None
        self.username = None
        self.password = None
        self.__key = None
        self.role = None

    def __encrypt(self, password, key=None):
        if not key:
            self.__key = rand.randint(0, 99)
        temp = ''
        k = int(len(password) / 2)
        for ch in password:
            temp += str((self.__key * ord(ch) + (self.__key << k)) % 26)
        n = int(len(temp) / 2)
        temp += str(self.__key) + str(k) + str(n)
        return temp

    def register(self):
        self.username = input("Enter username: ")
        self.name = input("Enter name: ")
        self.password = self.__encrypt(input("Enter password: "))
        self.status = 'Active'
        self.role = 'Registered'

    def change_password(self):
        self.password = self.__encrypt(input("Enter new password: "))

    def isExist(self, username, password):
        return (self.username == username) \
               and (self.password == self.__encrypt(password, self.__key)) \
               and (self.status != 'Suspended')

    def demoUser_setPass(self):
        self.password = self.__encrypt(self.password)


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        if config.data.users[username].isExist(username, password):
            config.loggedInUser = config.data.users[username]
            print("Successfully Logged in!")
        else:
            raise KeyError
    except KeyError:
        print("Oops! Seems like no user exist with such credentials!\n")


def reg():
    u = User()
    u.register()
    config.data.setUsers(u)


def allUsers():
    if len(config.data.users) != 0:
        print('\n'.join(config.data.users.keys()))
    else:
        print("No user found!")


def allUsers_byAlpha():
    userdata = config.db.linkedlist.LinkedList()
    ch = input("Enter any character: ")
    for username in config.data.users:
        if ch.upper() == username[0].upper():
            userdata.push(username)
    if len(userdata) != 0:
        print(userdata)
    else:
        print("No user found!")


def suspend():
    uname = input("Enter username of user to suspend: ")
    try:
        config.data.users[uname].status = 'Suspended'
        print(f"Account of {uname} has been suspended successfully!")
    except KeyError:
        print("User not Found!")


def unsuspend():
    uname = input("Enter username of user to unsuspend: ")
    try:
        config.data.users[uname].status = 'Active'
        print(f"Account of {uname} has been unsuspended successfully!")
    except KeyError:
        print("User not Found!")


def delete_user():
    uname = input("Enter username of user to delete: ")
    try:
        del config.data.users[uname]
        print(f"Account of {uname} has been deleted successfully!")
    except KeyError:
        print("User not Found!")


def modify_user():
    uname = input("Enter username of any user to edit: ")
    print("""What you want to modify? 
1. Name
2. Password""")
    ch = str(input("Choose any option: "))
    try:
        if ch == '1':
            config.data.users[uname].name = input("Enter new name: ")
        elif ch == '2':
            config.data.users[uname].change_password()
        else:
            print("Invalid Option Chosen!")
    except KeyError:
        print("User not Found!")


def add_user():
    u = User()
    u.register()
    print("""What role you want to assign to user? 
1. Registered
2. Administrator""")
    ch = input("Choose any option: ")
    if ch == '1':
        pass
    elif ch == '2':
        u.role = 'Administrator'

    config.data.setUsers(u)


def logout():
    config.loggedInUser = None
