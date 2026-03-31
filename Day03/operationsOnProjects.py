from tabulate import tabulate
from Day03.read_from_json import read_project
from Day03.save_to_json import save_project
from Day03.createProject import valid_date

projects = read_project()
def view_projects(project=None):
    if not projects:
        print("No projects found")
        return
    if project:
        project_copy = project.copy()
        project_copy.pop("id", None)
        print(tabulate([project_copy], headers="keys", tablefmt="fancy_grid"))
    else:
        projects_copy = []
        for proj in projects:
            temp = proj.copy()
            temp.pop("id", None)
            projects_copy.append(temp)

        print(tabulate(projects_copy, headers="keys", tablefmt="fancy_grid"))

def delete_project():
    project_id = input("Enter project ID to delete: ")

    if not project_id.isdigit():
        print("Invalid id, must be a number")
        return

    project_id = int(project_id)
    updated_projects = []
    found = False

    for project in projects:
        if project["id"] == project_id:
            found = True
        else:
            updated_projects.append(project)

    if not found:
        print("Project not found")
        return

    save_project(updated_projects)
    print("Project deleted")

def search_for_project():
    date = input("Enter date to search for: ")

    if not valid_date(date):
        print("Invalid date format")
        return

    found = False

    for project in projects:
        if project["start_date"] == date:
            view_projects(project)
            found = True

    if not found:
        print("Project not found")

def edit_project():
        project_id = input("Enter project ID to edit: ")

        if not project_id.isdigit():
            print("Invalid id, must be a number")
            return

        project_id = int(project_id)

        for project in projects:
            if project["id"] == project_id:

                print("Project found. Leave empty to keep current value.")

                new_title = input(f"New title ({project['title']}): ")
                new_details = input(f"New details ({project['details']}): ")
                new_target = input(f"New target ({project['target']}): ")

                if new_title:
                    project["title"] = new_title

                if new_details:
                    project["details"] = new_details

                if new_target:
                    if new_target.isdigit():
                        project["target"] = int(new_target)
                    else:
                        print("Invalid target, keeping old value")

                save_project(projects)
                print("Project updated successfully!")
                return


        print("Project not found")
