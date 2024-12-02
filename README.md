# Login System with 2FA

## Overview
A simple Python-based login system implementing Two-Factor Authentication (2FA) via OTP.

## Features
- Secure password hashing using `sha256`.
- Email-based OTP generation and validation.
- User registration and login.

## Requirements
- Python 3.x
- SMTP-enabled email account for sending OTPs.

## Setup
1. Clone this repository:
```
git clone https://github.com/Nikosane/login-2fa-system.git
cd login-2fa-system
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Update email credentials in the `auth/otp.py` file.

4. Run the program:
```
python main.py
```

## Future Enhancements
- Integrate a database (e.g., SQLite or MongoDB).
- Use environment variables for email credentials.
