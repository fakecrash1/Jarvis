class User:
    def __init__(self, name):
        self.name = name

class UserManager:
    def __init__(self):
        self.current_user = None

    def login(self, user):
        self.current_user = user

    def logout(self):
        self.current_user = None

fakecrash = User("Fakecrash")
szoszo = User("Szoszo")

user_manager = UserManager()

def select_user():
    print("Please select a user:")
    print("1. Fakecrash")
    print("2. Szoszo")
    user_choice = input("Enter 1 or 2: ")

    if user_choice == "1":
        user_manager.login(fakecrash)
    elif user_choice == "2":
        user_manager.login(szoszo)
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return select_user()

    return user_manager.current_user
