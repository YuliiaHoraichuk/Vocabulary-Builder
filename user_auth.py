import hashlib
import csv

# Model: User class to handle user data(username/pass/points/level) and actions (login/signup)
class User:
    def __init__(self):
        self.is_logged_in = False
        self.current_user = None

# Validate login: check that the username and the password exists in the database
    def validate_login(self, username_input, password_input):
        with open("user_data", "r") as file:
            for row in csv.reader(file, delimiter="\t"):
                username_csv, password_csv = row # username and password stored in user_data.csv
                if username_input == username_csv and password_input == password_csv:
                    return True
        return False

# Validate password: return (false, error) if doesn't validate; return (true, "") if validates
    def validate_password(self, password_input, repeat_password_input):
        if not password_input == repeat_password_input:
            return False, "Passwords do not match"
        if len(password_input) < 8:
            return False, "Password must be at least 8 characters long"
        return True, ""

# Validate username: return (false, error) if username is taken; return (true, "") if validates
    def validate_username(self, username_input):
        with open("user_data", "r") as file:
            for row in csv.reader(file, delimiter="\t"):
                if username_input == row[0]:
                    return False, "Username already exists"
        return True, ""

    def validate_signup(self, username_input, password_input, repeat_password_input):
        # pass return values from validate_username() to variables
        username, username_error = self.validate_username(username_input)
        if not username:
            print(username_error)
            return False, username_error

        #  pass return values from validate_password() to variables
        password, password_error = self.validate_password(password_input, repeat_password_input)
        if not password:
            print(password_error)
            return False, password_error

# Save new user credentials to the csv file
        with open("user_data", "a") as file:
            file.write(f"{username_input}\t{password_input}\n")



