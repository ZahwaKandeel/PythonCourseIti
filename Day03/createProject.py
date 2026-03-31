import time
from datetime import datetime
from Day03.read_from_json import read_project
from Day03.save_to_json import save_project

def valid_title():
    while True:
        title = input("Enter project title: ")
        if len(title.strip()) >= 2:
            return title
        print("Invalid title, insert minimum 2 characters")

def valid_details():
    while True:
        details = input("Enter project details: ")
        if len(details.strip()) >= 10:
            return details
        print("Invalid details, insert minimum 10 characters")

def valid_total_target():
    while True:
        target = input("Enter total target: ")
        if target.isdigit():
            target = int(target)
            if target > 0:
               return target
        print("Invalid target, must be a number")

def valid_date(date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except:
            print("Invalid date format (use YYYY-MM-DD)")

def valid_date_range():
    while True:
        start_date = input("Enter start date (YYYY-MM-DD): ")
        if not valid_date(start_date):
            print("Invalid start date format")
            continue

        end_date = input("Enter end date (YYYY-MM-DD): ")
        if not valid_date(end_date):
            print("Invalid end date format")
            continue

        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        if end > start:
            return start_date, end_date
        else:
            print("End date must be after start date")

def generate_project_id():
    return int(time.time() * 1000)

def create_project():
    projects = read_project()

    project_id = generate_project_id()
    title = valid_title()
    details = valid_details()
    target = valid_total_target()
    start_date, end_date = valid_date_range()

    project = {
        "id": project_id,
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date,
        "end_date": end_date
    }

    projects.append(project)
    save_project(projects)

    print(f"Project created successfully with ID: {project_id}")