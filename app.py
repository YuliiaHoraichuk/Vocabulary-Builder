import customtkinter as ctk

from GUI.login_display import LoginDisplay
from GUI.welcome_display import WelcomeDisplay
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

        self.current_window = LoginDisplay(self) # switch to login_display window
        self.current_window.set_controller(self) # set App as controller (MVC pattern)
        self.current_window.grid(row=0, column=0, sticky="nsew")

# Collects input from the View (login_display) and passes to the model (user_auth)
    def handle_login(self, username, password):
        if self.user.validate_login(username, password):
            print("success") # proof of concept - write actual logic later
        else:
            print('error')
            #self.showerror("Incorrect username or password") # seems that showerror is tk method, doesn't exist in ctk
            # Basically when my dummy vaidate_login() returns True, handle_login() prints "success"


# Run tkinter loop
if __name__ == "__main__":
    app = App()
    app.mainloop()