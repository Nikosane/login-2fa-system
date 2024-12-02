import json
import hashlib
from database import db_file

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    with open(db_file, "r+") as file:
        data = json.load(file)
        if email in data:
            print("User already exists!")
            return
        data[email] = {"password": hash_password(password)}
        file.seek(0)
        json.dump(data, file, indent=4)
    print("Registration successful!")
