import hashlib
import csv
import customtkinter as ctk

# User class to handle user data(username/pass/points/level) and actions (login/signup)
# Will implement status state: active or not-active
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

class LoginDisplay(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(width=600, height=400)

        # Divide the window into 2 columns; allows resizing the columns and centering the buttons
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Use label for welcome text msg instead of textbox - semantically better
        self.welcome_message = ctk.CTkLabel(self, text="\nWelcome to Vocabulary Builder App! \nPlease log in or "
        "create a new account", font=("Arial", 20))

        self.welcome_message.grid(row=0, column=0, columnspan=2, padx=20,
                                  pady=20, sticky="nsew")
        #   Center the label
        self.welcome_message.configure(anchor="center")
# TO-DO
        self.login_input = ctk.CTkTextbox(self, width=200, height=60)

        # Create login button
        self.login_button = ctk.CTkButton(self, text="LOGIN", command=self.button_login)
        self.login_button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        # Create signup button
        self.signup_button = ctk.CTkButton(self, text="SIGN UP", command=self.button_signup)
        self.signup_button.grid(row=2, column=1, padx=20, pady=20, sticky="ew")

# User instance to handle login and signup GUI
        self.user = User("", "")

    def button_login(self):
        self.user.login()

    def button_signup(self):
        self.user.signup()

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


