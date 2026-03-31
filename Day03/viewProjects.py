from tabulate import tabulate
from Day03.read_from_json import read_project


def view_projects():
    projects = read_project()
    if not projects:
        print("No projects found")
        return
    print(tabulate(projects, tablefmt="fancy_grid"))

# def delete_project():
#     projects = read_project()
#     project_choice = int(input("Insert project id you want to delete : "))

