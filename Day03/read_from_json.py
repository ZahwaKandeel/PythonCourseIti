import json

def read_data():
    try:
        with open('users.json', 'r') as f:
            return json.load(f)

    except Exception as e:
        return []

def read_project():
    try:
        with open('projects.json', 'r') as f:
            return json.load(f)

    except Exception as e:
        return []