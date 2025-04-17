# TO-DO: Reusable tk frame for signup/login display, if there's time
# TO-TO: hide password input: **** not pass

import customtkinter as ctk

class SignupDisplay(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None # set the controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3) # column #2 is bigger to fit input fields

# Signup header
        self.header = ctk.CTkLabel(self, text="\n Create a new account", font=("Arial", 20))
        self.header.grid(row=0, column=0, columnspan=2, padx=20, pady=(40, 30), sticky="nsew")

# Error message row - normally hidden
        self.error_message = ctk.CTkLabel(self, text="", font=("Arial", 16), text_color="red")
        self.error_message.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
        self.error_message.grid_forget()  # hide error message

# Username label and input
        self.username_label = ctk.CTkLabel(self, text="Username:", font=("Arial", 16))  # label
        self.username_label.grid(row=2, column=0, padx=(100, 0), pady=10, sticky="ew")
        self.username_input = ctk.CTkEntry(self)  # input
        self.username_input.grid(row=2, column=1, padx=(0, 100), pady=10, sticky="ew")

# Password label and input
        self.password_label = ctk.CTkLabel(self, text="Password:", font=("Arial", 16))  # label
        self.password_label.grid(row=3, column=0, padx=(100, 0), pady=10, sticky="ew")
        self.password_input = ctk.CTkEntry(self)  # input
        self.password_input.grid(row=3, column=1, padx=(0, 100), pady=10, sticky="ew")

# Repeat Password label and input
        self.repeat_password_label = ctk.CTkLabel(self, text="Repeat password:", font=("Arial", 16))  # label
        self.repeat_password_label.grid(row=4, column=0, padx=(100, 0), pady=10, sticky="w")
        self.repeat_password_input = ctk.CTkEntry(self)  # input
        self.repeat_password_input.grid(row=4, column=1, padx=(0, 100), pady=10, sticky="ew")

# Button - Sign Up
        self.sign_up_button = ctk.CTkButton(self, text="Sign Up", command=self.on_signup)
        self.sign_up_button.grid(row=5, column=0, padx=(120,0), pady=30, sticky="nsew")

# Button - Go back to the welcome window
        self.go_back_button = ctk.CTkButton(self, text="Back", command=self.go_back)
        self.go_back_button.grid(row=5, column=1, padx=(60,120), pady=30, sticky="nsew")

    def set_controller(self, controller):
        self.controller = controller # set the controller

# Collect username and password
    def on_signup(self):
        username = self.username_input.get()
        password = self.password_input.get()
        repeat_password = self.repeat_password_input.get()
        self.controller.handle_signup(username, password, repeat_password)

# Return to welcome window
    def go_back(self):
        self.controller.load_welcome_display()

# Display error message when login credentials are incorrect
    def show_error_message(self, text):
        self.error_message.configure(text=text) # display different error messages
        self.error_message.grid(row=1, column=0,columnspan=2, padx=20, pady=10, sticky="nsew")
        self.username_input.delete(0, "end") # clear username input
        self.password_input.delete(0, "end") # clear password input