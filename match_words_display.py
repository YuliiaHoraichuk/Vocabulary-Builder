import customtkinter as ctk
import random

class MatchWordsDisplay(ctk.CTkFrame):
    def __init__(self, parent, word_pairs):
        super().__init__(parent)
        self.controller = None
        self.word_buttons = [] # store word buttons
        self.def_buttons = []   # store definition buttons
        self.selected_word = None  # track selected word
        self.matched = 0 # counter
        self.word_pairs = word_pairs

# Two columns: word and definition
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

# Shuffle pairs
        words = []
        definitions = []

        for word, definition in word_pairs:
            words.append(word)
            definitions.append(definition)

        random.shuffle(words)
        random.shuffle(definitions)

        # Create 3 rows of buttons for words and definitions
        for i in range(3):
        # Create the word button
            word_text = words[i]
            word_button = ctk.CTkButton(self, text=word_text, command=lambda x=words[i]: self.select_word(x))
            word_button.grid(row=i, column=0, padx=10, pady=10, sticky="ew")

        # Create the definition button
            definition_text = definitions[i]
            definition_button= ctk.CTkButton(self, text=definition_text,command=lambda x=definitions[i]:
            self.match_definition(x))
            definition_button.grid(row=i, column=1, padx=10, pady=10, sticky="ew")

            self.word_buttons.append(word_button)
            self.def_buttons.append(definition_button)

        # Status label: show correct / wrong / win message
        self.status = ctk.CTkLabel(self, text="", font=("Arial", 16))
        self.status.grid(row=4, column=0, columnspan=2, pady=(20, 10))

        # Go back to the main menu
        self.go_back_button = ctk.CTkButton(self, text="Game Menu", font=("Arial", 18), command=self.go_back)
        self.go_back_button.grid(row=5, column=1, padx=(10, 40), pady=0, sticky="ew")

# Set controller
    def set_controller(self, controller):
        self.controller = controller

# Return to the game menu
    def go_back(self):
        self.controller.load_menu_display()

# When a word button is clicked, store the selected word
    def select_word(self, word):
        self.selected_word = word

# Check for a match
    def match_definition(self, definition):
        # Check if selected word matches clicked definition
        correct = False
        for w, d in self.word_pairs:
            if w == self.selected_word and d == definition:
                correct = True
                break

        if correct:
            self.status.configure(text="Correct!", text_color="green")
            self.matched += 1
        else:
            self.status.configure(text="Try again!", text_color="red")

        # Player wins after 3 correct matches hardcoded since 3 pairs
        if self.matched == 3:
            self.status.configure(text="You win!", text_color="green")