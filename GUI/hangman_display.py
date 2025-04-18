import customtkinter as ctk

class HangmanDisplay(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.chances_left = ctk.CTkLabel(self, text="Chances left: ")
        self.chances_left.grid(row=0, column=0, padx=40, pady=20, sticky="nsew")

        self.guess_input = GuessBox(self)
        self.guess_input.grid(row=1, column=0, padx=40, pady=20, sticky="nsew")

        #self.word = "rabbit"

    def set_controller(self, controller):
        self.controller = controller # set the controller

class GuessBox(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        word = "rabbit" # TEMP
        charbox_width = 30
        padding = 3

        # Create 2 extra (left and right) empty columns and set weight=1 to center the inner CTkEntry boxes
        columns = len(word) + 2
        self.grid_columnconfigure(0, weight=1) # left column
        self.grid_columnconfigure(columns-1, weight=1) # right column

        for i, char in enumerate(word):
            charbox = ctk.CTkEntry(self, width=charbox_width, height=40, justify="center")
            charbox.grid(row=0, column=i+1, padx=padding, pady=5, sticky="nsew")
