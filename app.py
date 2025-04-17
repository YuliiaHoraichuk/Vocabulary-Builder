# TO-DO: Load display method can be rewritten as a reusable tk frame

import customtkinter as ctk

from GUI.welcome_display import WelcomeDisplay
from GUI.login_display import LoginDisplay
from GUI.signup_display import SignupDisplay
from GUI.menu_display import MenuDisplay
from user_auth import User

# GUI App Window
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.user = User()

# Configure app window
        self.title("Vocabulary Builder")
        self.geometry("600x400")
        self.resizable(False, False) #disable window resizing

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.current_window = None
        self.load_welcome_display() # load welcome_display when the app launches

        self.username = None

# Display welcome window
    def load_welcome_display(self):
        if self.current_window:
            self.current_window.destroy() # destroy current window to avoid multiple windows being open simultaneously

        self.current_window = WelcomeDisplay(self) # switch to welcome_display window
        self.current_window.set_controller(self)  # set App as controller (MVC pattern)
        self.current_window.grid(row=0, column=0, sticky="nsew")

# Display login window
    def load_login_display(self):
        if self.current_window:
            self.current_window.destroy() # destroy current window to avoid multiple windows being open simultaneously

        self.current_window = LoginDisplay(self) # switch to the login_display window
        self.current_window.set_controller(self) # set App as controller (MVC pattern)
        self.current_window.grid(row=0, column=0, sticky="nsew")

# Display Signup window
    def load_signup_display(self):
        if self.current_window:
            self.current_window.destroy()  # destroy current window to avoid multiple windows being open simultaneously

        self.current_window = SignupDisplay(self) # switch to signup_display window
        self.current_window.set_controller(self) # set App as controller (MVC pattern)
        self.current_window.grid(row=0, column=0, sticky="nsew")

# Collects input from the View (login_display) and passes to the model (user_auth)
    def handle_login(self, username, password):
        if self.user.validate_login(username, password):
            self.username = username # assign before calling load_menu_display(), otherwise username = None
            self.load_menu_display() # if login is successful, display game menu
        else:
            self.current_window.show_error_message()

# If validation successful, load menu display, if not, display error
    def handle_signup(self, username, password, repeat_password):
        # assign return values from validate_signup()
        validation_success, error = self.user.validate_signup(username, password, repeat_password)

        if validation_success:
            self.username = username
            self.load_menu_display()
        else:
            self.current_window.show_error_message(error)

# Display the menu
    def load_menu_display(self):
        if self.current_window:
            self.current_window.destroy()

        self.current_window = MenuDisplay(self) # switch to the menu_display window
        self.current_window.set_controller(self) # set App as controller (MVC pattern)
        self.current_window.grid(row=0, column=0, sticky="nsew")

# Run tkinter loop
if __name__ == "__main__":
    app = App()
    app.mainloop()