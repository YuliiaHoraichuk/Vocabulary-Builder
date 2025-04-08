import customtkinter as ctk
from user_auth import LoginDisplay

# GUI class
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Vocabulary Builder")
        self.geometry("600x400")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.login_display = LoginDisplay(self)
        self.login_display.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()