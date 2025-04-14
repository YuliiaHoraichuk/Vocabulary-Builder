import customtkinter as ctk

# Main menu: choose game/level/topic + display username/score
class MenuDisplay(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None # set the controller

# Create a 3x3 grid
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)

# Welcome user
        self.welcome_user_message = ctk.CTkLabel(self, font=("Arial", 18))
        self.welcome_user_message.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

    def set_controller(self, controller):
        self.controller = controller # set the controller

        self.welcome_user_message.configure(text=f"Welcome, {self.controller.username}!")
        print(self.controller.username)
