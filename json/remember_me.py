import json

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is ur name? \n")
    with open (filename, 'w') as f:
        json.dump (username, f)
        print(f"We'll remember u when u come back, {username}")
else:
    print(f"Welcome back {username}!")
