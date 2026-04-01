from Day03.read_from_json import read_data

def login():
    users = read_data('users.json')

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user in users:
        if user['email'] == email and user['password'] == password:
            print("login successful")
            print(f"Welcome {user['first_name']}")
            return True

    print("Invalid email or password")
    return False