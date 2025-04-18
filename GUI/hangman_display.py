import customtkinter as ctk

class HangmanDisplay(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.chances_left = ctk.CTkLabel(self, text="Chances left: ")
        self.chances_left.grid(row=0, column=0, padx=40, pady=20, sticky="nsew")

    def set_controller(self, controller):
        self.controller = controller # set the controller