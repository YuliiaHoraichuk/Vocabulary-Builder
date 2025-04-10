import customtkinter as ctk
from user_auth import User

class LoginDisplay(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(width=600, height=400)
        self.grid_columnconfigure(0, weight=1)

        self.login_message = ctk.CTkLabel(self, text="\n Please enter your username and password:")
        self.username_label = ctk.CTkLabel(self, text="Enter your username:")