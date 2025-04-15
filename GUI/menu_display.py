# TO-DO: MAKE SELECT COLUMNS THE SAME WIDTH
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
        self.welcome_user_message.grid(row=0, column=0, padx=40, pady=20, sticky="nw")

# Display score
        self.score = ctk.CTkLabel(self, text="Score: 0", font=("Arial", 18)) # ADD ACTUAL SCORE LATER
        self.score.grid(row=0, column=1, padx=20, pady=20, sticky="ne")

# Select game
        self.select_game = GameSettings(self, title="Select a game:", values=["Hangman", "Match Words"])
        self.select_game.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

# Select level
        self.select_lvl = GameSettings(self, title="Select Level:", values=["A1 - Beginner", "A2 - Elementary",
                                                                            "B1 - Intermediate"])
        self.select_lvl.grid(row=1, column=1, pady=20, sticky="nsew")

# Select topic
        self.select_topic = GameSettings(self, title="Select Topic:", values=["Topic 1", "Topic 2", "Topic 3"])
        self.select_topic.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")

    def set_controller(self, controller):
        self.controller = controller # set the controller

        self.welcome_user_message.configure(text=f"Welcome, {self.controller.username}!")

# Reusable Dynamic Frame: header + buttons
class GameSettings(ctk.CTkFrame):
    def __init__(self, parent, title, values):
        super().__init__(parent)
        self.values = values # list of button labels
        self.buttons = [] # store buttons

        self.header = ctk.CTkLabel(self, text=title, font=("Arial", 18)) # Frame header
        self.header.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# For every value in the list create a button
        for i, value in enumerate(self.values):
            button = ctk.CTkButton(self, text=value, font=("Arial", 16))
            button.grid(row=i+1, column=0, padx=20, pady=20, sticky="nsew") # row=i+1 bc 1st row is occupied by header
            self.buttons.append(button)

