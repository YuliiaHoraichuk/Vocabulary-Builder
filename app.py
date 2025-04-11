import customtkinter as ctk

from GUI.login_display import LoginDisplay
from GUI.welcome_display import WelcomeDisplay

# GUI App Window
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

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
        self.current_window.set_controller(self) # s
        self.current_window.grid(row=0, column=0, sticky="nsew")

# Display login window
    def load_login_display(self):
        if self.current_window:
            self.current_window.destroy() # destroy current window to avoid multiple windows being open simultaneously

        self.current_window = LoginDisplay(self)
        self.current_window.set_controller(self) # set App as controller (MCV pattern)
        self.current_window.grid(row=0, column=0, sticky="nsew")

# Run tkinter loop
if __name__ == "__main__":
    app = App()
    app.mainloop()