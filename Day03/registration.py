import re
import uuid
from Day03.read_from_json import read_data
from Day03.save_to_json import save_data

def valid_name(name):
    if name.isalpha() and len(name) >= 2:
        return True
    print("Invalid name")
    return False

def valid_email():
    while True:
        email = input("Enter email: ")
        email_validation = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(email_validation, email):
            return email
        print("Invalid email")
        return False

def valid_password():
    while True:
        password = input("Enter password: ")
        pass_validation = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*-])(?=.{8,32}$)"
        if re.match(pass_validation, password):
            return password
        print("Invalid password")
        return False

def confirm_password(password):
    while True:
        confirm = input("Confirm password: ")
        if password == confirm:
            return password
        print("Passwords do not match")
        return False

def valid_phone_number():
    while True:
        phone = input("Enter phone number: ")
        phone_validation = r'^01[0125][0-9]{8}$'
        if re.match(phone_validation, phone):
            return phone
        print("Invalid phone number")
        return False

def registration():
    users = read_data('users.json')
    while True:
        first_name = input("Enter first name: ")
        if valid_name(first_name):
            break

    while True:
        last_name = input("Enter last name: ")
        if valid_name(last_name):
            break

    email = valid_email()
    password = valid_password()
    confirm_password(password)
    phone = valid_phone_number()

    user = {
        "id": str(uuid.uuid1()),
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone
    }

    users.append(user)
    save_data(users, 'users.json')

    print("\nRegistration completed")