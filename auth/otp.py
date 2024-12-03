import random
import json
from database import db_file

def send_otp(email):
    otp = random.randint(100000, 999999)
    with open(db_file, "r+") as file:
        data = json.load(file)
        data[email]["otp"] = otp
        file.seek(0)
        json.dump(data, file, indent=4)
    print(f"OTP sent to {email}: {otp}")  # Replace with actual email sending logic
    return True

def validate_otp(email):
    otp = int(input("Enter the OTP: "))
    with open(db_file, "r") as file:
        data = json.load(file)
        return otp == data[email].get("otp")
