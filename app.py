# TO-DO: Load display method can be rewritten as a reusable tk frame

import customtkinter as ctk

from GUI.hangman_display import HangmanDisplay
from GUI.welcome_display import WelcomeDisplay
from GUI.login_display import LoginDisplay
from GUI.signup_display import SignupDisplay
from GUI.menu_display import MenuDisplay
from user_auth import User
from hangman_game import HangmanGame

# GUI App Window
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.user = User()
        self.hangman_game = HangmanGame("RABBIT") # hardcoded change later

# Configure app window
        self.title("Vocabulary Builder")
        self.geometry("600x400")
        self.resizable(False, False) #disable window resizing

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.current_window = None
        #self.load_welcome_display() # load welcome_display when the app launches
        # TEMP
        self.load_hangman_display()
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

# Collect input from the View (signup_display) and pass to the Model (user_auth)
    def handle_signup(self, username, password, repeat_password):
        # assign return values from validate_signup()
        validation_success, error = self.user.validate_signup(username, password, repeat_password)

# If the validation is successful, switch to the current user and load the menu
        if validation_success:
            self.username = username
            self.load_menu_display()
        else:
            self.current_window.show_error_message(error) # Display error if registration fails

# Display the menu
    def load_menu_display(self):
        if self.current_window:
            self.current_window.destroy()

        self.current_window = MenuDisplay(self) # switch to the menu_display window
        self.current_window.set_controller(self) # set App as controller (MVC pattern)
        self.current_window.grid(row=0, column=0, sticky="nsew")

# Load the hangman game display
    def load_hangman_display(self):
        if self.current_window:
            self.current_window.destroy()

        self.current_window = HangmanDisplay(self)
        self.current_window.set_controller(self) # set App as controller (MVC pattern)
        self.current_window.grid(row=0, column=0, sticky="nsew")

# Pass logic from hangman_game to update hangman_display
    def play_hangman(self, char):
        guess_correct = self.hangman_game.guess_char(char) # after every guess update View
        self.current_window.keyboard.disable_button(char) # disable button

        # If the guess is correct, reveal the letter in the charboxes widget
        if guess_correct:
            _, positions = guess_correct
            self.current_window.guess_input.display_char(positions, char)

        # If the guess is wrong, chances =- 1
        else:
            self.current_window.chances_left.configure(text=f"Chances left: {self.hangman_game.chances}")

        if self.hangman_game.win():
            self.current_window.chances_left.configure(text="You win!")
            self.current_window.chances_left.configure(text_color="green")

        elif self.hangman_game.lose():
            self.current_window.chances_left.configure(text="You lose!")
            self.current_window.chances_left.configure(text_color="red")

# Run tkinter loop
if __name__ == "__main__":
    app = App()
    app.mainloop()