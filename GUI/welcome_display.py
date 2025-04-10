import customtkinter as ctk
from user_auth import User

# User auth GUI: welcome screen, login/signup
class WelcomeDisplay(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.app = None # set the controller

        self.configure(width=600, height=400)

# Divide the window into 2 columns; allows resizing the columns and centering the buttons
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

# Use label for welcome text msg instead of textbox - semantically better
        self.welcome_message = ctk.CTkLabel(self, text="\nWelcome to Vocabulary Builder App! \nPlease log in or "
        "create a new account", font=("Arial", 20))

        self.welcome_message.grid(row=0, column=0, columnspan=2, padx=20,
                                  pady=20, sticky="nsew")
# Center the label
        self.welcome_message.configure(anchor="center")

# Login button
        self.login_button = ctk.CTkButton(self, text="LOGIN", command=self.button_login)
        self.login_button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

# Signup button
        self.signup_button = ctk.CTkButton(self, text="SIGN UP", command=self.button_signup)
        self.signup_button.grid(row=2, column=1, padx=20, pady=20, sticky="ew")

# User instance to handle login and signup GUI
        self.user = User("", "")

    def set_controller(self, app):
        self.app = app

    def button_login(self):
   #     self.user.login()
# Clear the display
        self.welcome_message.destroy()
        self.login_button.destroy()
        self.signup_button.destroy()

        self.test_msg = ctk.CTkLabel(self, text="test")
        #self.username_input = ctk.CTkEntry(self)
        #self.password_input = ctk.CTkEntry(self)

        #self.submit_login = ctk.CTkButton(self, text="Submit", command=self.handle_login)

    def button_signup(self):
        self.user.signup()

    #def handle_login(self):
    #    return True