import hashlib
import csv

# User class to handle user data(username/pass/points/level) and actions (login/signup)
class User:
    def __init__(self):
        self.is_logged_in = False
        self.current_user = None

    def validate_login(self, username_input, password_input):
        with open("user_data", "r") as file:
            for row in csv.reader(file, delimiter="\t"): # access to csv is working
                username_csv, password_csv = row # username and password stored in user_data.csv
                if username_input == username_csv and password_input == password_csv:
                    #print(username, password)
                    return True
        return False

    def signup(self, username, password):
        pass_match = input("Enter a password again: ")

        if self.password == pass_match:
            with open("user_data", "a") as file:
                writer = csv.writer(file, delimiter = "\t", quotechar = "'", quoting = csv.QUOTE_MINIMAL)
                writer.writerow([self.username, self.password])
        else:
            print("Passwords do not match")


#implement later: check if the username exists in the database and the password is correct

'''
while 1:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        user = User("","")
        user.signup()
    elif choice == 2:
        user = User("","")
        user.login()
    else:
        break
'''
# TEMP! Store user data
users = []


