import json
import os
from werkzeug.security import generate_password_hash, check_password_hash

USER_FILE = os.path.join('database', 'users.json')

def load_users():
    if not os.path.exists(USER_FILE):
        return []
    with open(USER_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def find_user_by_mobile(mobile):
    users = load_users()
    return next((u for u in users if u['mobile'] == mobile), None)

def register_user(data):
    users = load_users()
    if any(u['username'] == data['username'] or u['email'] == data['email'] or u['mobile'] == data['mobile'] for u in users):
        return False
    data['id'] = max([u['id'] for u in users], default=0) + 1
    data['password'] = generate_password_hash(data['password'])
    users.append(data)
    save_users(users)
    return True

def authenticate_user(mobile, password):
    user = find_user_by_mobile(mobile)
    if user and check_password_hash(user['password'], password):
        return user
    return None
