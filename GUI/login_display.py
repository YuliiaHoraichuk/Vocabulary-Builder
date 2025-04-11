import customtkinter as ctk
from user_auth import User

class LoginDisplay(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None # set controller

        #self.configure(width=600, height=400)
        self.grid_columnconfigure(0, weight=1)

        self.login_message = ctk.CTkLabel(self, text="\n Please enter your username and password:")
        self.login_message.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.username_label = ctk.CTkLabel(self, text="Enter your username:")

    def set_controller(self, controller):
        self.controller = controller # set the controller