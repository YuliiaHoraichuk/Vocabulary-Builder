import customtkinter as ctk
from GUI.welcome_display import LoginDisplay

# GUI App Window
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Vocabulary Builder")
        self.geometry("600x400")

# Disable App window resizing
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

# Display login window
        self.login_display = LoginDisplay(self)
        self.login_display.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()