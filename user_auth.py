import hashlib
import csv
import customtkinter as ctk

# User class to handle user data(username/pass/points/level) and actions (login/signup)
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        with open("user_data", "a") as file:
            if username == self.username and password == self.password:
                print("Login successful")

    def signup(self):
        self.username = input("Create a username: ")
        self.password = input("Create a password: ")
        pass_match = input("Enter a password again: ")

        if self.password == pass_match:
            with open("user_data", "a") as file:
                writer = csv.writer(file, delimiter = "\t", quotechar = "'", quoting = csv.QUOTE_MINIMAL)
                writer.writerow([self.username, self.password])
        else:
            print("Passwords do not match")


#implement later: check if the username exists in the database and the password is correct

'''
while 1:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        user = User("","")
        user.signup()
    elif choice == 2:
        user = User("","")
        user.login()
    else:
        break
'''
# TEMP! Store user data
users = []


