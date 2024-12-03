import json
from auth.otp import send_otp, validate_otp
from auth.utils import hash_password
from database import db_file

def login_user():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    with open(db_file, "r") as file:
        data = json.load(file)
        if email not in data or data[email]["password"] != hash_password(password):
            print("Invalid credentials!")
            return

    print("Password verified. Proceeding to 2FA...")
    if send_otp(email) and validate_otp(email):
        print("Login successful!")
    else:
        print("Login failed!")
