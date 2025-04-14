import customtkinter as ctk

# Main menu: choose game/level/topic + display username/score
class Menu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None # set the controller

# Create a 3x3 grid
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)
    
        self.welcome_user_message = ctk.CTkLabel(self, text="Welcome, username!", font=("Arial", 18))
        self.welcome_user_message.grid(row=0, column=0, pad=20, sticky="e")
