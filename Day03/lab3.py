from Day03.registration import registration
from Day03.login import login

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            registration()
        elif choice == 2:
            if login():
                print("login successful")
        elif choice == 3:
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()