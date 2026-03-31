from Day03.viewProjects import view_projects
from Day03.createProject import create_project
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
                while True:
                    print("1. Create Project")
                    print("2. View all projects")
                    print("3. Edit your project")
                    print("4. Delete your project")
                    print("5. Search for project")
                    print("6. Back to main menu")

                    project_choice = int(input("Enter your choice: "))

                    if project_choice == 1:
                        create_project()
                    elif project_choice == 2:
                        view_projects()
                    # elif project_choice == 3:
                    #     edit_project()
                    # elif project_choice == 4:
                    #     delete_project()
                    # elif project_choice == 5:
                    #     search_for_project()
                    elif project_choice == 6:
                        break
                    else:
                        print("Invalid choice")

        elif choice == 3:
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()