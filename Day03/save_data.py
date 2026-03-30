import json

def save_data(users):
    try:
        with open('users.json', 'w') as f:
            json.dump(users, f, indent = 4)
    except Exception as e:
        return []

