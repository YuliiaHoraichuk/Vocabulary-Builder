import customtkinter as ctk

# View: Login Window
class LoginDisplay(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None # set the controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3) # column #2 is bigger to fit input fields

# Login header
        self.header = ctk.CTkLabel(self, text="\n Sign in with existing account", font=("Arial", 20))
        self.header.grid(row=0, column=0, columnspan=2, padx=20, pady=(40, 30), sticky="nsew")

# Error message row - normally hidden
        self.error_message = ctk.CTkLabel(self, text="Incorrect username or password. Please try again.",
                                          font=("Arial", 16), text_color="red")
        self.error_message.grid(row=1, column=0,columnspan=2, padx=20, pady=10, sticky="nsew")
        self.error_message.grid_forget() # hide error message

# Username label and input
        self.username_label = ctk.CTkLabel(self, text="Enter your username:", font=("Arial", 16)) # label
        self.username_label.grid(row=2, column=0, padx=(100,0), pady=10, sticky="w")
        self.username_input = ctk.CTkEntry(self) # input
        self.username_input.grid(row=2, column=1, padx=(0,100), pady=10, sticky="ew")

# Password label and input
        self.password_label = ctk.CTkLabel(self, text="Enter your password:", font=("Arial", 16)) # label
        self.password_label.grid(row=3, column=0, padx=(100,0), pady=10, sticky="w")
        self.password_input = ctk.CTkEntry(self) # input
        self.password_input.grid(row=3, column=1, padx=(0,100), pady=10, sticky="ew")

# Button - Sign In
        self.sign_in_button = ctk.CTkButton(self, text="Sign In", command=self.on_login)
        self.sign_in_button.grid(row=4, column=0, padx=(120,0), pady=30, sticky="nsew")

# Button - Go back to the welcome window
        self.go_back_button = ctk.CTkButton(self, text="Back")
        self.go_back_button.grid(row=4, column=1, padx=(60,120), pady=30, sticky="nsew")

    def set_controller(self, controller):
        self.controller = controller # set the controller

# Collect username and password
    def on_login(self):
        username = self.username_input.get()
        password = self.password_input.get()
        self.controller.handle_login(username, password)

# Display error message when login credentials are incorrect
    def show_error_message(self):
        self.error_message.grid(row=1, column=0,columnspan=2, padx=20, pady=10, sticky="nsew")
        self.username_input.delete(0, "end") # clear username input
        self.password_input.delete(0, "end") # clear password input