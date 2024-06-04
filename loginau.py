import hashlib
import webbrowser

# Dictionary to store user credentials
users = {}

def register():
    print("Register a new user:")
    username = input("Enter username: ")
    if username in users:
        print("User already exists. Please choose a different username.")
        return
    password = input("Enter password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed_password
    print("User registered successfully.")

def login():
    print("Login:")
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username] == hashed_password:
        print("Login successful.")
        return True
    else:
        print("Invalid username or password.")
        return False

def secured_page():
    print("Redirecting to the Oasis website...")
    webbrowser.open("https://www.oasis.com")

def main():
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            if login():
                secured_page()
                break
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
