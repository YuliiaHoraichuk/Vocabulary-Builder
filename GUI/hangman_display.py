import customtkinter as ctk

class HangmanDisplay(ctk.CTkFrame):
    def __init__(self, parent, word):
        super().__init__(parent)
        self.controller = None # set the controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

# Display status: chances left, win or lose
        self.chances_left = ctk.CTkLabel(self, text="Chances left: ", font=("Arial", 20))
        self.chances_left.grid(row=0, column=0, padx=40, pady=0, sticky="nsew")

# Go back to the main menu
        self.go_back_button = ctk.CTkButton(self, text="Game Menu", font=("Arial", 18), command=self.go_back)
        self.go_back_button.grid(row=0, column=1, padx=(10, 40), pady=0, sticky="ew")

# Character labels - letter revealed if it's in the word
        self.guess_input = GuessBox(self, word)
        self.guess_input.grid(row=1, column=0, columnspan=2, padx=40, pady=20, sticky="nsew")

# Keyboard - press key to guess a letter
        self.keyboard = Keyboard(self)
        self.keyboard.grid(row=2, column=0, columnspan=2, padx=40, pady=20, sticky="nsew")

    def set_controller(self, controller):
        self.controller = controller # set the controller
        self.keyboard.set_controller(controller)

# Return to the game menu
    def go_back(self):
        self.controller.load_menu_display()

class GuessBox(ctk.CTkFrame):
    def __init__(self, parent, word):
        super().__init__(parent)

        self.word = word.upper()
        self.charboxes = [] # store char labels
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
            self.charboxes.append(charbox) # store every charbox in a list

    def display_char(self, charlist, char):
        for i in charlist:
            self.charboxes[i].configure(text=char)

# Visual keyboard and related methods (on_click, disable_button)
class Keyboard(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        row1 = list("QWERTYUIOP")
        row2 = list("ASDFGHJKL")
        row3 = list("ZXCVBNM")

        self.buttons = {}

# Iterate through rows and keys to create buttons
        for row_index, row_keys in enumerate([row1, row2, row3]):
            for char_index, key in enumerate(row_keys):
                button = ctk.CTkButton(self, text=key, width=30, height=40, command=lambda x=key: self.on_click(x))
                button.grid(row=row_index, column=char_index, padx=3, pady=3)
                self.buttons[key] = button


    def set_controller(self, controller):
        self.controller = controller # set the controller

# Click key: on click play hangman round (pass as anonymous func to the button command)
    def on_click(self, button):
        self.controller.play_hangman(button)

# Disable key: a key cannot be clicked more than once
    def disable_button(self, char):
        button = self.buttons[char]
        button.configure(state="disabled", fg_color="grey")