import customtkinter as ctk
from user_auth import User

# User auth GUI: welcome screen, login/signup
class WelcomeDisplay(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None # set the controller
        #self.user = User("", "")  # user instance to handle login and signup GUI

# Divide the window into 2 columns; allows resizing the columns and centering the buttons
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

# Use label for welcome text msg instead of textbox - better semantically
        self.welcome_message = ctk.CTkLabel(self, text="\nWelcome to Vocabulary Builder App! \nPlease log in or "
        "create a new account", font=("Arial", 20))
        self.welcome_message.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew") #append to grid
        self.welcome_message.configure(anchor="center") # Center the label

# Login button
        self.login_button = ctk.CTkButton(self, text="LOGIN", command=self.display_login)
        self.login_button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

# Signup button
        self.signup_button = ctk.CTkButton(self, text="SIGN UP", command=self.display_signup)
        self.signup_button.grid(row=2, column=1, padx=20, pady=20, sticky="ew")

    def set_controller(self, controller):
        self.controller = controller # set the controller

    def display_login(self):
        self.controller.load_login_display() # On click switch to login_display window

    def display_signup(self):
        return True
        #self.user.signup() # do later
