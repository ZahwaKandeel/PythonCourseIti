import re
from Day03.read_data import read_data
from Day03.save_data import save_data


def valid_name(name):
    if name.isalpha() and len(name) >= 2:
        return True
    print("Invalid name")
    return False

def valid_email(email):
    email_validation = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(email_validation, email):
        return True
    print("Invalid email")
    return False

def valid_password(password):
    pass_validation = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*-])(?=.{8,32}$)"
    if re.match(pass_validation, password):
        return True
    print("Invalid password")
    return False

def confirm_password(password, confirm_password):
    if password == confirm_password:
        return True
    print("Passwords do not match")
    return False

def valid_phone_number(number):
    phone_validation = r'^01[0125][0-9]{8}$'
    if re.match(phone_validation, number):
        return True
    print("Invalid phone number")
    return False

def registration():
    users = read_data()
    while True:
        first_name = input("Enter first name: ")
        if valid_name(first_name):
            break

    while True:
        last_name = input("Enter last name: ")
        if valid_name(last_name):
            break

    while True:
        email = input("Enter email: ")
        if valid_email(email):
            break

    while True:
        password = input("Enter password: ")
        if valid_password(password):
            break

    while True:
        confirm = input("Confirm password: ")
        if confirm_password(password, confirm):
            break

    while True:
        phone = input("Enter phone number: ")
        if valid_phone_number(phone):
            break

    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone
    }

    users.append(user)
    save_data(users)

    print("\nRegistration completed")