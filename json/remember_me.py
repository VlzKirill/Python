import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_user():
    username = input("What is ur name? \n")
    filename = 'username.json'
    with open (filename, 'w') as f:
        json.dump (username, f)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back? {username}")
    else:
        username = get_new_user()
        print(f"We'll remember u when u come back, {username}")

greet_user()