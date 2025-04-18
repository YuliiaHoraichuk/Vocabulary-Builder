import customtkinter as ctk

class HangmanDisplay(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.chances_left = ctk.CTkLabel(self, text="Chances left: ")
        self.chances_left.grid(row=0, column=0, padx=40, pady=0, sticky="nsew")

        self.guess_input = GuessBox(self)
        self.guess_input.grid(row=1, column=0, padx=40, pady=20, sticky="nsew")

        self.keyboard = Keyboard(self)
        self.keyboard.grid(row=2, column=0, padx=40, pady=20, sticky="nsew")

    def set_controller(self, controller):
        self.controller = controller # set the controller

class GuessBox(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.word = "rabbit" # TEMP
        charbox_width = 30
        padding = 3

 # Create 2 extra (left and right) empty columns and set weight=1 to center the inner CTkEntry boxes
        columns = len(self.word) + 2
        self.grid_columnconfigure(0, weight=1) # left column
        self.grid_columnconfigure(columns-1, weight=1) # right column

# Create a separate input box for every letter in the word
        for i, char in enumerate(self.word):
            charbox = ctk.CTkLabel(self, text="", width=charbox_width, height=40, fg_color="white", corner_radius=5)
            charbox.grid(row=0, column=i+1, padx=padding, pady=5, sticky="nsew")

class Keyboard(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        row1 = list("QWERTYUIOP")
        row2 = list("ASDFGHJKL")
        row3 = list("ZXCVBNM")

        self.buttons = {}

        for row_index, row_keys in enumerate([row1, row2, row3]):
            for char_index, key in enumerate(row_keys):
                button = ctk.CTkButton(self, text=key, width=30, height=40)
                button.grid(row=row_index, column=char_index, padx=3, pady=3)
                self.buttons[key] = button