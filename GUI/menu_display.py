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
        self.welcome_user_message.grid(row=0, column=0, padx=40, pady=10, sticky="nw")

# Warning message - normally hidden
        self.warning_message = ctk.CTkLabel(self, text="Please select game, level, and topic.")
        self.warning_message.grid(row=1, column=0, columnspan=3)
        self.warning_message.grid_forget() # hide warning message

# Store selected game, level, and topic
        self.selected_game = None
        self.selected_lvl = None
        self.selected_topic = None

# Button - Select game
        self.select_game = GameSettings(self, title="Select a game:", values=["Hangman", "Match Words"])
        self.select_game.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

# Button - Select level
        self.select_lvl = GameSettings(self, title="Select Level:", values=["A1", "A2",
                                                                            "B1"])
        self.select_lvl.grid(row=2, column=1, pady=20, sticky="nsew")

# Buton - Select topic
        self.select_topic = GameSettings(self, title="Select Topic:", values=["General", "Education", "Career"])
        self.select_topic.grid(row=2, column=2, padx=20, pady=20, sticky="nsew")

# Button - Start the game
        self.start_game = ctk.CTkButton(self, text="Start", font=("Arial", 18), command=self.start_game)
        self.start_game.grid(row=4, column=1, pady=(10,20))

# Set the controller
    def set_controller(self, controller):
        self.controller = controller
        self.welcome_user_message.configure(text=f"Welcome, {self.controller.username}!")

        # Set the controller for every child (otherwise controller = None)
        self.select_game.set_controller(controller)
        self.select_lvl.set_controller(controller)
        self.select_topic.set_controller(controller)

    def select_options(self, category, option):
        if "game" in category.lower():
            self.selected_game = option
        elif "level" in category.lower():
            self.selected_lvl = option
        elif "topic" in category.lower():
            self.selected_topic = option

    def start_game(self):
        # Display the warning message if not all game settings selected
        if not all([self.selected_game, self.selected_lvl, self.selected_topic]):
            self.warning_message.grid(row=1, column=0, columnspan=3)

        selected_game = self.selected_game.strip().lower()
        selected_lvl = self.selected_lvl.strip().upper()
        selected_topic = self.selected_topic.strip().lower()

        self.controller.launch_game(selected_game, selected_lvl, selected_topic)

# Reusable Dynamic Frame: header and buttons
class GameSettings(ctk.CTkFrame):
    def __init__(self, parent, title, values):
        super().__init__(parent)
        self.controller = None  # set the controller
        self.parent = parent # set the parent reference
        self.values = values # list of button labels
        self.buttons = [] # store buttons

        self.header = ctk.CTkLabel(self, text=title, font=("Arial", 18)) # Frame header
        self.header.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# For every value in the list create a button
        for i, value in enumerate(self.values):
            button = ctk.CTkButton(self, text=value, font=("Arial", 16))
            button.grid(row=i+1, column=0, padx=20, pady=20, sticky="nsew") # row=i+1 bc 1st row is occupied by header
            self.buttons.append((button, value))

# Set the controller and configure button action
    def set_controller(self, controller):
        self.controller = controller # set the controller
        for button, value in self.buttons:
            button.configure(command=lambda x=value: self.on_click(x)) # lambda to bind on_click to the current button

    def on_click(self, value):
        if self.controller:
            self.parent.select_options(self.header.cget("text"), value) # get the widget text value